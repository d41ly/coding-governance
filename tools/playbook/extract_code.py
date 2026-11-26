# extract_code.py — this kit's copy of the shared `extract_code` block (TOOL-dTotalRecall-13, -8): the
# range extractor and the tokenizers the code record (`code_record.py`) derives each blob through. The
# canonical lives in gov's lib dir, and a parity row there holds the block between the markers
# byte-identical to it, so a change is made in the canonical and copied here whole.
# >>> extract_code — canonical copy: extract_code.py in gov's lib dir (byte-identical; gated)
import ast
import collections
import hashlib
import os
import re
import subprocess
import warnings


#: The shipped `probe` pattern sets. Each one MUST have a frozen sentinel fixture in the lexicon
#: kit's `selftest.py` that yields a non-zero definition count, so a set going inert fails there
#: rather than here.
#:
#: SHIPPED, NOT RESOLVED, and the two names are kept apart on purpose. Every kit carrying this block
#: installs it under `role = "engine"`, so an upgrade overwrites this file: an adopter arming
#: TypeScript, Go or C# by editing the dict below would lose it on the next `apply`, which is why the
#: extractor set is DECLARABLE in `.lexicon.conf` and merged over this one by the lexicon's
#: `resolve_pattern_sets`. Nothing mutates this constant. TOOL-aSurfacedLexicon-9.
PATTERN_SETS = {
    "js-regex": {
        "functions": [
            re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)", re.M),
            re.compile(r"^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>", re.M),
        ],
        "types": [re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z_$][\w$]*)", re.M)],
        "imports": [
            re.compile(r"""^\s*import\s+(?:[^'"]*\s+from\s+)?['"]([^'"]+)['"]""", re.M),
            re.compile(r"""require\(\s*['"]([^'"]+)['"]\s*\)""", re.M),
        ],
    },
}


def ext_of(path: str) -> str:
    """The extension used for a LANGS lookup. A file with no dot in its BASENAME reports `<none>`,
    which must be declared like any other: two such files are tracked here, and letting them fall
    through unnamed is exactly the silent skip the fail-closed law refuses."""
    base = path.rsplit("/", 1)[-1]
    return base.rsplit(".", 1)[-1] if "." in base else "<none>"


def _python_defs(src: str):
    """Definitions and imports from a real parse. A SyntaxError RAISES rather than degrading to an
    empty result: an unparseable file under a `parser` declaration is a broken corpus, and
    returning `[]` would launder it into a clean run."""
    import ast

    tree = ast.parse(src)
    funcs, types_, imports = [], [], []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs.append((node.name, node.lineno))
        elif isinstance(node, ast.ClassDef):
            types_.append((node.name, node.lineno))
        elif isinstance(node, ast.Import):
            imports.extend((a.name, node.lineno) for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            # `from a.b import c` touches BOTH `a.b` and `a.b.c`, and `c` may itself be a module.
            # Keeping only `node.module` discarded the imported NAME, which made the commonest
            # crossing spelling in Python invisible to the deleted P3, and the same discard would
            # blind `check_self_containment` to `from map_lib import _STOPWORDS`. `node.level`
            # carries the leading dots of a relative import and is preserved here rather than
            # silently flattened — that is how the self-containment walk tells relative from bare.
            dots = "." * (node.level or 0)
            mod = node.module or ""
            if dots or mod:
                imports.append((dots + mod, node.lineno))
            for a in node.names:
                if a.name == "*":
                    continue
                sep = "." if mod else ""
                imports.append((dots + mod + sep + a.name, node.lineno))
    return funcs, types_, imports


#: A shell function name, as this parser will accept one. Deliberately the SAME character class the
#: naive same-line regex used, so the two populations are comparable name-for-name and the only
#: difference between them is what the tokenizer could see that a line match could not.
_SH_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

#: Characters that end a heredoc DELIMITER word. Not a general operator set — the tokenizer below
#: dispatches on characters directly and this is the one place it needs a class.
_SH_BREAK = " \t;&|<>\n"


def scan_shell_tokens(src: str) -> list:
    """`[(kind, text, line)]` for shell source: every CODE token, and nothing that is not code.

    `kind` is `word` or `op`; `op` is one of `( ) { }`. Everything else the shell reads as syntax —
    redirections, separators, pipes — is consumed as a word break and emitted as nothing, because
    the four definition forms `parse_shell_defs` recognises need no other operator.

    WHAT IT TRACKS, which is the whole reason this is not a regex: single quotes, double quotes as a
    STATE rather than a span, `$'…'`, backslash escapes and line continuations, `#` comments at a
    word boundary, `${…}` and `$((…))` as opaque expansions, backticks as an opaque span, command
    substitution `$(…)` as suspended-string-state CODE with its own nesting, heredocs with quoted
    and unquoted delimiters in both the plain and `<<-` tab-stripped forms, and here-strings `<<<`.

    THE HERE-STRING IS WHY THE STATE MACHINE EXISTS. `<<<` and a literal run of `<` inside a quoted
    grep pattern are indistinguishable to a line regex and trivially distinguishable here: a
    heredoc-aware REFINEMENT of the naive pattern reads `'^<<<<<<< ours$'` in
    the memory-tree kit's `merge-rows.test.sh` as an opener whose terminator never arrives and blanks
    the thousand lines below it, losing ten real definitions. A tokenizer never enters that branch,
    because the run is inside single quotes.

    RAISES `SyntaxError` on a source it cannot tokenize — an unterminated quote, heredoc or `${`,
    naming the construct and the line it opened on. Never a partial list and never an empty one:
    `scan_corpus` turns that into a named refusal, and returning `[]` would launder a broken file
    into a clean run exactly as it would for `_python_defs`.
    """
    toks: list = []
    word: list = []
    wline = 1
    i, n, line = 0, len(src), 1
    parens: list = []
    heredocs: list = []
    at_word_start = True
    dq = False
    dq_line = 0

    def add_word():
        """Close the word being accumulated, if any, and emit it."""
        nonlocal word
        if word:
            toks.append(("word", "".join(word), wline))
            word = []

    def add_char(s: str):
        """Append source text to the word being accumulated, opening one if none is."""
        nonlocal wline
        if not word:
            wline = line
        word.append(s)

    def read_quoted(j: int, q: str, escapes: bool) -> int:
        """The index just past the `q` that closes a span opened before `j`."""
        while j < n:
            c2 = src[j]
            if escapes and c2 == "\\" and j + 1 < n:
                j += 2
                continue
            if c2 == q:
                return j + 1
            j += 1
        raise SyntaxError(f"unterminated {q} quote opened at line {line}")

    def read_braced(j: int) -> int:
        """The index just past the `}` closing a `${` opened before `j`, counting nesting."""
        depth = 1
        while j < n and depth:
            if src[j] == "\\":
                j += 2
                continue
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
            j += 1
        if depth:
            raise SyntaxError(f"unterminated ${{ opened at line {line}")
        return j

    while i < n:
        c = src[i]

        # --- the expansions a double-quoted string and bare code read the same way ------------
        if c == "\\" and i + 1 < n:
            if src[i + 1] == "\n":
                i += 2
                line += 1
                continue
            add_char(src[i:i + 2])
            i += 2
            at_word_start = False
            continue

        if c == "`":
            j = read_quoted(i + 1, "`", True)
            seg = src[i:j]
            add_char(seg)
            line += seg.count("\n")
            i = j
            at_word_start = False
            continue

        if src.startswith("$((", i):
            j = src.find("))", i + 3)
            if j < 0:
                raise SyntaxError(f"unterminated $(( opened at line {line}")
            seg = src[i:j + 2]
            add_char(seg)
            line += seg.count("\n")
            i = j + 2
            at_word_start = False
            continue

        if src.startswith("${", i):
            j = read_braced(i + 2)
            seg = src[i:j]
            add_char(seg)
            line += seg.count("\n")
            i = j
            at_word_start = False
            continue

        if src.startswith("$(", i):
            # A command substitution's body is CODE, including inside a double-quoted string, so
            # the string state is SUSPENDED here and restored by the `)` that closes it. Handling
            # this by counting parentheses inside the string instead was wrong in both directions
            # and measured so: without the count, `"$(sed "1s/^x*()/y()/")"` closed the string on
            # its inner quote and lost four later definitions; with a bare count, the `(` inside
            # `"$(sed 's/FAILED (\(.*\)/x/')"` closed it one paren early and cost twenty.
            add_word()
            parens.append(("$(", dq))
            dq = False
            i += 2
            at_word_start = True
            continue

        # --- inside a double-quoted string: everything not handled above is literal -----------
        if dq:
            if c == '"':
                add_char('"')
                dq = False
                i += 1
                at_word_start = False
                continue
            if c == "\n":
                line += 1
            add_char(c)
            i += 1
            continue

        # --- code state ------------------------------------------------------------------------
        if c == "\n":
            add_word()
            line += 1
            i += 1
            # A heredoc BODY is not code and is never tokenized. The queue is drained here rather
            # than at the `<<` because a line may open several, and their bodies follow the line.
            while heredocs:
                delim, strip, hline = heredocs.pop(0)
                while True:
                    j = src.find("\n", i)
                    raw = (src[i:] if j < 0 else src[i:j]).rstrip("\r")
                    if (raw.lstrip("\t") if strip else raw) == delim:
                        i = n if j < 0 else j + 1
                        line += 1
                        break
                    if j < 0:
                        raise SyntaxError(
                            f"unterminated heredoc <<{delim} opened at line {hline}")
                    i = j + 1
                    line += 1
            at_word_start = True
            continue

        if c in " \t":
            add_word()
            i += 1
            at_word_start = True
            continue

        if c == "#" and at_word_start:
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue

        if c == "'":
            j = read_quoted(i + 1, "'", False)
            seg = src[i:j]
            add_char(seg)
            line += seg.count("\n")
            i = j
            at_word_start = False
            continue

        if c == '"':
            add_char('"')
            dq, dq_line = True, line
            i += 1
            at_word_start = False
            continue

        if c == "(":
            add_word()
            parens.append(("(", dq))
            toks.append(("op", "(", line))
            i += 1
            at_word_start = True
            continue

        if c == ")":
            add_word()
            marker, was_dq = parens.pop() if parens else ("(", False)
            if marker == "$(":
                dq = was_dq
            else:
                # An UNBALANCED `)` is legal shell — every `case` arm ends with one — so it is
                # emitted rather than refused. Only quote and heredoc states can fail to close.
                toks.append(("op", ")", line))
            i += 1
            at_word_start = True
            continue

        if c in "{}":
            add_word()
            toks.append(("op", c, line))
            i += 1
            at_word_start = True
            continue

        if src.startswith("<<", i):
            add_word()
            strip = src.startswith("<<-", i)
            j = i + (3 if strip else 2)
            while j < n and src[j] in " \t":
                j += 1
            delim: list = []
            while j < n and src[j] not in _SH_BREAK:
                ch = src[j]
                if ch in "'\"":
                    k = read_quoted(j + 1, ch, False)
                    delim.append(src[j + 1:k - 1])
                    j = k
                elif ch == "\\" and j + 1 < n:
                    delim.append(src[j + 1])
                    j += 2
                else:
                    delim.append(ch)
                    j += 1
            i = j
            # A HERE-STRING LANDS HERE WITH AN EMPTY DELIMITER and queues nothing, which is
            # right: `<<<` is `<<` followed by a `<`, and `<` is a word break, so the
            # delimiter scan stops immediately. There WAS an explicit `<<<` arm above this
            # one and it is deleted: reverting it changed not one token anywhere in this
            # corpus, because this path already produced the same result for every
            # here-string in it. A branch whose removal reds nothing is an assertion about
            # nothing, which is the rule the lexicon kit's own gate legs are held to.
            if delim:
                heredocs.append(("".join(delim), strip, line))
            at_word_start = True
            continue

        if c in ";&|<>":
            add_word()
            i += 1
            at_word_start = True
            continue

        add_char(c)
        i += 1
        at_word_start = False

    add_word()
    if dq:
        raise SyntaxError(f'unterminated " quote opened at line {dq_line}')
    if heredocs:
        raise SyntaxError(
            f"unterminated heredoc <<{heredocs[0][0]} opened at line {heredocs[0][2]}")
    return toks


def parse_shell_defs(src: str):
    """Shell function definitions as `(functions, types, imports)`, from a TOKENIZER not a regex.

    FOUR RECOGNISED FORMS, and no fifth: the POSIX `name() { … }`, the bash `function name { … }`,
    the combined `function name() { … }`, and the subshell body `name() ( … )`. The body may open on
    a later line than the name. A name is `[A-Za-z_][A-Za-z0-9_]*`, which is the same class the
    naive same-line regex accepted, so the two readings are comparable name-for-name. Each hit is
    `(name, line)` — the line the NAME is on.

    TYPES AND IMPORTS ARE EMPTY LISTS, and that is a refusal rather than an omission: shell has
    neither in any sense the lexicon kit grades, so the declaration carries no `sh` type cell and P2 grades
    nothing here. The three-list shape is `extract`'s contract and is unchanged.

    THREE REFUSALS, each of which this header owes you because two of them have no runtime behaviour
    to observe:

    1. A file it CANNOT TOKENIZE raises `SyntaxError` naming the construct and the line it opened
       on — an unterminated quote, heredoc or `${`. It never returns an empty or partial list for
       such a file. `scan_corpus` catches that and yields a named refusal, exactly as it does for an
       unparseable Python file, because an unreadable file under an armed declaration is a broken
       corpus and `[]` would launder it into a clean run.
    2. A definition constructed by `eval`, or arriving by `source`/`.` of another file, is NOT
       found. There is no definition SITE to grade: the name exists only after a runtime expansion.
       A sourced file's own definitions are extracted where they are written, which is the right
       answer; this repo carries thirty such constructions and every one of them is out of reach of
       any static extractor, so pretending otherwise would be the green-by-absence claim this parser
       exists to refuse.
    3. A definition inside a HEREDOC BODY is not a definition and is not returned. This is the one
       refusal with a confirmed live instance: the hooks kit's `agent-cap.test.sh` embeds a JavaScript
       `function f() { … }` inside a `<<'EOF'` body, which the naive same-line pattern reports as a
       shell function.

    NOT AN INTERPRETER. It tokenizes and locates; it never evaluates, never expands and never runs
    what it reads. TOOL-aSurfacedLexicon-14.
    """
    return [(name, ln) for name, ln, _at, _body in read_shell_sites(scan_shell_tokens(src))], [], []


def read_shell_sites(toks: list) -> list:
    """`[(name, line, name index, body index)]` for each definition `parse_shell_defs`'s four forms find in
    a shell token stream, the indices into `toks`: the one walk its list and `extract_ranges` read."""
    out, k, m = [], 0, len(toks)
    while k < m:
        kind, text, ln = toks[k]
        if kind == "word" and text == "function" and k + 1 < m and toks[k + 1][0] == "word" \
                and _SH_NAME.match(toks[k + 1][1]):
            j = k + 2
            if j + 1 < m and toks[j][1] == "(" and toks[j + 1][1] == ")":
                j += 2
            if j < m and toks[j][0] == "op" and toks[j][1] in "{(":
                out.append((toks[k + 1][1], toks[k + 1][2], k + 1, j))
                k = j + 1
                continue
        elif kind == "word" and _SH_NAME.match(text) and k + 2 < m \
                and toks[k + 1][1] == "(" and toks[k + 2][1] == ")":
            j = k + 3
            if j < m and toks[j][0] == "op" and toks[j][1] in "{(":
                out.append((text, ln, k, j))
                k = j + 1
                continue
        k += 1
    return out


# ---- TOOL-aGradedDialect-3: the TypeScript reader -----------------------------------------

#: A TypeScript identifier, as this locator will accept one. Deliberately the SAME character class
#: the shipped `js-regex` set accepts, so the two readings of one population are comparable
#: name-for-name and the only difference between them is what the tokenizer could see.
_TS_NAME = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")

#: Words after which a `/` opens a REGEX and a `<` opens a JSX element, because each of them ENDS a
#: statement or an operator rather than an expression. Every other word ends an expression, so the
#: slash divides and the angle compares. This is the ported shape of `scan_shell_tokens`'s
#: `at_word_start`: a state the lexer already knows, never a lookahead over the text.
_TS_EXPR_WORDS = frozenset(
    "return typeof instanceof in of new delete void yield await throw case do else extends".split())

#: The bracket openers `read_ts_type_end` counts. Not a general operator table — the tokenizer
#: dispatches on characters directly and this is the one place a depth walk needs the set.
_TS_OPENERS = ("(", "[", "{", "<")


def check_ts_generic(src: str, i: int) -> bool:
    """A `<` at expression position in a `.tsx` source: a GENERIC parameter list, not a JSX element?

    TypeScript's own tie-break, and the only lookahead in this tokenizer: in a `.tsx` file `<T>` is
    an element and `<T,>` and `<T extends X>` are type parameters, so the construct is decided by
    what follows the NAME and by nothing else. Written down rather than left to the `.ts` reader
    because a `.tsx` file carrying `const pick = <T,>(x) => x` would otherwise scan as an element
    whose closing tag never arrives, and REFUSE the whole file.
    """
    n = len(src)
    j = i + 1
    while j < n and src[j] in " \t\n":
        j += 1
    k = j
    while k < n and (src[k].isalnum() or src[k] in "_$"):
        k += 1
    if k == j:
        return False
    while k < n and src[k] in " \t\n":
        k += 1
    return src[k:k + 1] == "," or src[k:k + 8] == "extends "


def check_ts_tag_start(src: str, i: int) -> bool:
    """A `<` in a `.tsx` source: can what follows it legally OPEN a JSX element?

    A CLOSING TAG reaches here too, and leaving `/` out of the set was a regression this arm caught:
    inside JSX TEXT the `</span>` of a nested element comes back through this dispatch rather than
    through the `jsxtag` frame, and rejecting it emitted `op '<'` and sent the `/` to `read_regex`.
    The rejection is safe only where a JSX element could legally open, since the caller reaches this
    at all only when `expr_end` is False -- `a < /re/.test(x)` never gets here.

    `check_ts_generic` decides the AMBIGUOUS case — `<T>` element versus `<T,>` type parameters —
    and answers False for everything that is not an identifier, which sent `1 << 3` down the JSX
    branch and refused the whole file. A tag name starts with an identifier character and a fragment
    opens `<>`; `<`, `=`, `!` and a digit are operator continuations and can only be arithmetic or a
    comparison, and `/` opens the closing tag the paragraph above is about.
    """
    j = i + 1
    # `.isspace()`, matching `check_ts_generic` thirty lines up. Skipping only space and tab made a
    # newline between `<` and its tag name a fresh refusal on legal JSX, and the divergence between
    # two lookaheads over the same character was a slip rather than an argument.
    while j < len(src) and src[j].isspace():
        j += 1
    c = src[j:j + 1]
    return bool(c) and (c.isalpha() or c in "_$>/")


#: The declarator keywords a `<name>:` annotation can sit under. An object literal's `{ icon: <Home/> }`
#: has a `:` too and its `<` IS an element, so the annotation rule keys on this set rather than on the
#: colon alone — 39 of the frozen corpus's records carry JSX and several carry exactly that shape.
_TS_DECLARATORS = frozenset(
    ("const", "let", "var", "readonly", "public", "private", "protected", "static", "declare"))


def check_ts_generic_fn_type(src: str, i: int) -> bool:
    """A `<` at `i` opens a generic parameter list belonging to a FUNCTION TYPE.

    `<T>(x: T) => T` is a type; `<span>{x}</span>` is an element. The tails are what tell them
    apart -- a generic parameter list is followed by the `(` of the signature it belongs to,
    and an element is followed by its children. Needed because the TOKEN TAIL cannot: an
    interface member and an object-literal property both present `, name :`, and keying the
    member rule on that alone turned `parts.push({ key: "x", node: <span>{t}</span> })` from
    green to a refusal. Round 2 of the closing review predicted that exact shape.
    """
    depth, j, n = 0, i, len(src)
    while j < n:
        if src.startswith("=>", j):
            j += 2
            continue
        ch = src[j]
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
            if depth == 0:
                j += 1
                break
        j += 1
    else:
        return False
    while j < n and src[j] in " \t":
        j += 1
    return src[j:j + 1] == "("


def check_ts_type_position(toks: list, src: str = "", i: int = -1) -> bool:
    """The tokens just emitted put this `<` in a TYPE position, where JSX cannot appear.

    Two shapes, and both were measured refusing valid `.tsx` source before this existed:
    `const f: <T>(x: T) => T = ...`, an annotation under a declarator, and the tail of a `type X =`
    alias, which the caller tracks separately because its body outlives the tokens visible here.
    JSX is a value and a type position holds no values, so a `<` here is always type syntax.
    """
    if len(toks) < 3:
        return False
    # A declarator ANNOTATION: `const f: <T>(x: T) => T = ...`. Keyed on the declarator keyword and
    # deliberately NOT on the colon alone -- an object literal's `{ icon: <Home/> }` has a colon too
    # and its `<` really is an element, which 39 of the frozen corpus's records depend on.
    if toks[-1][0] == "op" and toks[-1][1] == ":" and toks[-2][0] == "word":
        if toks[-3][0] == "word" and toks[-3][1] in _TS_DECLARATORS:
            return True
        # A MEMBER SIGNATURE inside an interface or a type literal: `{ run: <T>(x: T) => T }`.
        # The separator before the name is NOT enough on its own and the first cut of this arm
        # proved it: an object-literal property presents the identical `, name :` tail, so
        # `parts.push({ key: "x", node: <span>{t}</span> })` went from green to a refusal. What
        # separates them is the TAIL of the angle run -- a generic parameter list is followed by
        # the `(` of its signature, an element by its children -- so the source position is
        # required and the token tail alone cannot answer this. Round-2 finding 4, filed as
        # TOOL-aGradedDialect-8 on a hypothesis; the live corpus supplied the instance.
        return (toks[-3][0] == "op" and toks[-3][1] in ("{", ";", ",")
                and i >= 0 and check_ts_generic_fn_type(src, i))
    # A TYPE-ALIAS body: `type Mapper = <T>(x: T) => T`. This replaced a `type_alias` FLAG that was
    # armed on the alias header and cleared at a depth-0 `;`, and the flag was wrong twice over. It
    # never cleared in semicolon-free source, so one ASI alias suppressed JSX for the rest of the
    # file and every later `<` walked its `/` into `read_regex`. And it armed on any depth-0 word
    # `type` with the name optional and `=` indistinguishable from `===`, so an ordinary
    # `item.type === 1 ? <b>on</b>` refused the whole file. A token tail carries no state between
    # statements, so neither failure has anywhere to live: the reading is decided where it is used.
    if toks[-1][0] == "op" and toks[-1][1] == "=" and toks[-2][0] == "word" \
            and toks[-3][0] == "word" and toks[-3][1] == "type":
        return True
    return False


def scan_ts_tokens(src: str, jsx: bool = False, calls=None, conts=None, lits=None) -> list:
    """`[(kind, text, line)]` for TypeScript source: every CODE token, and nothing that is not code.

    `kind` is `word`, `op` or `jsx`. `op` is one of `( ) { } [ ] = : ; , < > =>` and `@` — the
    punctuation `parse_ts_defs` needs. Every other operator the language reads as syntax is consumed
    as a word break and emitted as nothing, because no definition form below needs it.

    THE ONE `jsx` TOKEN, text `<jsx>`, marks where an element OPENS FROM CODE — the outermost `<` of
    a JSX tree, never a nested child and never one inside a `{…}` container, which is suppressed
    like everything else in there. It is the fact the `returns:jsx` selector routes on: a
    definition whose value is one is a component by the only reading that does not consult its
    name. No definition form keys on it — its text matches no op, no keyword and not `_TS_NAME` —
    so `parse_ts_defs` walks past it. It is NOT invisible by construction: the marker occupies a
    position, so a form that read the token AFTER an element as part of the element's own
    statement — `const A = <div />` then `(x) => x` on the next line, an arrow where valid code
    has none — reads differently with it. That is a difference on invalid source only, and it
    is measured rather than argued: the conformance arm and the whole-file arms score the same
    either side of the marker, and every one of 1257 adopter files read identically.

    `calls`, when a set is passed, receives the INDEX of every `(` that opened a CALL rather than
    a grouping. The lexer already knows: `expr_end` is the state that tells `a / b` from `/re/`,
    and a `(` after an expression is an application while one after `return`, `=>`, `?`, `&&`
    or `,` is a parenthesis. The token itself is the same `op` either way, so nothing that reads
    the stream can tell the difference — only the owner walk asks, and it is the difference
    between `=> <A/>` returned and `=> mount(<A/>)` passed.

    `conts`, when a set is passed, receives the INDEX of every token that opens a LINE while an
    operator this lexer does not emit was the last thing consumed — `isValid(a) &&` then a
    newline then `isValid(b)`, or `getItems()` then `.length`. A silent literal opening such a
    line (`cond &&` then `'a' in x`) needs no mark: `lits` below records where it ended, and
    the readers decide the token after it by that record. The token stream cannot tell that
    line from `return noop()` then `const el`, and the two ASI readers need to: the first
    continues an expression, the second ends a statement. `pend` is the flag — set where an
    operator is consumed silently, cleared where an operand ends, whether or not the operand
    emitted a token (a string, a template, a regex and an element do not). Closing review
    round 3: keying this on `expr_end` instead re-opened the generic-close boundary, because a
    `>` clears `expr_end` too.

    `lits`, when a dict is passed, is the other half of the same blindness: the INDEX the next
    token will take after a silent LITERAL — a string, a template, a regex — mapped to the LINE
    the literal ended on, so a literal that spans the break, or opens the later line before a
    word operator (`'a' in x`), is not read as the earlier line's close (round 5); so a reader that
    decides a line break from the last emitted token can see that `open ? 'Open' : 'Closed'`
    closed its line with an operand and not with the `:`. Closing review round 4.

    WHAT IT CONSUMES WITHOUT EMITTING, which is the whole reason this is not a regex: single- and
    double-quoted strings, a template literal's TEXT, `//` and `/* */` comments, a regex literal,
    and JSX text children. A `function` keyword inside a template literal or a JSX text child is
    DATA, and no same-line pattern can tell it from code — this corpus carries one such file, a
    Facebook pixel snippet embedded in a `.tsx` template literal.

    THE STATE IS A STACK, not a set of flags, because the constructs nest: a template literal holds
    a `${}` substitution which may hold another template literal. `/` and `<` are decided by the
    previously LEXED token, never by a lookahead pattern — with the single exception
    `check_ts_generic` names and argues.

    TWO SPANS ARE TOKENIZED AND SUPPRESSED: a template `${…}` substitution and a JSX `{…}`
    expression container. They are lexed so the state machine stays honest about nesting and
    terminators, and no token from inside them is emitted, so `parse_ts_defs` returns no definition
    from either. Spec §8 F2 prices that refusal against the conformance floor rather than arguing
    it away.

    RAISES `SyntaxError` on a source it cannot tokenize, naming the construct and the line it opened
    on. Never a partial list and never an empty one: `scan_corpus` turns that into a named refusal,
    and returning `[]` would launder a broken file into a clean run exactly as it would for
    `_python_defs`.
    """
    toks: list = []
    stack = ["code"]
    opens: list = []
    suppress = 0
    expr_end = False
    i, n, line = 0, len(src), 1

    pend = False

    def add_token(kind: str, text: str) -> None:
        """Emit one token, unless we are inside a suppressed span; note a continuation."""
        nonlocal pend
        if not suppress:
            # A continuation is a token opening a line after a silent operator. A silent LITERAL
            # opening such a line needs no mark: `lits` records where it ended, and the readers
            # decide the token after it by that record alone (rounds 5 to 7 of the closing
            # review built a mark for it, then found the record made the mark unobservable).
            if pend and conts is not None and toks and line > toks[-1][2]:
                conts.add(len(toks))
            toks.append((kind, text, line))
        pend = False

    def read_string(j: int, q: str, wrap: bool = False) -> int:
        """The index just past the `q` that closes a string opened before `j`.

        `wrap` is passed ONLY from the `jsxtag` frame. A code string may not cross a newline
        and a JSX ATTRIBUTE VALUE may, so breaking at the newline unconditionally refused
        every wrapped attribute -- five files on a live adopter corpus, one of which no other
        fix reaches. The code-path callers stay byte-identical rather than sharing a
        loosened rule they do not want.
        """
        while j < n:
            c2 = src[j]
            if c2 == "\\":
                j += 2
                continue
            if c2 == "\n" and not wrap:
                break
            if c2 == q:
                return j + 1
            j += 1
        raise SyntaxError(f"unterminated {q} string opened at line {line}")

    def read_regex(j: int) -> int:
        """The index just past the flags of a regex literal opened before `j`."""
        cls = False
        while j < n:
            c2 = src[j]
            if c2 == "\\":
                j += 2
                continue
            if c2 == "\n":
                break
            if c2 == "[":
                cls = True
            elif c2 == "]":
                cls = False
            elif c2 == "/" and not cls:
                j += 1
                while j < n and src[j].isalpha():
                    j += 1
                return j
            j += 1
        raise SyntaxError(f"unterminated regex literal opened at line {line}")

    while i < n:
        top = stack[-1]
        c = src[i]

        # --- a template literal's TEXT ---------------------------------------------------------
        if top == "tmpl":
            if c == "\\":
                line += src.count("\n", i, min(i + 2, n))
                i += 2
                continue
            if c == "`":
                stack.pop()
                opens.pop()
                expr_end = True
                pend = False
                if lits is not None and not suppress:
                    lits[len(toks)] = line
                i += 1
                continue
            if src.startswith("${", i):
                stack.append("tmplcode")
                opens.append(("${ substitution", line))
                suppress += 1
                expr_end = False
                i += 2
                continue
            if c == "\n":
                line += 1
            i += 1
            continue

        # --- JSX text children ------------------------------------------------------------------
        if top == "jsxchildren":
            if src.startswith("</", i):
                j = src.find(">", i)
                if j < 0:
                    raise SyntaxError(
                        f"unterminated JSX element opened at line {opens[-1][1]}")
                line += src.count("\n", i, j)
                i = j + 1
                stack.pop()
                opens.pop()
                expr_end = True
                pend = False
                continue
            if c == "<":
                stack.append("jsxtag")
                opens.append(("JSX element", line))
                i += 1
                continue
            if c == "{":
                stack.append("jsxexpr")
                opens.append(("JSX expression", line))
                suppress += 1
                expr_end = False
                i += 1
                continue
            if c == "\n":
                line += 1
            i += 1
            continue

        # --- inside a JSX opening tag, where the attributes live --------------------------------
        if top == "jsxtag":
            if src.startswith("/>", i):
                stack.pop()
                opens.pop()
                expr_end = True
                pend = False
                i += 2
                continue
            # COMMENTS ARE LEGAL INSIDE AN OPENING TAG and this frame had no case for them,
            # which was 24 of the 45 files a LIVE adopter corpus refused. Everything inside a
            # comment was lexed as tag content: `// it's fine` opened a string on the
            # apostrophe and `// a > b` ended the tag on the `>`, and each then cascaded to a
            # refusal hundreds of lines later naming a construct that was not there. Mirrored
            # from the code section below rather than re-derived, so two readings of one
            # comment cannot drift apart.
            #
            # AFTER the `/>` case and BEFORE every other one. `/>` cannot collide with `//` or
            # `/*`, so this position is safe, and sitting ahead of the quote and `>` cases is
            # what makes it work at all.
            if src.startswith("//", i):
                j = src.find("\n", i)
                i = n if j < 0 else j
                continue
            if src.startswith("/*", i):
                j = src.find("*/", i + 2)
                if j < 0:
                    raise SyntaxError(f"unterminated /* comment opened at line {line}")
                line += src.count("\n", i, j)
                i = j + 2
                continue
            if c == "<":
                # AN EXPLICIT TYPE ARGUMENT on the element itself -- `<Tabs<Tab> v={1} />`.
                # Without this the type argument's own `>` ended the opening tag and the
                # element's real `/>` became JSX text, refusing the file. 21 of 45.
                #
                # UNCONDITIONAL, and that is only safe because the comment branches above run
                # FIRST. An unrestricted balanced run consumed a `<noscript>` written inside
                # an in-tag comment and turned a green file red, which is the whole reason
                # this edit may not land before the comment fix. A `<` cannot otherwise reach
                # here: an attribute value's angle brackets sit inside a string or an
                # expression container and both have their own case above. Keying it on
                # `toks[-1]` was tried and could not fire at all -- this frame never emits the
                # tag NAME as a token. `=>` is skipped so an arrow inside the type argument
                # does not decrement the depth.
                depth, j = 0, i
                while j < n:
                    if src.startswith("=>", j):
                        j += 2
                        continue
                    if src[j] == "<":
                        depth += 1
                    elif src[j] == ">":
                        depth -= 1
                        if depth == 0:
                            j += 1
                            break
                    elif src[j] == "\n":
                        line += 1
                    j += 1
                else:
                    j = i + 1
                i = j
                continue
            if c == ">":
                stack[-1] = "jsxchildren"
                i += 1
                continue
            if c in "\"'":
                j = read_string(i + 1, c, wrap=True)
                line += src.count("\n", i, j)
                i = j
                continue
            if c == "{":
                stack.append("jsxexpr")
                opens.append(("JSX expression", line))
                suppress += 1
                expr_end = False
                i += 1
                continue
            if c == "\n":
                line += 1
            i += 1
            continue

        # --- code -------------------------------------------------------------------------------
        if c == "\n":
            line += 1
            i += 1
            continue
        if c.isspace():
            # `.isspace()`, not `" \t\r"`: an NBSP or a U+2028 fell through to the operator
            # catch-all and set `pend`, so the next line read as a continuation. The other
            # whitespace skip in this file took the same fix earlier. Closing review round 4.
            i += 1
            continue
        if src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        if src.startswith("/*", i):
            j = src.find("*/", i + 2)
            if j < 0:
                raise SyntaxError(f"unterminated /* comment opened at line {line}")
            line += src.count("\n", i, j)
            i = j + 2
            continue
        if c in "\"'":
            j = read_string(i + 1, c)
            line += src.count("\n", i, j)
            i = j
            expr_end = True
            pend = False
            if lits is not None and not suppress:
                lits[len(toks)] = line
            continue
        if c == "`":
            stack.append("tmpl")
            opens.append(("template literal", line))
            i += 1
            continue
        if c == "/":
            if not expr_end:
                j = read_regex(i + 1)
                line += src.count("\n", i, j)
                i = j
                expr_end = True
                pend = False
                if lits is not None and not suppress:
                    lits[len(toks)] = line
                continue
            i += 1
            expr_end = False
            pend = True
            continue
        if c == "<":
            if jsx and not expr_end and not check_ts_generic(src, i) \
                    and check_ts_tag_start(src, i) \
                    and not check_ts_type_position(toks, src, i):
                add_token("jsx", "<jsx>")
                stack.append("jsxtag")
                opens.append(("JSX element", line))
                i += 1
                continue
            add_token("op", "<")
            i += 1
            expr_end = False
            continue
        if c == "{":
            stack.append("brace")
            opens.append(("{ block", line))
            add_token("op", "{")
            i += 1
            expr_end = False
            continue
        if c == "}":
            if top == "tmplcode" or top == "jsxexpr":
                stack.pop()
                opens.pop()
                suppress -= 1
            else:
                # An unbalanced `}` at the base of the stack is EMITTED rather than refused; only a
                # frame that failed to close is a refusal, and it is raised after the loop.
                if top == "brace":
                    stack.pop()
                    opens.pop()
                add_token("op", "}")
                expr_end = True
            i += 1
            continue
        if src.startswith("=>", i):
            add_token("op", "=>")
            i += 2
            expr_end = False
            continue
        if c in "()[]=:;,>@":
            # `?.(` is an OPTIONAL CALL, and the `?` and `.` before it each cleared `expr_end`
            # on the way through the catch-all — so the state says grouping where the source
            # says application. The two bytes before the paren settle it.
            if c == "(" and (expr_end or src[i - 2:i] == "?.") and calls is not None \
                    and not suppress:
                calls.add(len(toks))
            add_token("op", c)
            i += 1
            expr_end = c in ")]"
            continue
        if c.isalnum() or c in "_$":
            j = i
            while j < n and (src[j].isalnum() or src[j] in "_$"):
                j += 1
            text = src[i:j]
            add_token("word", text)
            expr_end = text not in _TS_EXPR_WORDS
            i = j
            continue
        if c == "!":
            # PREFIX negation arrives with `expr_end` already False and a TypeScript NON-NULL
            # assertion with it already True, so the following `/` is decided correctly either way
            # by what preceded the `!`. Clearing it here made `count! / 2` read as a regex.
            i += 1
            continue
        if c in "+-" and src[i + 1:i + 2] == c:
            # `++` and `--` as ONE token. A postfix bump leaves the lexer after an expression and a
            # prefix one leaves it before one; both are already right in `expr_end`. Consuming these
            # one character at a time cleared it and sent `i++ / 2` to `read_regex` — loudly when the
            # line held one more `/`, and SILENTLY when it held two, swallowing the span between.
            i += 2
            continue
        i += 1
        expr_end = False
        pend = True

    if len(stack) > 1:
        construct, ln = opens[-1]
        raise SyntaxError(f"unterminated {construct} opened at line {ln}")
    return toks


def read_ts_angle_end(toks: list, k: int):
    """The index just past the `>` closing a `<` at `k`, or `None` when that `<` compares.

    Brackets inside the run are counted so a heritage clause's type literals — `extends
    Component<{ a: X }, { b: Y }>` — do not end it, and an unbalanced closer or a `;` at angle
    depth ends the attempt rather than swallowing the rest of the file.
    """
    angle, inner, m, j = 0, 0, len(toks), k
    while j < m and j - k < 400:
        kind, text, _ln = toks[j]
        if kind == "op":
            if text in ("(", "[", "{"):
                inner += 1
            elif text in (")", "]", "}"):
                inner -= 1
                if inner < 0:
                    return None
            elif inner == 0:
                if text == "<":
                    angle += 1
                elif text == ">":
                    angle -= 1
                    if angle == 0:
                        return j + 1
                elif text == ";":
                    return None
        j += 1
    return None


def read_ts_paren_end(toks: list, k: int):
    """The index just past the `)` closing the `(` at `k`, or `None`."""
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if text == "(":
                depth += 1
            elif text == ")":
                depth -= 1
                if depth == 0:
                    return j + 1
        j += 1
    return None


def read_ts_brace_end(toks: list, k: int) -> int:
    """The index just past the `}` closing the `{` at `k`; the end of the list when none does."""
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if text == "{":
                depth += 1
            elif text == "}":
                depth -= 1
                if depth == 0:
                    return j + 1
        j += 1
    return m


def read_ts_type_end(toks: list, k: int, stop: str):
    """The index of the first `stop` op at bracket depth 0 from `k`, or `None`.

    This is how a TYPE ANNOTATION is stepped over without parsing type grammar: the annotation ends
    at the token the caller names — `=` for a variable declaration, `=>` for an arrow's return type
    — and a `,`, `;` or unbalanced closer before it means there was no such annotation.

    A `=>` AT DEPTH 0 IS NOT AN END, and that is the one rule here worth writing down: a function
    TYPE is spelled `(t: Tone) => boolean`, so `let f: (t: Tone) => boolean = function (t) {…}`
    carries a fat arrow inside the annotation that precedes the `=` this walk is looking for.
    """
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if depth == 0 and text == stop:
                return j
            if text in _TS_OPENERS:
                depth += 1
            elif text in (")", "]", "}", ">"):
                depth -= 1
                if depth < 0:
                    return None
            elif depth == 0 and text in (";", ","):
                return None
        j += 1
    return None


def check_ts_arrow(toks: list, k: int) -> bool:
    """Does an arrow function or a function expression START at `k`?

    The four heads: `function`, `async` before any of these, `x =>`, `(params) =>` with an optional
    return-type annotation, and `<T,>(params) =>`.
    """
    m = len(toks)
    if k >= m:
        return False
    kind, text, _ln = toks[k]
    if kind == "word":
        if text == "async":
            return check_ts_arrow(toks, k + 1)
        if text == "function":
            return True
        return k + 1 < m and toks[k + 1][0] == "op" and toks[k + 1][1] == "=>"
    if text == "<":
        j = read_ts_angle_end(toks, k)
        return j is not None and check_ts_arrow(toks, j)
    if text == "(":
        j = read_ts_paren_end(toks, k)
        if j is None:
            return False
        if j < m and toks[j][0] == "op" and toks[j][1] == ":":
            e = read_ts_type_end(toks, j + 1, "=>")
            if e is None:
                return False
            j = e
        return j < m and toks[j][0] == "op" and toks[j][1] == "=>"
    return False


def read_ts_body_start(toks: list, k: int):
    """The index of the body `{` of the callable whose parameter list opens at `k`, or `None`.

    `check_ts_body` is this reader asked as a yes/no; the index is what the `returns:jsx`
    selector needs, because a body is a SCOPE and a scope has a start.
    """
    j = read_ts_paren_end(toks, k)
    if j is None:
        return None
    depth, m = 0, len(toks)
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if depth == 0 and text == "{":
                return j
            if depth == 0 and text in (";", ")", "}", ","):
                return None
            if text == "<":
                # A balanced run is an annotation's type arguments and is stepped over whole;
                # an unbalanced `<` compares, and a comparison after a parameter list is a
                # VALUE, not a return type. Counting it as a bracket let `(x) => x > 1` in a
                # member value walk into a later `if (a < b) {` and take that block for the
                # body (closing review round 3).
                e = read_ts_angle_end(toks, j)
                if e is None:
                    return None
                j = e
                continue
            if text in ("(", "["):
                depth += 1
            elif text in (")", "]"):
                depth -= 1
                if depth < 0:
                    return None
        j += 1
    return None


def check_ts_body(toks: list, k: int) -> bool:
    """Does the callable whose parameter list opens at `k` carry a BODY?

    An OVERLOAD SIGNATURE is a declaration terminated by `;` with no body, and TypeScript reports
    the implementation rather than the signatures — so returning one would be a definition site the
    oracle does not count. The scan steps over a return-type annotation on the way, including one
    that is itself a type literal: `function f(): { a: string } {` reaches its body brace because
    the type literal's own `{` is the first at depth 0 either way, and the `;` inside it is not.
    """
    return read_ts_body_start(toks, k) is not None


def read_ts_arrow_body(toks: list, k: int):
    """The index of the first BODY token of the arrow or function expression starting at `k`.

    For an arrow that is the token after `=>` — a `{` for a block body, anything else for an
    expression body. For a `function` expression it is the body brace itself. `None` when no
    such form starts at `k`, or when its body cannot be found; `check_ts_arrow` is NOT rewritten
    over this on purpose, so the graded population cannot move with the scope reader.
    """
    m = len(toks)
    if k >= m:
        return None
    kind, text, _ln = toks[k]
    if kind == "word":
        if text == "async":
            return read_ts_arrow_body(toks, k + 1)
        if text == "function":
            j = k + 1
            if j < m and toks[j][0] == "word":
                j += 1
            if j < m and toks[j][0] == "op" and toks[j][1] == "<":
                a = read_ts_angle_end(toks, j)
                j = a if a is not None else j
            if j < m and toks[j][0] == "op" and toks[j][1] == "(":
                return read_ts_body_start(toks, j)
            return None
        if k + 1 < m and toks[k + 1][0] == "op" and toks[k + 1][1] == "=>":
            return k + 2 if k + 2 < m else None
        return None
    if text == "<":
        j = read_ts_angle_end(toks, k)
        return read_ts_arrow_body(toks, j) if j is not None else None
    if text == "(":
        j = read_ts_paren_end(toks, k)
        if j is None:
            return None
        if j < m and toks[j][0] == "op" and toks[j][1] == ":":
            e = read_ts_type_end(toks, j + 1, "=>")
            if e is None:
                return None
            j = e
        if j < m and toks[j][0] == "op" and toks[j][1] == "=>":
            return j + 1 if j + 1 < m else None
    return None


#: A token that, ending a line, lets the EXPRESSION continue on the next. Every op but a closer,
#: and the words that must be followed by an operand. Anything else at a line end is where ASI
#: ends a brace-less arrow body.
_TS_EXPR_CONTINUES = frozenset(("(", "[", "{", "=", ":", ",", "<", ">", "=>", "@")) | _TS_EXPR_WORDS



def read_ts_expr_end(toks: list, k: int, conts=frozenset(), lits=None) -> int:
    """The index just past the brace-less arrow body that starts at `k`.

    It ends at a depth-0 `;` or `,`, at an unbalanced closer, or at a line break that ends a
    statement under ASI — the rule applied to the tokens this lexer emits, plus two facts the
    lexer hands over. A line continues the one before it when its first token is in `conts`
    (an operator this lexer does not emit was the last thing consumed: `isValid(a) &&` then
    `isValid(b)`, `cond` then `? a`), when it opens with an ELEMENT (the lexer opens one only
    after an operator), or with `:` or `,`; and it ends when the earlier line closed with a
    token that cannot continue — a word, a closer, or a `>` that closes a generic run after
    `as`, `satisfies` or `new`, while a comparison `>` continues; and it ends when the earlier
    line closed with a silent LITERAL (`lits`: a string, a template, a regex), whatever token
    was emitted before it. The ceiling that remains is a line opening with `(` or `[` after an
    operand, read as a new statement — the one ASI hazard every semicolon-free style guide
    tells its readers to avoid. The rule is the line and not
    the next semicolon, because the other reading swallows every semicolon-less statement
    after the arrow, and a module-level element two lines down would make a plain helper a
    component. `check_ts_returned` is the backward twin and reads the same facts.
    """
    lits = lits or {}
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, ln = toks[j]
        # A literal that ended right before `j` is decided by ITS record, never by the token
        # before the literal: one that started earlier and ended on this line is an operand on
        # this line, whatever sat before it (round 6).
        if depth == 0 and j > k and ln > toks[j - 1][2] and j not in conts \
                and (lits[j] < ln if j in lits else
                     (toks[j - 1][1] not in _TS_EXPR_CONTINUES
                      or check_ts_generic_close(toks, j - 1))) \
                and kind != "jsx" and text not in (":", ","):
            return j
        if kind == "op":
            if text in ("(", "[", "{"):
                depth += 1
            elif text in (")", "]", "}"):
                depth -= 1
                if depth < 0:
                    return j
            elif depth == 0 and text in (";", ","):
                return j
        j += 1
    return m


def read_ts_block_kind(prev, cur: str, pend) -> str:
    """Which KIND of block a `{` opens: `statement`, `class`, `object` or `type`.

    THE WHOLE REASON A REGEX CANNOT DO THIS. A property signature in an interface and a property
    assignment in an object literal are spelled identically — `render: (el: HTMLElement) => string`
    is a function TYPE in one and a function DEFINITION in the other — and only the enclosing block
    tells them apart. This corpus carries the case: `interface Window` declares two such properties
    and the oracle counts ZERO functions in it.

    `pend` is the kind a `class`, `interface`, `enum` or `type` header already decided; `cur` is the
    enclosing block, which is what routes a `:` to a nested type literal inside a type and to a
    nested object literal inside an object.
    """
    if pend:
        return pend
    if prev is None:
        return "statement"
    pk, pt, _ln = prev
    if pk == "op":
        if pt == ":":
            return "object" if cur == "object" else "type"
        if pt in ("=", "(", ",", "[", "<"):
            return "type" if cur == "type" else "object"
        return "statement"
    if pt in ("as", "satisfies", "extends", "implements"):
        return "type"
    if pt in ("return", "case"):
        return "object"
    return "statement"


#: Tokens that can END a line and still continue a type on the next one. Anything else at a line
#: end is an ASI MEMBER BOUNDARY: `label: string` then a newline then `onClick = () => {}` is TWO
#: members, and a walk that crosses it finds the SECOND member's `=`, grades the first member's
#: annotation word as a function name, and skips the real name entirely.
_TS_TYPE_CONTINUES = frozenset(("=", "|", "&", ",", "<", "(", "[", ":", "extends", "keyof",
                                "typeof", "infer", "readonly", "new", "=>"))

#: What may sit directly before a class member's NAME. A ternary's `:` sits after a VALUE, so
#: keying the annotation arm on this set is what stops `x = cond ? aVal : bVal` grading `aVal`.
_TS_MEMBER_HEAD = frozenset(("{", "}", ";", "public", "private", "protected", "readonly",
                             "static", "abstract", "override", "declare", "async"))


def check_ts_member_annotation(toks: list, k: int, e: int) -> bool:
    """The span `k`..`e` is ONE class member's type annotation, not a walk across a boundary.

    `read_ts_type_end` stops at a depth-0 `;` or `,` or an unbalanced closer, and ASI supplies
    none of them between two class members. So the bound here is the LINE: a token opening a new
    line whose predecessor could not continue a type ends the annotation, whatever
    `read_ts_type_end` thought. Measured before this existed:
    `class A { label: string NEWLINE onClick = () => {} }` graded `label` and never graded
    `onClick` -- D3's own defect, reintroduced by D3's own fix.
    """
    for j in range(k + 1, min(e, len(toks))):
        prev = toks[j - 1]
        if toks[j][2] > prev[2] and prev[1] not in _TS_TYPE_CONTINUES:
            return False
    return True


def parse_ts_defs(src: str, jsx: bool = False):
    """TypeScript definitions as `(functions, types, imports)`, from a TOKENIZER not a regex.

    THE RECOGNISED FORMS, mirroring the oracle's set so recall and precision are comparable form for
    form: `function <name>` including `export`, `export default`, `async` and generator forms; a
    class or object-literal METHOD and a `get` or `set` accessor, under the name the oracle records;
    `constructor`; a `const`, `let` or `var` bound to an arrow or a function expression; a property
    assignment or class property initialised to one. `class`, `interface`, `type` and `enum` are
    types. Each hit is `(name, line)` — the line the NAME is on, never its body's.

    `jsx` picks the LEXER, and the two extensions take two `PARSERS` ids for that reason: `.ts`
    lexes `<T>(x) => x` as a generic arrow and `.tsx` lexes `<T>` as an element, so one lexer mode
    necessarily mis-reads one of the two populations.

    SIX REFUSALS, and this header owes you every one of them because three have no runtime failure
    to stage:

    1. A source it CANNOT TOKENIZE raises `SyntaxError` naming the construct and the line it opened
       on: an unterminated string, template literal, `${ substitution`, `/* comment`, regex literal,
       `{ block` or JSX element. It never returns an empty or partial list for such a file.
       `scan_corpus` turns that into a named refusal, because an unreadable file under an armed
       declaration is a broken corpus and `[]` would launder it into a clean run.
    2. A definition written inside a template `${…}` substitution or a JSX `{…}` expression
       container is NOT returned. Those spans are tokenized and SUPPRESSED — the ported shape of
       `scan_shell_tokens`, which treats `${…}` and `$((…))` as opaque — and the cost is priced
       against the conformance floor rather than argued away. Spec §8 F2.
    3. An OVERLOAD SIGNATURE — a `function` declaration terminated by `;` with no body — is not a
       definition. TypeScript reports the implementation, and so does this.
    4. A definition constructed by `eval`, by a decorator, or arriving through an `import` is NOT
       found. There is no definition SITE to grade: the name exists only after a runtime step.
    5. A COMPUTED or string-literal property key — `[k]: () => …`, `"on-change": () => …` — is not
       returned. The locator names a definition by its identifier and there is none to name; the
       oracle drops computed keys before they reach a record for the same reason.
    6. IMPORTS ARE AN EMPTY LIST, and that is a refusal rather than an omission: the corpus walk
       discards the third element, the only import consumer reads the lexicon kit's own Python directly,
       and a populated list would be an ungraded population with a fixture obligation. The
       three-list shape is `extract`'s contract and is unchanged. `parse_shell_defs` set the
       precedent for types.

    NOT AN INTERPRETER. It tokenizes and locates; it never resolves a type, walks a module graph,
    evaluates or runs what it reads. TOOL-aGradedDialect-3.
    """
    funcs, types_, _owned = parse_ts_source(src, jsx)
    return funcs, types_, []


def parse_ts_source(src: str, jsx: bool = False):
    """`(functions, types, jsx_owners)`: `parse_ts_defs`'s two lists plus the set of INDICES into
    `functions` whose own body holds a JSX element.

    A DEFINITION OWNS AN ELEMENT WHEN THE ELEMENT IS ITS VALUE, and three words in that rule each
    cost a measurement against the adopter corpus this build exists for, read 2026-09-11 (601
    `.tsx` files, 3145 functions, 951 offenders when the cell is armed blind). Every figure below
    is that read; none is derivable here, which is why each carries the date.

    DEFINITION means a DECLARED name — `function name` whether statement or named expression, and
    `const`, `let` or `var` bound to an arrow or a function expression. An object property, a
    class property and a method are NOT scopes here, because a member's name is its container's
    KEY: `render: (r) => <td />` is spelled by the API that reads `config.render`, and a casing
    rule cannot move it. Counting members routed 121 such slots on that corpus and 8 components;
    excluding them leaves the 8 in the parent cell, where they pin.

    VALUE means the element sits at CALL DEPTH ZERO in the body's value expression — a brace-less
    arrow body, or the expression after a `return` inside a block body. A grouping parenthesis
    (`return (`, `=> (`, `cond ? (`, `open && (`) does not raise the depth; a call, an array
    literal or an object literal does. So `=> <A />` and `return x ? <A /> : null` are returned,
    and `=> mount(<A />)`, `return renderToStaticMarkup(<A />)` and `return [{ el: <A /> }]` are
    not — a component RETURNS an element, a test helper hands one to something. "Contains" was
    the first cut and it pinned 162 names on that corpus; this pins 86.

    OWNS means the INNERMOST function spanning the element, named or not, and only a declared
    name routes. So a hook that defines a component inside itself is not one — `function
    useThing() { const Row = () => <tr />; return Row; }` routes `Row` and leaves `useThing` in
    the parent — and an anonymous callback ABSORBS what it renders: `return (props) => <C />` is a
    higher-order function returning a component, not a component, and the element is the
    arrow's. Every `=>`, every nameless `function` and every METHOD body opens such a scope —
    a HOC returning `class extends Component { render() { return <W /> } }` is not routed for
    its member's element either; a declared arrow's `=>` opens a duplicate with identical bounds,
    and the named one wins the tie. What this
    reading therefore misses is the component whose whole value is a callback's — `const List =
    () => items.map((i) => <li />)` — beside `return createPortal(<A />, el)` and `return null`,
    a component with no element to see. A scope is a body brace to its match, or a brace-less
    body to where `read_ts_expr_end` stops. An element outside every scope — a module-level
    `const el = <div />` — belongs to nobody.

    The two lists are the ones `parse_ts_defs` has always returned, computed by the same
    predicates in the same order; the scope reads run only after a name is appended, so they
    cannot move the population — with TWO deliberate exceptions the closing review made this
    header own, both fabricated identifiers of the class the class-annotation arm documents.
    The anonymous-function scope arm consumes a `function` word that no name follows, and
    before it existed that word FELL THROUGH to the member arm, matched `_TS_NAME`, and entered
    the population as a definition called `function`: `{ foo: function () {} }` graded `foo`
    AND `function`. And `read_ts_body_start` once counted `<` and `>` as brackets and never
    refused below zero, so a CALL inside an array or object member — `rail: [blk("Callout",
    { title: "R" })]` — could balance by accident onto a later `{` and be graded as a method
    named `blk`. Both are gone. Measured 2026-09-13 against the base reader over the adopter
    corpus: 1261 of 1265 files identical, and the four that differ lose nine such call sites
    and gain nothing. Each is pinned by an arm. Otherwise this is one walk and not a second
    parser over the same tokens.
    """
    calls: set = set()
    conts: set = set()
    lits: dict = {}
    toks = scan_ts_tokens(src, jsx, calls, conts, lits)
    funcs: list = []
    types_: list = []
    scopes: list = []
    blocks = ["statement"]
    pend = None
    k, m = 0, len(toks)

    def add_scope(body, owner: int):
        """Record the body starting at token `body` as a scope owned by `funcs[owner]`, or by
        nobody when `owner` is -1 — an anonymous function, which absorbs and never routes.

        Owned scopes come from the two declaration arms and from no member arm, which is the
        rule in the header and not an omission.
        """
        if body is None or body >= m:
            return
        if body and toks[body - 1][1] == "=>" and body not in conts \
                and lits.get(body, toks[body][2]) < toks[body][2]:
            # The arrow's value was a silent literal — `(i) => `k-${i}`` — and `body` is the
            # NEXT statement's first token; the scope is empty, and opening it there graded
            # the next line's element as the helper's (closing review round 4). Keyed on the
            # `=>` before it: a `{` after a return type ending in a literal TYPE is a body
            # (round 5).
            return
        if toks[body][0] == "op" and toks[body][1] == "{":
            scopes.append((body, read_ts_brace_end(toks, body), owner))
        else:
            scopes.append((body, read_ts_expr_end(toks, body, conts, lits), owner))

    while k < m:
        kind, text, ln = toks[k]
        cur = blocks[-1]

        if kind == "op":
            if text == "<":
                # A balanced generic run is SKIPPED whole, so a type argument's own braces cannot
                # be read as a block. `read_ts_angle_end` returns None where the `<` compares.
                j = read_ts_angle_end(toks, k)
                k = j if j is not None else k + 1
                continue
            if text == "{":
                # THE PREV TOKEN IS READ PAST THE MARKER. `return <A /> || { render: () => 1 }`
                # classified its brace by `return` in 1.3 and by the marker in 1.4, which made it
                # a `statement` block and LOST the member — the one silent shrink the closing
                # review found in the marker's wake. The marker is not a token any form reads.
                p = k - 1
                while p >= 0 and toks[p][0] == "jsx":
                    p -= 1
                want = read_ts_block_kind(toks[p] if p >= 0 else None, cur, pend)
                pend = None
                if want == "type":
                    # A type carries no definition site, so it is stepped over whole rather than
                    # walked. That is what keeps an interface's property SIGNATURES out of `funcs`.
                    k = read_ts_brace_end(toks, k)
                    continue
                blocks.append(want)
                k += 1
                continue
            if text == "}":
                if len(blocks) > 1:
                    blocks.pop()
                k += 1
                continue
            if text == ";":
                pend = None
            if text == "=>":
                add_scope(k + 1, -1)
            if text == "(" and cur in ("object", "class"):
                # A METHOD BODY absorbs like an anonymous function's, and it is opened on the
                # syntactic body — a parameter list followed by a brace, inside a member
                # block — whatever spells the key: a word, `render<T>(`, `[k](`, `'render'(`.
                # Round 2 of the closing review: keyed on the population arm, three of those
                # spellings leaked their element to the enclosing declared function. A `(`
                # inside a member VALUE that is not a method finds no body brace and opens
                # nothing.
                add_scope(read_ts_body_start(toks, k), -1)
            k += 1
            continue

        nxt = toks[k + 1] if k + 1 < m else None
        nt = nxt[1] if nxt else ""

        if text == "function" and nxt and nxt[0] == "word" and _TS_NAME.match(nt):
            j = k + 2
            if j < m and toks[j][0] == "op" and toks[j][1] == "<":
                a = read_ts_angle_end(toks, j)
                j = a if a is not None else j
            if j < m and toks[j][0] == "op" and toks[j][1] == "(" and check_ts_body(toks, j):
                funcs.append((nt, nxt[2]))
                add_scope(read_ts_body_start(toks, j), len(funcs) - 1)
            k += 1
            continue
        if text == "function":
            add_scope(read_ts_arrow_body(toks, k), -1)
            k += 1
            continue

        if text in ("class", "interface", "enum") and nxt and nxt[0] == "word" \
                and _TS_NAME.match(nt):
            types_.append((nt, nxt[2]))
            pend = "class" if text == "class" else "type"
            k += 2
            continue

        if text == "type" and nxt and nxt[0] == "word" and _TS_NAME.match(nt) \
                and k + 2 < m and toks[k + 2][0] == "op" and toks[k + 2][1] in ("=", "<"):
            types_.append((nt, nxt[2]))
            pend = "type"
            k += 2
            continue

        if cur == "statement" and text in ("const", "let", "var") and nxt \
                and nxt[0] == "word" and _TS_NAME.match(nt):
            j = k + 2
            if j < m and toks[j][0] == "op" and toks[j][1] == ":":
                e = read_ts_type_end(toks, j + 1, "=")
                j = e if e is not None else m
            if j < m and toks[j][0] == "op" and toks[j][1] == "=" \
                    and check_ts_arrow(toks, j + 1):
                funcs.append((nt, nxt[2]))
                add_scope(read_ts_arrow_body(toks, j + 1), len(funcs) - 1)
            k += 1
            continue

        if cur == "class" and _TS_NAME.match(text) and nt == ":" and nxt[0] == "op" \
                and (k == 0 or toks[k - 1][1] in _TS_MEMBER_HEAD):
            # A class PROPERTY carrying a type ANNOTATION. Without this arm the `nt == "="` arm
            # below sees the annotation's LAST WORD sitting in front of the `=` and grades that:
            # `private onChange: (e: Event) => void = (e) => {}` appended `void`, and a realistic
            # `handleClick: React.MouseEventHandler = () => {}` appended `MouseEventHandler`. A
            # FABRICATED identifier entered the graded population -- P1 offenders, the `.conv` cell
            # pins, `--list` -- while the property's real name was never graded at all. `_TS_NAME`
            # matches `void`, so no downstream keyword filter caught it. The `const` arm at the top
            # of this loop has always stepped its annotation this way; the class arm did not.
            e = read_ts_type_end(toks, k + 2, "=")
            bounded = e is not None and check_ts_member_annotation(toks, k + 2, e)
            if bounded and e < m and toks[e][0] == "op" and toks[e][1] == "=" \
                    and check_ts_arrow(toks, e + 1):
                funcs.append((text, ln))
            # Step past the annotation whether or not it held an arrow, so that no token INSIDE
            # it can reach the arms below and be graded as a name -- but ONLY when the span really
            # was this member's annotation. An unbounded `k = e` jumped to the NEXT member's `=`,
            # so rejecting the cross-boundary walk stopped `label` being graded and lost `onClick`
            # with it. Trading a fabricated name for a missing one is not a fix.
            k = e if bounded else k + 1
            continue

        if cur in ("object", "class") and _TS_NAME.match(text):
            if nt == "(" and nxt[0] == "op" and check_ts_body(toks, k + 1):
                funcs.append((text, ln))
                # The method's SCOPE is opened by the `(` branch above, on the body rather
                # than on this arm, so a method this arm cannot name still absorbs.
            elif cur == "object" and nt == ":" and nxt[0] == "op" \
                    and check_ts_arrow(toks, k + 2):
                funcs.append((text, ln))
            elif cur == "class" and nt == "=" and nxt[0] == "op" \
                    and check_ts_arrow(toks, k + 2):
                funcs.append((text, ln))
        k += 1

    # THE OWNER WALK, after the population is final so it cannot move it. Scopes nest, so the
    # innermost one spanning a marker is the one with the LATEST start; a marker no scope spans
    # is module-level and belongs to nobody.
    owned: set = set()
    for mk in (i for i, t in enumerate(toks) if t[0] == "jsx"):
        inner = max((sc for sc in scopes if sc[0] <= mk < sc[1]), default=None)
        if inner is not None and inner[2] >= 0 \
                and check_ts_returned(toks, calls, conts, lits, inner[0], mk):
            owned.add(inner[2])
    return funcs, types_, owned


#: What may sit before the dotted name of a generic run that ENDS a statement: `v as Foo<Bar>`,
#: `x satisfies Foo<T>`, `new Map<string, Foo>` with no call parens. A `>` that pairs with an
#: earlier `<` under any other head is a comparison — `a < b && c >` newline `d ? ...` — and
#: continues (closing review round 3). THE CEILING THAT KEY BUYS: a bare instantiation
#: expression ending a line, `return makeBox<string>` (TypeScript 4.7), has no head and reads
#: as a comparison, so the next line continues it. A head-free rule cannot tell that from
#: `return a < b && c >`, and the comparison is the shape prettier emits (round 4, stated).
_TS_GENERIC_HEADS = frozenset(("as", "satisfies", "new"))

#: The expression words a type-argument run can NEVER hold. `typeof`, `void`, `new`, `in` and
#: `extends` all can — `ReturnType<typeof f>`, `Promise<void>`, `Map<string, () => void>`,
#: `T extends U` — so bounding the search on every expression word read those runs as
#: comparisons (closing review round 5). A `;` is not here either: `read_ts_angle_end` already
#: refuses one at depth zero, and a `{ a: string; b: number }` type literal holds one inside.
_TS_STMT_WORDS = _TS_EXPR_WORDS - frozenset(("typeof", "void", "new", "in", "extends"))


def check_ts_generic_close(toks: list, j: int) -> bool:
    """Does the `>` at `j` CLOSE a statement-ending type-argument run — `v as Foo<Bar>` — rather
    than compare? Read backward for the `<` whose balanced run ends exactly here, then over the
    dotted name before it (consecutive words, since `.` is not emitted) to the keyword that
    heads it; anything but `as`, `satisfies` or `new` there is a comparison pair.
    """
    if toks[j][0] != "op" or toks[j][1] != ">":
        return False
    depth = 0
    for i in range(j - 1, max(j - 400, 0), -1):
        # No type-argument run holds a statement keyword AT ITS OWN DEPTH, so reaching one
        # before the `<` means the `>` pairs with nothing in ITS statement — an `as` two
        # statements up must not make a comparison here a boundary (round 4). STATEMENT words,
        # not expression words: the run may hold `typeof`, `void`, `new` (round 5). And not
        # inside a group or in member position: `Record<string, { delete: boolean }>` holds
        # `delete` as a KEY and `ReturnType<typeof api.delete>` as an elided-dot MEMBER, a word
        # directly after a word on the same line (round 6).
        kind_i, text_i, line_i = toks[i]
        if kind_i == "op" and text_i in (")", "]", "}"):
            depth += 1
            continue
        if kind_i == "op" and text_i in ("(", "[", "{"):
            if depth == 0:
                return False
            depth -= 1
            continue
        if depth:
            continue
        if kind_i == "word" and text_i in _TS_STMT_WORDS \
                and not (toks[i - 1][0] == "word" and toks[i - 1][2] == line_i):
            return False
        if kind_i == "op" and text_i == "<" and read_ts_angle_end(toks, i) == j + 1:
            p = i - 1
            while p >= 0 and toks[p][0] == "word" and toks[p][1] not in _TS_GENERIC_HEADS \
                    and toks[p][1] not in _TS_STMT_WORDS:
                p -= 1
            return p >= 0 and p < i - 1 and toks[p][0] == "word" and toks[p][1] in _TS_GENERIC_HEADS
    return False


def check_ts_returned(toks: list, calls: set, conts: set, lits: dict, start: int, mk: int) -> bool:
    """Is the element at `mk` the VALUE of the body that starts at `start`?

    `m_` below is the token count, bound once because two walks need it.

    For a block body the value expression is the one after the nearest `return` before `mk` —
    reached without crossing a `;`, an unmatched `{`, or a line break that ends a statement under
    ASI, so an element in an initializer or an object literal is not it whether or not the source
    writes its semicolons. A `return` whose next token sits on a later line returns nothing (ASI), so the
    element after it is an expression statement and not the value. For a brace-less body the
    value expression is the body. Within that expression every `(` the lexer recorded in
    `calls` opens an argument list, and `[` or `{` opens a literal; an element under any of them
    is passed or held, not returned. A grouping `(` is transparent. `f<T>(` and `f?.(` are calls
    too: the first is read from the angle run here, the second is recorded by the lexer.

    THE CEILING: `return` followed on its own line by a template literal that spans lines reads
    as a bare `return`, because `lits` carries the line a literal ENDED on and the test above
    asks where the value STARTED. Prettier never emits it; the arm pins the verdict (round 6).
    """
    m_ = len(toks)
    if toks[start][0] == "op" and toks[start][1] == "{":
        # BACKWARD, over balanced groups: a `}` that closes an object literal inside the return
        # expression — `return cond ? build({ x }) : <B />` — is stepped over whole, and only an
        # UNMATCHED `{`, a `;`, or an ASI line break at depth zero ends the walk. Closing review
        # round 1: the first cut stopped at any `}` and lost that component, and stopped at no
        # line break and took an earlier statement's `return` in semicolon-free source.
        r = None
        depth = 0
        for j in range(mk - 1, start, -1):
            kind, text, _ln = toks[j]
            # THE ASI RULE, backward, and FIRST — before the bracket bookkeeping, so a closer
            # ending a line at depth zero is a boundary too: `if (!open) return noop()` then
            # `const el = <Modal />` on the next line, and `return []`, `return {}`. Round 2
            # of the closing review found the test nineteen lines below the closer branch that
            # pre-empted it, so it held for `return null` alone. A line break after a token
            # that cannot continue an expression is a statement boundary even with no `;`. A
            # `:`, a `,` or an ELEMENT opening the later line continues the earlier one — the
            # lexer opens an element only after an operator, so a marker at line start means
            # the `?` or `&&` this lexer does not emit sat before it. And a `>` at line end is
            # two things: the close of a generic run under `as`, `satisfies` or `new` (`return
            # v as Foo<Bar>`), a boundary; or a comparison (`return a >` newline `b ? <B /> :
            # null`), a continuation. A line that closed with a silent literal (`lits`) ended
            # whatever token preceded the literal. A token in `conts` opens its line after an operator the lexer
            # consumed silently — `isValid(a) &&` then `isValid(b)` — and continues too; round 3
            # found the closer-first ordering breaking INSIDE that expression, on prettier's own
            # output. `read_ts_expr_end` states the ceiling.
            if depth == 0 and toks[j][2] < toks[j + 1][2] and (j + 1) not in conts \
                    and (lits[j + 1] < toks[j + 1][2] if (j + 1) in lits else
                         (text not in _TS_EXPR_CONTINUES
                          or check_ts_generic_close(toks, j))) \
                    and toks[j + 1][0] != "jsx" and toks[j + 1][1] not in (":", ",", "="):
                break
            if kind == "op" and text in (")", "]", "}"):
                depth += 1
                continue
            if kind == "op" and text in ("(", "[", "{"):
                # An unmatched `{` is the block this statement lives in; an unmatched `(` or
                # `[` is a group the element sits INSIDE — `return (` — and is walked past.
                if depth == 0 and text == "{":
                    break
                if depth:
                    depth -= 1
                continue
            if depth:
                continue
            if kind == "word" and text == "return":
                r = j + 1
                break
            if kind == "op" and text == ";":
                break
        if r is None or toks[r][2] > toks[r - 1][2]:
            return False
    else:
        r = start
    # A CALL WITH TYPE ARGUMENTS — `mount<P>(<C />)` — closes its angle run with a `>` that clears
    # the lexer's `expr_end`, so its `(` is not in `calls`. The token walk can see what the
    # lexer could not: a balanced run after a word, followed by `(`, is an application.
    generic: set = set()
    for j in range(r, mk):
        if toks[j][0] == "op" and toks[j][1] == "<" and j and toks[j - 1][0] == "word":
            e = read_ts_angle_end(toks, j)
            if e is not None and e < m_ and toks[e][0] == "op" and toks[e][1] == "(":
                generic.add(e)
    held: list = []
    for j in range(r, mk):
        kind, text, _ln = toks[j]
        if kind != "op":
            continue
        if text == "(":
            held.append(j in calls or j in generic)
        elif text in ("[", "{"):
            held.append(True)
        elif text in (")", "]", "}") and held:
            held.pop()
    return not any(held)


def read_ts_jsx_defs(src: str) -> list:
    """The `(name, line)` pairs of `parse_tsx_defs(src)[0]` whose value is a JSX element.

    `parse_ts_source`'s header is the rule. Always the `.tsx` lexer: a `.ts` source cannot hold an
    element, and `check_declaration` refuses a `returns:jsx` selector on any extension but one
    read by `tsx-tokens` for that reason.
    """
    funcs, _types, owned = parse_ts_source(src, jsx=True)
    return [funcs[i] for i in sorted(owned)]


def parse_tsx_defs(src: str):
    """`parse_ts_defs` with JSX lexing on — the `.tsx` half of the pair. Its header is that one."""
    return parse_ts_defs(src, jsx=True)


#: The `parser`-mode extractors, keyed by the pattern-set id its `LANGS` row names — the third
#: extractor arm, beside `python-ast` and the `probe` sets. Keyed rather than branched on the
#: extension because `extract_text` is handed source TEXT and a mode, never a path: `drift-audit`
#: calls it against git blobs at two shas and has no file to look at. A `parser` row naming an id
#: that is not here is a REFUSAL in `scan_corpus`, never a silent fallthrough to Python.
#:
#: TWO IDS FOR ONE READER, and not one reader handed the extension: `extract_text` is given source
#: TEXT and a mode and never a path, and the two `.ts`/`.tsx` populations need two different lexer
#: modes — `<T>(x) => x` is a generic arrow in one and an element in the other, so one mode
#: necessarily mis-reads one of them. TOOL-aGradedDialect-3 §4.
PARSERS = {"python-ast": _python_defs, "shell-tokens": parse_shell_defs,
           "ts-tokens": parse_ts_defs, "tsx-tokens": parse_tsx_defs}


def _probe_defs(src: str, pset: str, sets: dict | None = None):
    spec = (sets if sets is not None else PATTERN_SETS)[pset]

    def hits(key):
        out = []
        for rx in spec[key]:
            for m in rx.finditer(src):
                out.append((m.group(1), src.count("\n", 0, m.start()) + 1))
        return out

    return hits("functions"), hits("types"), hits("imports")


def resolve_extractor(mode: str, pset: str, sets: dict | None = None):
    """THE ARMEDNESS PREDICATE: the extractor a `(mode, pattern-set id)` pair reaches, or `None`.

    ONE HOME, because this question is asked at FOUR sites and an earlier revision of the spec named
    only the two that DISPATCH — `extract_text` and the refusal in `scan_corpus`. The other two
    REPORT: the coverage fraction and `--expand`'s armed-extension tally each decided armedness for
    themselves, so a `probe` row whose id names a parser would have been extracted by one half of a
    run and counted UNARMED by the other. The fraction and the extraction disagreeing about the same
    file is two answers to one question inside one run. TOOL-aGradedDialect-3 §8 F1.

    THE PATTERN-SET ID SELECTS THE READER AND THE MODE TOKEN CARRIES ONLY THE STANDING, which is
    what makes a tokenizer-shaped reader reachable under `probe` at all. Before this, `probe`
    reached `PATTERN_SETS` alone, so a reader that MISSED its conformance floor — the honest `probe`
    outcome — had nowhere to run, and the rule that whatever ships declares `parser` or `probe` was
    mechanically false for half of its own vocabulary. A new mode TOKEN was the other shape and the
    engine's own comment refuses it: `LANG_MODE_RANK` reads an unknown mode as absent, so a
    strengthening edit would fire a weakening finding.

    `dark` reaches nothing by declaration, and a `parser` row naming an unshipped id reaches nothing
    by fact; `scan_corpus` tells those two apart in its message and this predicate does not need to.
    """
    if mode not in ("parser", "probe"):
        return None
    if pset in PARSERS:
        return PARSERS[pset]
    if mode == "probe" and pset in (PATTERN_SETS if sets is None else sets):
        return _probe_defs
    return None


def extract_text(src: str, mode: str, pset: str, *, sets: dict | None = None):
    """`(functions, types, imports)` for SOURCE TEXT, or `None` when the mode declares no extractor.

    Split out of `extract` so a caller holding BYTES rather than a path uses the SAME extractor.
    `drift-audit`'s marginal-offense-rate signal derives its two operands from git blobs at two shas
    and never writes a tree; a second implementation there would be the
    `second-implementation-is-not-a-second-opinion` class inside the one instrument whose entire
    value is that both of its operands come from one extractor. TOOL-dScaffoldedMirror-7 S4.

    `sets` IS KEYWORD-ONLY AND DEFAULTS TO THE SHIPPED CONSTANT, which is the whole shape of the
    change TOOL-aSurfacedLexicon-9 was allowed to make here. The positional contract is frozen —
    `drift_report.py` calls both of these positionally against git blobs — so the resolution arrives
    beside it rather than inside it, and an adopter who never passes one is on exactly the previous
    behaviour by the default.
    """
    if mode == "dark":
        return None
    # THE ONE DISPATCH, through the ONE armedness predicate. It is keyed on the pattern-set id
    # rather than branched a second time on `mode`: `parser` already means "a real parse", and
    # which parse is what the set id has always said. TOOL-aSurfacedLexicon-14, widened to reach
    # the same readers under `probe` by TOOL-aGradedDialect-3 §8 F1.
    reader = resolve_extractor(mode, pset, sets)
    if reader is None:
        # UNCHANGED FAILURE SHAPE. `scan_corpus` refuses this pair by name one line before it could
        # ever get here, so reaching this is a direct caller passing a pair no reader answers —
        # which used to raise `KeyError(pset)` out of `PARSERS[pset]` or out of `_probe_defs`, and
        # still does. Returning an empty triple would launder an unshipped id into a clean run.
        raise KeyError(pset)
    if reader is _probe_defs:
        return _probe_defs(src, pset, sets)
    return reader(src)


_IDENT_TOKEN_RE = re.compile(r"[A-Za-z_$][\w$]*")


#: Per-language lexical PROFILE — the sole declaration of the field set (TOOL-aLexedStripper-1 §4,
#: seventh field by TOOL-aLexedStripper-6). Fields, in order:
#:   line_markers             tokens opening a comment that runs to end of line
#:   marker_needs_word_start  whether a marker opens a comment ONLY at line start or after space
#:   block_pair               the block-comment open/close pair, or None
#:   quote_chars              characters opening a single-line string
#:   triple_quoted            whether ''' and \"\"\" open a multi-line string
#:   backtick_is_string       whether a backtick opens a string whose content is NOT code
#:   interpolation_pair       open/close tokens whose BODY is code, or None
#: `marker_needs_word_start` is shell-only: `$#` is the argument count and `${p#/opt/}` is a prefix
#: strip, and treating either as a comment deletes the rest of the line. Backtick is NOT a string in
#: shell, where it opens command substitution and the content IS code. `interpolation_pair` is what
#: lets one rule cover a JS template's `${…}` and a Python f-string's `{…}`; the Python row applies
#: it only inside a string whose prefix carries `f`.
_PROFILE_C = (("//",), False, ("/*", "*/"), ("'", '"'), False, True, ("${", "}"))
_PROFILE_PY = (("#",), False, None, ("'", '"'), True, False, ("{", "}"))
_PROFILE_SH = (("#",), True, None, ("'", '"'), False, False, None)

_LEX_PROFILES = {}
for _e in (".js .jsx .mjs .cjs .ts .tsx .c .h .cc .cpp .hpp .java .go .rs .cs .swift .kt "
           ".scala .php").split():
    _LEX_PROFILES[_e] = _PROFILE_C
for _e in (".py", ".pyi"):
    _LEX_PROFILES[_e] = _PROFILE_PY
for _e in ".sh .bash .zsh .toml .yaml .yml .cfg .ini .conf".split():
    _LEX_PROFILES[_e] = _PROFILE_SH

#: Extensions `_LEX_PROFILES` knows a comment syntax for but which declare no functions. This is the
#: ONLY authored half of the definition-carrying set below — the language half is DERIVED from the
#: profile table, so a language the tokenizer learns is covered the day it is added.
#:
#: A SECOND COPY OF A JUDGEMENT, said plainly. The lexicon kit reaches the same conclusion for its
#: own coverage denominator and argues it at greater length in its engine, outside this block. The
#: two kits import neither each other nor that engine's reading, so the two are independent readings
#: of one question and may diverge; this set is the codebase-map kit's.
_DATA_EXTS = frozenset({".toml", ".yaml", ".yml", ".cfg", ".ini", ".conf"})

#: What the codebase-map kit believes CAN carry a definition. Derived, minus the data formats above.
#:
#: WHAT IT CANNOT SEE: a language `_LEX_PROFILES` has no profile for. `_identifier_tokens` handles
#: one fail-open, by design, and a dark-layer check built on this set therefore MISSES it rather
#: than reporting it — a false negative, chosen over the false positive of calling every unknown
#: extension a source layer.
DEFINITION_CARRYING_EXTS = frozenset(_LEX_PROFILES) - _DATA_EXTS

_TRIPLE_QUOTES = ('"""', "'''")
#: String prefix letters Python allows before a quote. Only `f` (any case) turns the
#: `interpolation_pair` on, but all of them have to be RECOGNISED so `rf"…"` is still seen as
#: f-prefixed and `b"…"` is not.
_PY_PREFIX_CHARS = "rRbBuUfF"


def _identifier_tokens(source: str, suffix: str = "") -> set[str]:
    """Distinct identifier tokens in a source file's CODE, with comments and string CONTENT removed
    by ONE left-to-right pass over the lexical profile for ``suffix``.

    A regex chain cannot express that comments and strings EXCLUDE each other, and whichever it
    strips first wins. The three regexes this replaced applied C syntax to every language, so a
    ``/*`` inside a Python docstring opened a comment running to the next ``*/`` (measured: 674
    lines swallowed, one file down to 18.8% recall against ``tokenize`` ground truth), a ``//``
    truncated a line of floor division, and a ``#`` truncated a line of TypeScript.

    An UNDECLARED suffix strips NOTHING and returns every token. Over-counting is this scan's
    documented fail-open direction — it feeds a RANKING, never a gate — and guessing a
    comment syntax is exactly how the old chain got here.

    A multi-line construct left UNTERMINATED at EOF is ABANDONED, the pass resuming just after the
    opener, so an odd backtick cannot reproduce the same swallow this function exists to remove.
    """
    prof = _LEX_PROFILES.get(suffix)
    if prof is None:
        return set(_IDENT_TOKEN_RE.findall(source))
    markers, word_start, block, quotes, triple, backtick, interp = prof
    out: list[str] = []
    i, n = 0, len(source)

    def _string(start: int, delim: str, multiline: bool, interpolate: bool) -> int:
        """Consume a string opened at ``start`` by ``delim``. Text is blanked; an interpolation body
        is COPIED, because it holds real code. Returns the index just past the close, or past the
        opener when the literal is unterminated (the abandon rule)."""
        j = start + len(delim)
        while j < n:
            if source[j] == "\\":
                j += 2
                continue
            if interpolate and source.startswith(interp[0], j):
                if source.startswith(interp[0] * 2, j) and interp[0] == "{":
                    j += 2  # `{{` is a literal brace and opens nothing
                    continue
                k = j + len(interp[0])
                depth = 0
                body = []
                closed = False
                while k < n:
                    c = source[k]
                    # A brace inside a NESTED STRING is text, not structure. Counting it inflated the
                    # depth so the real closer never matched, and the walk ran on past the literal
                    # consuming comments and string bodies as code -- the over-capture direction of
                    # the same defect this scanner exists to remove. Measured: `{` inside a quoted
                    # argument leaked a following comment's prose into the index.
                    if c in quotes:
                        e = k + 1
                        while e < n and source[e] != c:
                            if source[e] == chr(92):
                                e += 2
                                continue
                            if source[e] == chr(10):
                                break
                            e += 1
                        if e < n and source[e] == c:
                            body.append(" " * (e - k + 1))
                            k = e + 1
                            continue
                    if c == interp[0][-1]:
                        depth += 1
                    elif c == interp[1]:
                        if depth == 0:
                            closed = True
                            break
                        depth -= 1
                    body.append(c)
                    k += 1
                # An interpolation that never closes is TEXT, not code. Emitting the body anyway
                # walked to EOF and leaked the whole rest of the file into the index as identifiers
                # -- the over-capture direction of the same defect this scanner exists to remove.
                out.append(" " + "".join(body) + " " if closed else " ")
                j = k + 1 if closed else k
                continue
            if not multiline and source[j] == "\n":
                return j  # a single-line literal never crosses its line
            if source.startswith(delim, j):
                return j + len(delim)
            j += 1
        return start + len(delim)  # unterminated: abandon, rescan from just after the opener

    while i < n:
        ch = source[i]
        if block and source.startswith(block[0], i):
            j = source.find(block[1], i + len(block[0]))
            i = i + len(block[0]) if j < 0 else j + len(block[1])
            out.append(" ")
            continue
        hit = next((m for m in markers if source.startswith(m, i)), None)
        if hit and (not word_start or i == 0 or source[i - 1].isspace()):
            j = source.find("\n", i)
            i = n if j < 0 else j
            out.append(" ")
            continue
        if ch in quotes or (backtick and ch == "`"):
            # Python string prefixes sit immediately before the quote; `f` (any case) turns on the
            # replacement field. A prefix run is at most a few letters and is already in ``out``.
            # The prefix run is a PYTHON construct, so it is read only for a profile that has
            # them. Running it for the C family cost nothing but said the opposite of what it meant.
            fstring = False
            if triple:
                k = i - 1
                pre = ""
                while k >= 0 and source[k] in _PY_PREFIX_CHARS:
                    pre = source[k] + pre
                    k -= 1
                fstring = "f" in pre.lower()
            if triple and any(source.startswith(d, i) for d in _TRIPLE_QUOTES):
                d = source[i : i + 3]
                i = _string(i, d, True, bool(interp) and fstring)
            elif ch == "`":
                i = _string(i, "`", True, bool(interp))
            else:
                i = _string(i, ch, False, bool(interp) and fstring)
            out.append(" ")
            continue
        out.append(ch)
        i += 1
    return set(_IDENT_TOKEN_RE.findall("".join(out)))


#: The armed set `read_defs_at` reads when its caller names none: the shipped extractors, keyed by
#: the extensions each reads. A caller holding a declaration, the lexicon's
#: `LANGS`, passes its own `armed` in this same `{extension: (pattern-set id, mode)}` shape.
#: It MIRRORS the lexicon's `KNOWN_EXTS` (TOOL-dTotalRecall-43 S15): `js` is the `js-regex` probe, and
#: no extension the lexicon does not know is armed; the lexicon self-test's parity arm holds the two equal.
BUILTIN_ARMED = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe"),
                 "sh": ("shell-tokens", "parser"), "ts": ("ts-tokens", "parser"),
                 "tsx": ("tsx-tokens", "parser")}


def read_state_listing(root, state):
    """`[(blob, path)]` for `state`, `blob` None where the text is read from disk; `None` when git failed.

    `worktree` and `index` list `git ls-files -s -z`, whose rows are `<mode> <blob> <stage>`; a
    gitlink is a commit no extractor reads, and an unmerged path's stages 1 to 3 are no text git would
    commit, so the index reads stage 0 alone and an unmerged path yields no entry (TOOL-dTotalRecall-13
    §8 F4). The worktree reads each tracked path once, whatever its stages. A revision lists
    `git ls-tree -r -z`, whose rows are `<mode> <type> <blob>`, blobs alone.
    """
    tracked = state in ("worktree", "index")
    argv = ["git", "ls-files", "-s", "-z"] if tracked else ["git", "ls-tree", "-r", "-z", state]
    listing = subprocess.run(argv, cwd=root, capture_output=True)
    if listing.returncode != 0:
        return None
    out, seen = [], set()
    for rec in listing.stdout.split(b"\0"):
        meta, _, raw = rec.partition(b"\t")
        bits = meta.split()
        if len(bits) < 3:
            continue
        rel = raw.decode("utf-8", errors="replace")
        if not tracked:
            if bits[1] == b"blob":
                out.append((bits[2].decode("ascii"), rel))
        elif bits[0] == b"160000" or (state == "index" and bits[2] != b"0"):
            continue
        elif state == "index":
            out.append((bits[1].decode("ascii"), rel))
        elif rel not in seen:
            seen.add(rel)
            out.append((None, rel))
    return out


def read_blob_batch(root, blobs):
    """`{blob: bytes}` from ONE `git cat-file --batch`; `None` when git failed or a header is no blob's."""
    if not blobs:
        return {}
    batch = subprocess.run(["git", "cat-file", "--batch"], cwd=root, capture_output=True,
                           input="".join(blob + "\n" for blob in blobs).encode("ascii"))
    if batch.returncode != 0:
        return None
    out, buf, i = {}, batch.stdout, 0
    for blob in blobs:
        nl = buf.find(b"\n", i)
        header = buf[i:nl].split() if nl >= 0 else []
        if len(header) < 3 or not header[2].isdigit():
            return None
        size = int(header[2])
        out[blob] = buf[nl + 1: nl + 1 + size]
        i = nl + 1 + size + 1
    return out


def read_worktree_blobs(root, rels):
    """`{path: blob id}` for tracked working-tree paths present on disk, from ONE `git hash-object
    --stdin-paths` spawn, so each id is the one `git hash-object <path>` prints: the clean filters and
    `core.autocrlf` applied, a symlink hashed as its link text. `None` when git failed."""
    if not rels:
        return {}
    got = subprocess.run(["git", "hash-object", "--stdin-paths"], cwd=root, capture_output=True,
                         input="".join(rel + "\n" for rel in rels).encode("utf-8"))
    ids = got.stdout.decode("ascii", errors="replace").split()
    if got.returncode != 0 or len(ids) != len(rels):
        return None
    return dict(zip(rels, ids))


def read_defs_at(root, state, paths=None, cache=None, *, armed=None, sets=None, missing=None):
    """`{path: (blob, (functions, types, imports))}` for every path whose extension `armed` maps, read
    from `state`: `worktree`, each tracked file's bytes on disk; `index`, the staging index's stage-0
    entries; anything else, a revision. Restricted to `paths` when given. `None` when a git call
    failed, which is not an empty tree. TOOL-dTotalRecall-13 S2, generalising the lexicon's
    `read_defs_at_sha`.

    AT MOST TWO SPAWNS PER READ: one listing and one `git cat-file --batch` over the blobs not in
    `cache`, because on Windows a per-file read is spawn-bound. The worktree spawns no batch: its
    blob ids come from ONE `git hash-object --stdin-paths` (`read_worktree_blobs`, TOOL-dTotalRecall-43
    S36), git's own id of the path with its filters and `core.autocrlf` applied, so a blob unchanged
    since the index or a revision shares their cache entry, and its text is the bytes on disk, a
    symlink's (mode `120000`) its link text. A tracked path absent from disk yields no worktree entry
    and is appended to `missing` where the caller passes a list.

    `armed` maps an extension to `(pattern-set id, mode)` and defaults to `BUILTIN_ARMED`; `sets` is
    `extract_text`'s. `cache` maps `(blob, extension)` to the triple, so a blob shared by two states
    or two revisions is parsed once. A blob whose extractor raises `SyntaxError`, `ValueError` or
    `KeyError`, or that `extract_text` answers `None` for, maps to the EMPTY triple rather than
    dropping its path: a caller comparing two states reads an unparseable file as one that lost what
    it held, and says so.
    """
    armed = BUILTIN_ARMED if armed is None else armed
    cache = {} if cache is None else cache
    listing = read_state_listing(root, state)
    if listing is None:
        return None
    want, disk, loose = [], {}, {}
    for blob, rel in listing:
        ext = ext_of(rel)
        if ext not in armed or (paths is not None and rel not in paths):
            continue
        if blob is None:
            full = f"{root}/{rel}"
            try:
                if os.path.islink(full):
                    data = os.fsencode(os.readlink(full))
                else:
                    with open(full, "rb") as fh:
                        data = fh.read()
            except OSError:
                if missing is not None:
                    missing.append(rel)
                continue
            loose[rel] = data
            continue
        want.append(((blob, ext), rel))
    ids = read_worktree_blobs(root, list(loose))
    if ids is None:
        return None
    for rel, data in loose.items():
        disk[ids[rel]] = data
        want.append(((ids[rel], ext_of(rel)), rel))
    todo = sorted({key for key, _ in want if key not in cache})
    texts = read_blob_batch(root, sorted({blob for blob, _ext in todo if blob not in disk}))
    if texts is None:
        return None
    texts.update(disk)
    for key in todo:
        pset, mode = armed[key[1]]
        try:
            got = extract_text(texts[key[0]].decode("utf-8", errors="replace"), mode, pset, sets=sets)
        except (SyntaxError, ValueError, KeyError):
            got = None
        cache[key] = got if got else ([], [], [])
    return {rel: (key[0], cache[key]) for key, rel in want}


# ---- TOOL-dTotalRecall-8: definitions with their ranges, and the call sites inside them --------

#: A shell file another sources: the last `*.sh` name of a `.` or `source` command's first argument.
_SH_SOURCE = re.compile(r"^[ \t]*(?:\.|source)[ \t]+[^\n;|&]*?([\w.-]+\.sh)\b", re.M)


def derive_range_hash(lines: list, line: int, end_line: int) -> str:
    """The first 12 hex of the SHA-1 of source lines `line` to `end_line`, one-based and inclusive."""
    text = "\n".join(lines[line - 1:end_line]) + "\n"
    return hashlib.sha1(text.encode("utf-8", "surrogatepass")).hexdigest()[:12]


def extract_ranges(src: str, ext: str):
    """What one blob's text defines and calls, or `None` for an extension with no range reader here. A dict:

    `defs`     `[(qualified name, "function" or "class", line, end_line, body hash)]` in source order, a nested
               definition's name joining its parents with `.`, the hash `derive_range_hash`'s over the range;
    `calls`    `[(the enclosing definition's qualified name or "", callee as spelled, line)]`;
    `imports`  `[(local name, module, imported name)]`, a shell file's the files it sources;
    `bases`    `{class: [base as spelled]}`, and `assigns` `[(scope, name, callee)]`, a name assigned from a
               call, both what resolving a Python method needs;
    `argv`     the list and tuple literals of a Python file holding a string, each member its string, or
               `$<dotted name>` for a name, or `$` for another expression.

    Python is `ast`; shell and JavaScript (and `ts`, `tsx`) are the tokenizers above, a range running from the
    name's line to the line its body closes on. A site is every call's spelled name (Python), every word
    that could name a function (shell) and every applied name (JavaScript): which definition one reaches is
    the caller's to resolve, over a tree. RAISES what `ast.parse` or the tokenizer raises.
    """
    src = src.removeprefix("\ufeff").replace("\r\n", "\n")
    if ext == "py":
        return _read_py_ranges(src.replace("\r", "\n"))
    if ext == "sh":
        return _read_sh_ranges(src)
    if ext in ("js", "mjs", "cjs", "ts", "tsx"):
        return _read_ts_ranges(src, ext == "tsx")
    return None


def _read_py_ranges(src: str) -> dict:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # a string escape's warning is the file's, never this reader's
        tree = ast.parse(src)
    lines = src.split("\n")
    out = {"defs": [], "calls": [], "imports": [], "bases": {}, "assigns": [], "argv": []}

    def read_dotted(node):
        parts = []
        while isinstance(node, ast.Attribute):
            parts.append(node.attr)
            node = node.value
        if isinstance(node, ast.Name):
            return ".".join([node.id, *reversed(parts)])
        return ".".join(["?", *reversed(parts)]) if parts else None

    def scan_node(node, scope):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            name = f"{scope}.{node.name}" if scope else node.name
            is_class = isinstance(node, ast.ClassDef)
            out["defs"].append((name, "class" if is_class else "function", node.lineno, node.end_lineno,
                                derive_range_hash(lines, node.lineno, node.end_lineno)))
            if is_class:
                out["bases"].setdefault(name, [b for b in map(read_dotted, node.bases) if b])
            for deco in node.decorator_list:  # evaluated where the definition stands, outside its own range
                scan_node(deco, scope)
            for child in ast.iter_child_nodes(node):
                if child not in node.decorator_list:
                    scan_node(child, name)
            return
        if isinstance(node, ast.Call):
            callee = read_dotted(node.func)
            if callee:
                out["calls"].append((scope, callee, node.lineno))
        elif isinstance(node, ast.Import):
            for a in node.names:
                top = a.name if a.asname else a.name.split(".")[0]
                out["imports"].append((a.asname or top, top, ""))
        elif isinstance(node, ast.ImportFrom):
            for a in node.names:
                out["imports"].append((a.asname or a.name, "." * node.level + (node.module or ""), a.name))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and isinstance(node.value, ast.Call):
            callee = read_dotted(node.value.func)
            if callee:
                out["assigns"].append((scope, node.targets[0].id, callee))
        elif isinstance(node, (ast.List, ast.Tuple)):
            words = [e.value if isinstance(e, ast.Constant) and isinstance(e.value, str)
                     else "$" + (read_dotted(e) or "") for e in node.elts]
            if any(not w.startswith("$") for w in words):
                out["argv"].append(words)
        for child in ast.iter_child_nodes(node):
            scan_node(child, scope)

    scan_node(tree, "")
    return out


def _scan_owned(spans: list, sites: list, lines: list) -> tuple:
    """`(defs, calls)` from `spans`, `[(name, kind, line, end_line, first index, last index)]` in token order,
    and `sites`, `[(index, name, line)]` in token order: each name qualified by the spans holding it, each
    site given the innermost span holding it. One pass over both, a stack of the spans still open."""
    defs, calls, opened, at = [], [], [], 0
    for i, name, line in [*sites, (float("inf"), "", 0)]:
        while at < len(spans) and spans[at][4] <= i:
            own, kind, first, last, begin, close = spans[at]
            while opened and opened[-1][1] < begin:
                opened.pop()
            qual = f"{opened[-1][0]}.{own}" if opened else own
            defs.append((qual, kind, first, last, derive_range_hash(lines, first, last)))
            opened.append((qual, close))
            at += 1
        while opened and opened[-1][1] < i:
            opened.pop()
        if name:
            calls.append((opened[-1][0] if opened else "", name, line))
    return defs, calls


def _read_sh_ranges(src: str) -> dict:
    toks = scan_shell_tokens(src)
    spans, named = [], set()
    for name, line, name_at, body in read_shell_sites(toks):
        named.add(name_at)
        opener, closer = toks[body][1], "}" if toks[body][1] == "{" else ")"
        depth, end = 0, body
        while end < len(toks):
            if toks[end][0] == "op":
                depth += (toks[end][1] == opener) - (toks[end][1] == closer)
                if not depth:
                    break
            end += 1
        end = min(end, len(toks) - 1)
        spans.append((name, "function", line, max(line, toks[end][2]), name_at, end))
    sites = [(i, text, ln) for i, (kind, text, ln) in enumerate(toks)
             if kind == "word" and i not in named and _SH_NAME.match(text)]
    defs, calls = _scan_owned(spans, sites, src.split("\n"))
    return {"defs": defs, "calls": calls, "imports": [(m, m, "") for m in _SH_SOURCE.findall(src)],
            "bases": {}, "assigns": [], "argv": []}


def _read_ts_ranges(src: str, jsx: bool) -> dict:
    applied, conts, lits = set(), set(), {}
    toks = scan_ts_tokens(src, jsx, applied, conts, lits)
    funcs, types_, _owned = parse_ts_source(src, jsx)
    want, classes = collections.Counter(funcs + types_), set(types_)
    spans, m = [], len(toks)
    for i, (kind, text, ln) in enumerate(toks):
        if kind != "word" or not want.get((text, ln)):
            continue
        want[(text, ln)] -= 1
        if (text, ln) in classes:
            body = next((j for j in range(i, m) if toks[j][1] in ("{", ";")), None)
        else:
            j = i + 1
            if j < m and toks[j][1] == "<":
                j = read_ts_angle_end(toks, j) or j
            if j < m and toks[j][1] == "(":
                body = read_ts_body_start(toks, j)
            else:
                eq = j if check_ts_arrow(toks, j + 1) else read_ts_type_end(toks, j + 1, "=")
                if eq is not None and eq + 1 in lits:  # its value was a silent literal, and the arrow the walk
                    continue                           # above read is the NEXT statement's: no definition here
                body = read_ts_arrow_body(toks, eq + 1) if eq is not None else None
        if body is None or body >= m:
            end = i + 1
        elif toks[body][1] == "{":
            end = read_ts_brace_end(toks, body)
        else:
            end = max(read_ts_expr_end(toks, body, conts, lits), i + 1)
        spans.append((text, "class" if (text, ln) in classes else "function", ln,
                      max(ln, toks[min(end, m) - 1][2]), i, end - 1))
    starts = {s[4] for s in spans}
    sites = [(i - 1, toks[i - 1][1], toks[i - 1][2]) for i in sorted(applied)
             if i and i - 1 not in starts and toks[i - 1][0] == "word" and _TS_NAME.match(toks[i - 1][1])]
    defs, calls = _scan_owned(spans, sites, src.split("\n"))
    return {"defs": defs, "calls": calls, "bases": {}, "assigns": [], "argv": [],
            "imports": [(mod, mod, "") for mod, _line in _probe_defs(src, "js-regex")[2]]}
# <<< extract_code

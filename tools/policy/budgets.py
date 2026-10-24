"""budgets.py - the policy reader's half for size caps (TOOL-dGroundRules-9): the cap census, one
answer per cap, and the verdict a breach takes.

    python <this kit>/budgets.py resolve <cap>[=legacy:<n>|=default:<n>] ...    # one row per cap
    python <this kit>/budgets.py check <cap>[=legacy:<n>|=default:<n>] <measured>  # the verdict

THE CENSUS, `caps.toml` beside this file, is one `[[cap]]` row per size cap: its name under
`budgets.*`, its class, its unit, its enforcer, its legacy home and whether it is a family. A `switch`
cap obeys the switch; a `consumer`, `correctness` or `exempt` cap sits outside it, and this module
refuses to answer one, so its enforcer cannot read a mode it must not obey.

THE ANSWER. `resolve_caps` reads the policy file ONCE, through `policy.read_revision` at the
revision `rev` names, else the landed one, and `policy.resolve_read` for `budgets.enforce`,
`budgets.pinned` and each requested `budgets.<cap>`. A cap's value is the file's when the file sets
one, else its legacy home's. A `limits:` home is a row of the template-size limits file at this
kit's tool root, read by this module alone, from the same revision and never from the working tree
(§8 F5 of the spec). Every other home is read by the enforcer and handed in as `legacy:<n>`; a
`default:<n>` handed in is a code constant and not a home, so a file value overrides it. A cap whose
value sits in both homes refuses. The mode is `refuse` where `budgets.pinned` names the cap or
`budgets.enforce` resolves `refuse`, else `warn`; a family cap answers its mode and the value handed
in, if any. A request naming no census row is answered only where it hands in a `default:`: the
template-size gate's subject with no declared row keeps that gate's default, under the switch.

`check_budgets` is the schema rule `policy.validate` calls for the `[budgets]` table: a pinned name
outside the switch or naming no census row, and a `budgets.<cap>` naming no row, set on a family cap
or not a positive integer, each a Problem on its line.

Exit 0 under or warned, 1 refused, 2 a refusal, printed as `policy: refused · <path>:<line> · <why>`.
"""
import posixpath
import re
import sys
import tomllib
from collections import namedtuple
from pathlib import Path

import policy  # the module beside this file

KIT = Path(__file__).resolve().parent
CENSUS = "caps.toml"
LIMITS_NAME = "template-size-limits.txt"
CLASSES = ("switch", "consumer", "correctness", "exempt")
OUTSIDE = ("consumer", "correctness", "exempt")
UNITS = ("bytes", "lines", "chars", "count")
HOME_FORMS = ("limits", "file", "conf", "constant")
FIELDS = ("name", "class", "unit", "enforcer", "home", "family", "research")
# The two exact rows under `budgets` a cap name may never shadow.
RESERVED = ("enforce", "pinned")
REQUEST = re.compile(r"(?P<cap>[^=]+)(?:=(?P<how>legacy|default):(?P<n>[0-9]+))?")
SHELL_KEY = r"^\s*(?:export\s+)?{}\s*="

Cap = namedtuple("Cap", "name cls unit enforcer home family research line")
CapAnswer = namedtuple("CapAnswer", "value mode source reason cap unit rule")
CapVerdict = namedtuple("CapVerdict", "over refuse line")


# The {prefix} token, INLINED byte-identically from the canonical copy named on its marker line and
# gated by the resolve-python self-test: a kit may not import a sibling.
# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token


def derive_kit_rel():
    """This kit's directory as a path from the top of its repository with a trailing `/`, git's own
    spelling, or None where the kit is in no repository."""
    prefix = policy.run_git(KIT, "rev-parse", "--show-prefix")
    return None if prefix is None else prefix.strip()


def derive_tool_root():
    """The tool root this kit sits in, repo-relative, "" at a root install or outside a repository."""
    rel = derive_kit_rel()
    return posixpath.dirname(rel.rstrip("/")) if rel else ""


def derive_census_rel():
    """The census as a refusal names it: repo-relative, or this kit's own path outside a repository."""
    rel = derive_kit_rel()
    return (KIT / CENSUS).as_posix() if rel is None else rel + CENSUS


def read_cap_census(repo="."):
    """{name: Cap} for the census `repo` holds at this kit's own path, else this kit's own, in file
    order. A census that does not parse, a row lacking a field or carrying an unknown one, a class,
    unit or home form outside its set, a reserved name, or a name twice is a Refusal naming the
    census and the row's line."""
    rel = derive_kit_rel()
    path = Path(repo, rel, CENSUS) if rel is not None and Path(repo, rel, CENSUS).is_file() else KIT / CENSUS
    shown = derive_census_rel()
    try:
        text = path.read_text(encoding="utf-8")
        doc = tomllib.loads(text)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise policy.Refusal(shown, 0, f"the cap census does not read: {exc}") from None
    heads = [n for n, ln in enumerate(text.splitlines(), 1) if ln.strip() == "[[cap]]"]
    out = {}
    for i, row in enumerate(doc.get("cap", [])):
        line = heads[i] if i < len(heads) else 0
        missing = [f for f in FIELDS if f not in row]
        unknown = [f for f in row if f not in FIELDS]
        why = (f"lacks {', '.join(missing)}" if missing else f"carries the unknown field {unknown[0]}" if unknown
               else f"class {row['class']!r} is none of {', '.join(CLASSES)}" if row["class"] not in CLASSES
               else f"unit {row['unit']!r} is none of {', '.join(UNITS)}" if row["unit"] not in UNITS
               else f"home {row['home']!r} opens with none of {', '.join(HOME_FORMS)}"
               if str(row["home"]).partition(":")[0] not in HOME_FORMS
               else f"family {row['family']!r} is not a boolean" if not isinstance(row["family"], bool)
               else f"{row['name']} shadows budgets.{row['name']}" if row["name"] in RESERVED
               else f"{row['name']} is a census row twice" if row["name"] in out else None)
        if why:
            raise policy.Refusal(shown, line, why)
        out[row["name"]] = Cap(row["name"], row["class"], row["unit"], row["enforcer"], row["home"],
                               row["family"], row["research"], line)
    return out


def parse_request(req):
    """(cap, how, n) for one request in the CLI's grammar, `<cap>[=legacy:<n>|=default:<n>]`; how and
    n are None where nothing is handed in. Anything else is a Refusal."""
    m = REQUEST.fullmatch(req)
    if not m:
        raise policy.Refusal(derive_census_rel(), 0, f"{req!r} is not <cap>[=legacy:<n>|=default:<n>]")
    return m["cap"], m["how"], int(m["n"]) if m["n"] else None


def derive_limits_rel():
    """The limits file's path from the top of the repository, at this kit's tool root."""
    root = derive_tool_root()
    return f"{root}/{LIMITS_NAME}" if root else LIMITS_NAME


def parse_limits_rows(text):
    """{row key: (value text, line)} of the limits file's text: tab-separated rows, comment and blank
    lines skipped, the value stripped of whitespace, as the template-size gate parsed it, the first
    row of a key kept. The file's ONE parser: every reader of its rows comes through here."""
    rows = {}
    for n, line in enumerate((text or "").replace("\r", "").split("\n"), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _tab, val = line.partition("\t")
        rows.setdefault(key, ("".join(val.split()), n))
    return rows


def read_limits_home(repo, sha):
    """(the limits file's repo-relative path, its rows by `parse_limits_rows`) in the commit `sha`
    names. An absent file has no rows."""
    rel = derive_limits_rel()
    return rel, parse_limits_rows(policy.run_git(repo, "show", f"{sha}:{rel}"))


def derive_home_line(repo, home):
    """(path, line) of a `file:`, `conf:` or `constant:` home as the working tree spells it: the line
    assigning its key or opening with its row key, 0 where none does or the key is a placeholder."""
    _form, _c, rest = home.partition(":")
    path, _c, key = rest.rpartition(":")
    path = resolve_prefix_token(path, derive_tool_root())
    try:
        lines = Path(repo, path).read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return path, 0
    rx = re.compile(SHELL_KEY.format(re.escape(key)) + "|" + re.escape(key) + r"\t")
    return path, next((n for n, ln in enumerate(lines, 1) if not key.startswith("<") and rx.match(ln)), 0)


def resolve_caps(requests, repo=".", rev=None):
    """{cap: CapAnswer} for each request in the CLI's grammar, over ONE read of the policy file at the
    revision `rev` names, else the landed one. The value is the file's `budgets.<cap>` when it sets
    one, else the legacy home's, else the `default:` handed in; the source is the reader's for a file
    value, `default` for a legacy home's (the catalogue's derived default is that home), and
    `constant` for the enforcer's own handed-in default, which no declaration holds. A cap nothing
    gives a value answers None, source `none`: unchecked, as a 0 is. Refused: a request naming no
    census row with no `default:`, a cap outside the switch, a `legacy:` handed for a `limits:` home,
    a limits row that is not a number, a cap held in both homes, and every refusal the reader makes."""
    census = read_cap_census(repo)
    rows = policy.load_catalogue(policy.KIT)
    read = policy.read_revision(repo, rev, rows)

    # Each read spells its key as a string, the shape the reader-coverage arm reads as a reader.
    def read_key(key):
        path = policy.parse_key(key)
        return policy.resolve_read(path, policy.read_catalogue_row(path, rows), read)
    enforce, pinned = read_key("budgets.enforce"), read_key("budgets.pinned")
    pins = pinned.value if isinstance(pinned.value, list) else []
    limits = None
    out = {}
    for req in requests:
        name, how, n = parse_request(req)
        cap = census.get(name)
        if name in pins:
            mode, rule = "refuse", "budgets.pinned names it"
        else:
            mode, rule = ("refuse" if enforce.value == "refuse" else "warn"), f"budgets.enforce is {enforce.value}"
        if cap is None:
            if how != "default":
                raise policy.Refusal(derive_census_rel(), 0, f"{name} names no row of the cap census, and no default was handed in")
            out[name] = CapAnswer(n, mode, "constant", f"{name} names no census row; the enforcer's default {n}",
                                  name, "bytes", rule)
            continue
        if cap.cls in OUTSIDE:
            raise policy.Refusal(derive_census_rel(), cap.line, f"{name} is {cap.cls}, outside the switch; its enforcer reads no mode")
        form, _c, key = cap.home.partition(":")
        if cap.family:
            out[name] = CapAnswer(n, mode, "default", f"a family cap: the value is per subject, {cap.home}",
                                  name, cap.unit, rule)
            continue
        seg = policy.render_json(name)  # one quoted segment, whatever `/`, `.` or `*` the name carries
        hit = read_key(f"budgets.{seg}")
        # An unset key resolves to the row's derived default, a table: that is "no file value".
        held = None if isinstance(hit.value, dict) else hit.value
        legacy = None
        if form == "limits":
            if how == "legacy":
                raise policy.Refusal(derive_census_rel(), cap.line, f"{name}'s home is the limits file, which budgets.py reads alone")
            if limits is None:
                limits = read_limits_home(repo, read["sha"])
            lrel, lrows = limits
            if key in lrows:
                val, line = lrows[key]
                if not val.isdigit():
                    raise policy.Refusal(lrel, line, f"budgets.{name}'s row is not a number: {val!r}")
                legacy = (int(val), lrel, line)
        elif how == "legacy":
            legacy = (n, *derive_home_line(repo, cap.home))
        if held is not None and legacy is not None:
            raise policy.Refusal(legacy[1], legacy[2], f"budgets.{name} is held in both homes")
        if held is not None:
            out[name] = CapAnswer(held, mode, hit.source, hit.reason, name, cap.unit, rule)
        elif legacy is not None:
            out[name] = CapAnswer(legacy[0], mode, "default", f"not set in {policy.POLICY_REL}; its legacy home "
                                  f"{legacy[1]}:{legacy[2]} holds {legacy[0]}", name, cap.unit, rule)
        elif how == "default":
            out[name] = CapAnswer(n, mode, "constant", f"not set in {policy.POLICY_REL}; the enforcer's constant {n}",
                                  name, cap.unit, rule)
        else:  # nothing declares a value: unchecked, as a 0 is, and said in the reason
            out[name] = CapAnswer(None, mode, "none", f"budgets.{name} has no value: {policy.POLICY_REL} does not set "
                                  f"it and its home {cap.home} holds none", name, cap.unit, rule)
    return out


def check_cap(answer, measured, subject=None):
    """CapVerdict(over, refuse, line) for `measured` against `answer`. A value of 0, or none, is
    unchecked, as every enforcer reads it. A breach refuses under `refuse` and warns otherwise; the
    line names the subject, `answer.cap` where none is given, and the rule that set the mode."""
    subject = subject or answer.cap
    if not answer.value:
        return CapVerdict(False, False, f"BUDGET OK — {answer.cap} · {subject} · {measured} {answer.unit}, unchecked")
    if measured <= answer.value:
        return CapVerdict(False, False, f"BUDGET OK — {answer.cap} · {subject} · {measured} {answer.unit} of {answer.value}")
    word = "REFUSE" if answer.mode == "refuse" else "WARN"
    return CapVerdict(True, answer.mode == "refuse", f"BUDGET {word} — {answer.cap} · {subject} · {measured} "
                      f"{answer.unit} over {answer.value} · {answer.rule}")


def check_budgets(doc, text="", census=None):
    """[Problem] for the `[budgets]` table of a parsed policy file, each at the line of `text` that
    `policy.derive_key_line` finds: a `budgets.pinned` name of a class outside the switch or naming no
    census row, and a `budgets.<cap>` naming no census row, set on a family cap, or not a positive
    integer. The census is `read_cap_census`'s for the working directory unless `census` names one,
    and is read only when the table pins or sets something."""
    table = doc.get("budgets")
    if not isinstance(table, dict):
        return []
    pins = table.get("pinned") if isinstance(table.get("pinned"), list) else []
    caps = {k: v for k, v in table.items() if k not in RESERVED and not isinstance(v, dict)}
    if not pins and not caps:
        return []
    census = read_cap_census() if census is None else census
    out = []
    at = policy.derive_key_line(text, ("budgets", "pinned"))
    for name in pins:
        row = census.get(name)
        if row is None:
            out.append(policy.Problem(at, "budgets.pinned", f"{name} names no row of the cap census"))
        elif row.cls in OUTSIDE:
            out.append(policy.Problem(at, "budgets.pinned", f"{name} is {row.cls}, outside the switch, so no pin reaches it"))
    for name, value in caps.items():
        key = policy.render_dotted(("budgets", name))
        line = policy.derive_key_line(text, ("budgets", name))
        row = census.get(name)
        if row is None:
            out.append(policy.Problem(line, key, f"{name} names no row of the cap census"))
        elif row.family:
            out.append(policy.Problem(line, key, f"{name} is a family cap: its enforcer asks only its mode, "
                                      "and the policy file may not set its value"))
        elif isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            out.append(policy.Problem(line, key, f"{name} is {policy.render_json(value)}, not a positive integer"))
    return out


USAGE = ("usage: python budgets.py resolve [--explain] <cap>[=legacy:<n>|=default:<n>] ... "
         "| check <cap>[=legacy:<n>|=default:<n>] <measured>")


def main(argv):
    """`resolve`: one `<cap>\\t<value>\\t<mode>\\t<source>` row per request, `-` for an absent
    value; under `--explain`, one `budgets: <cap> · <rule> · <reason>` line per cap on stderr, the
    rule that set the mode, which a shell enforcer names on its breach line. `check`: the verdict
    line, exit 1 when it refuses. Run in the repository to read."""
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    verb, args = (argv[0], argv[1:]) if argv else ("", [])
    explain = verb == "resolve" and args[:1] == ["--explain"]
    args = args[1:] if explain else args
    if verb == "check" and len(args) == 2 and args[1].isdigit():
        reqs, measured = args[:1], int(args[1])
    elif verb == "resolve" and args:
        reqs, measured = args, None
    else:
        print(USAGE, file=sys.stderr)
        return 2
    try:
        answers = resolve_caps(reqs, ".")
    except policy.Refusal as exc:
        print(exc, file=sys.stderr)
        return 2
    if measured is None:
        for a in answers.values():
            print(f"{a.cap}\t{'-' if a.value is None else a.value}\t{a.mode}\t{a.source}")
            if explain:
                print(f"budgets: {a.cap} · {a.rule} · {a.reason}", file=sys.stderr)
        return 0
    verdict = check_cap(next(iter(answers.values())), measured)
    print(verdict.line)
    return 1 if verdict.refuse else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

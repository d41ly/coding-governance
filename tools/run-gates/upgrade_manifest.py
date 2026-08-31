"""upgrade_manifest.py — an adopter JSON leg manifest -> gate-legs.toml.

Driven by `adopt-run-gates.sh --upgrade`; not meant to be run by hand. A FILE rather than a block
inlined into that script, for the reason `profile_bar.py` is one: two hundred lines of Python inside
a single-quoted shell string cannot carry an apostrophe, and a converter whose comments have to be
written around a quoting rule is a converter nobody will edit.

argv: <source.json> <gate-profiles.txt> <out.toml> <dry:0|1> <force:0|1> <target-root>
"""
import json, os, sys
# adopt-run-gates.sh --upgrade — convert an adopter's JSON leg manifest into gate-legs.toml.
# TOOL-aGatheredDeclaration-7. Every rule here is the spec's; the comments say WHY, not what.

SRC, PROF, OUT, DRY, FORCE = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] == "1", sys.argv[5] == "1"
TARGET = sys.argv[6]

# THE MAPPING IS A TABLE, not a chain of conditionals, so an unmapped key is a LOOKUP MISS that
# refuses rather than a branch nobody wrote. That is what makes a third dialect fail loudly instead
# of silently losing a field.
MAP = {
    "name": "name", "argv": "argv", "cwd": "cwd", "ceiling": "ceiling",
    "guard": "guard", "chunk": "chunk", "impure": "impure", "tool": "tool",
    "full_only": "full_only",
    "subject": "!hold", "optIn": "!hold",      # both spell the hold; resolved together below
    "phase": "lane",
}
# Ruled DROP: reported, and the leg is still emitted. `scope` is an adopter's tier enum resolved
# through a second file, so guessing a guard path list from it would produce guards that silently
# scope legs OUT — worse than not carrying it. `pg_autowire` is product-specific provisioning.
DROP = {"scope": "an adopter tier enum resolved through a second file; assign `guard` path lists by hand",
        "pg_autowire": "product-specific container provisioning; declare it in the leg's own argv"}

notes, dropped = [], {}


def die(msg):
    sys.stderr.write("adopt-run-gates --upgrade: %s\n" % msg)
    sys.exit(2)


def s(v):
    if any(ord(c) < 0x20 for c in v):
        die("a value carries a control byte and cannot be written as TOML: %r" % v)
    return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'


def arr(xs):
    return "[" + ", ".join(s(str(x)) for x in xs) + "]"


def wrap(text, lead="# ", width=96):
    out, line = [], lead
    for w in str(text).split():
        if len(line) + len(w) + 1 > width and line != lead:
            out.append(line.rstrip()); line = lead + w
        else:
            line = line + w if line == lead else line + " " + w
    if line != lead:
        out.append(line.rstrip())
    return "\n".join(out) if out else lead.rstrip()


# ---- dialect detection, on the parsed value's TYPE ---------------------------------------------
# Not on the filename: both observed adopters call the file gate-legs.json and the shapes differ.
try:
    doc = json.load(open(SRC, encoding="utf-8"))
except Exception as e:
    die("%s does not parse as JSON: %s" % (SRC, e))

if isinstance(doc, list):
    legs, extra, dialect = doc, {}, "A (bare array)"
elif isinstance(doc, dict) and isinstance(doc.get("legs"), list):
    legs = doc["legs"]
    extra = {k: v for k, v in doc.items() if k != "legs"}
    dialect = "B (object with a `legs` key)"
else:
    die("%s is neither a JSON array of legs nor an object carrying a `legs` array — this converter "
        "handles the two dialects it has observed and refuses a third rather than guessing" % SRC)

if not legs:
    die("%s declares no legs; refusing to write an empty manifest" % SRC)

# ---- the profile table: REQUIRED, because the TOML wins wholesale --------------------------------
# TOML absent -> the runner reads the legacy PAIR; TOML present -> it wins, and a manifest with no
# [[profile]] row drops the target to the built-in formula without saying so. Refuse instead.
profiles = []
if os.path.exists(PROF):
    pend = []
    for raw in open(PROF, encoding="utf-8").read().splitlines():
        if raw.startswith("#"):
            pend.append(raw); continue
        if not raw.strip():
            continue
        f = raw.split("\t")
        if len(f) < 4:
            die("%s carries a malformed row: %r" % (PROF, raw))
        knobs = dict(kv.split("=", 1) for kv in f[3].split(",") if "=" in kv)
        profiles.append((f[0], f[1], f[2], knobs, pend)); pend = []
if not profiles:
    die("%s has no readable profile table, and a gate-legs.toml with no [[profile]] row silently "
        "drops this target to the runner's built-in width formula. Keep the table, or declare the "
        "rows by hand after this converts the legs." % PROF)

L = []
A = L.append
A("# gate-legs.toml — the merge bar, DECLARED. One file: defaults, profiles, lanes, legs.")
A("#")
A(wrap("Converted from %s (dialect %s) by adopt-run-gates.sh --upgrade. AUTHORED from here on: this "
       "converter runs once. Needs CPython 3.11+ to be read at all; below that the runner reads the "
       "legacy pair and says so." % (os.path.basename(SRC), dialect)))
# S4: the prose the source could only carry as data becomes COMMENTS. Losing it is the defect this
# whole format exists to fix, so a converter that dropped it would be the joke telling itself.
if extra.get("_doc"):
    A("#"); A(wrap(str(extra["_doc"])))
A("")
A("[bar]")
A(wrap("OWNER OPT-IN, shipped false. A ceiling KILLS a leg before it can answer, so enforcement OFF "
       "produces strictly more evidence than a ceiling that fired. GATE_CEILINGS=0|1 overrides."))
A("enforce_ceilings = false")
pol = extra.get("ceiling_policy")
A("default_ceiling = %d" % (pol if isinstance(pol, int) and pol > 0 else 1800))
A(wrap("OWNER OPT-IN, shipped false. The turnstile serialises one bar per repository and therefore "
       "enqueues parallel pushes behind each other. GATE_TURNSTILE=1 turns it on."))
A("turnstile = false")
A("turnstile_ttl = 1800")

A(""); A("# " + "-" * 96)
for nm, c, r, knobs, cmts in profiles:
    for x in cmts:
        A(x)
    A("[[profile]]"); A("name = %s" % s(nm)); A("min_cores = %s" % int(c))
    A("min_ram_mb = %s" % int(r)); A("width = %s" % int(knobs.get("width", 1))); A("")

# ---- lanes: emitted from the lane values the legs actually map to ------------------------------
# A leg naming a lane no [[lane]] row declares is a manifest the runner REFUSES, so emitting legs
# alone would write a file the target cannot read. Order is preserved: lanes run in declaration
# order and `fast` before `heavy` before `serial` is the adopter's own sequence.
ORDER = ["fast", "heavy", "serial"]
lanes = []
for lg in legs:
    ln = lg.get("phase") or "heavy"
    if ln not in lanes:
        lanes.append(ln)
lanes.sort(key=lambda x: (ORDER.index(x) if x in ORDER else len(ORDER), x))
A("# " + "-" * 96)
A(wrap("LANES. A manifest that declared no `phase` gets ONE lane and every leg in it, which "
       "reproduces the source's behaviour exactly — a conversion that changes behaviour is a "
       "conversion whose green means nothing."))
for i, ln in enumerate(lanes):
    A(""); A("[[lane]]"); A("name = %s" % s(ln))
    A('concurrency = 1' if ln in ("fast", "serial") else 'concurrency = "profile"')
    A("short_circuit = %s" % ("true" if ln == "fast" and len(lanes) > 1 else "false"))

A(""); A("# " + "-" * 96)
A(wrap("LEGS. opt_in = true means HELD unless asked for with GATE_OPTIN=1. It carries both source "
       "spellings: `subject = kit` and `optIn: true`."))

over = extra.get("ceiling_over_policy") or {}
held = 0
for lg in legs:
    if not isinstance(lg, dict):
        die("a leg row is not an object")
    unknown = [k for k in lg if k not in MAP and k not in DROP]
    if unknown:
        die("leg %r declares key(s) no mapping covers: %s. The table is the SOURCE: add a rule for "
            "each, or say it is dropped — this converter refuses rather than losing a field silently."
            % (lg.get("name", "?"), ", ".join(sorted(unknown))))
    for k in lg:
        if k in DROP:
            dropped.setdefault(k, []).append(lg.get("name", "?"))
    hold = (lg.get("subject") == "kit") or bool(lg.get("optIn")) or (lg.get("chunk") == "selftests")
    held += hold
    A("")
    if isinstance(lg.get("impure"), str):
        A(wrap("IMPURE: " + lg["impure"]))
    if lg.get("name") in over:
        A(wrap("CEILING: " + str(over[lg["name"]])))
    if lg.get("scope"):
        A(wrap("Source `scope` was %r — %s" % (lg["scope"], DROP["scope"])))
    A("[[leg]]")
    A("name = %s" % s(str(lg.get("name", ""))))
    A("argv = %s" % arr(lg.get("argv") or []))
    if lg.get("cwd") and lg["cwd"] != ".":
        A("cwd = %s" % s(lg["cwd"]))
    A("chunk = %s" % s(str(lg.get("chunk") or "default")))
    A("lane = %s" % s(lg.get("phase") or (lanes[0] if len(lanes) == 1 else "heavy")))
    A("opt_in = %s" % ("true" if hold else "false"))
    c = lg.get("ceiling")
    if isinstance(c, int) and not isinstance(c, bool) and c > 0:
        A("ceiling = %d" % c)
    if lg.get("guard"):
        A("guard = %s" % arr(lg["guard"]))
    if lg.get("impure"):
        A("impure = true")
    if lg.get("tool"):
        A("tool = %s" % s(lg["tool"]))
    if lg.get("full_only"):
        A("full_only = true")

body = "\n".join(L) + "\n"

if DRY:
    sys.stdout.write(body)
else:
    if os.path.exists(OUT) and not FORCE:
        die("%s already exists. Re-run with --force to overwrite it; this converter will not "
            "silently replace a declaration somebody may have edited." % OUT)
    open(OUT, "w", encoding="utf-8", newline="\n").write(body)

# ---- S6: the test report ------------------------------------------------------------------------
# It REPORTS and never edits. A tool cannot run a foreign suite, so it cannot know whether its edit
# was correct, and an edit it cannot verify is worse than a report the owner acts on.
r = ["", "---- upgrade report ----",
     "source:   %s  (dialect %s)" % (SRC, dialect),
     "emitted:  %s%s" % (OUT if not DRY else "(dry run — nothing written)", ""),
     "legs:     %d, of which %d are opt_in (held unless GATE_OPTIN=1)" % (len(legs), held),
     "profiles: %d, from %s" % (len(profiles), PROF),
     "lanes:    %s" % ", ".join(lanes)]
for k, names in sorted(dropped.items()):
    r.append("DROPPED `%s` on %d leg(s): %s" % (k, len(names), DROP[k]))
    r.append("          %s" % ", ".join(names[:6]) + (" …" if len(names) > 6 else ""))

# What the target's OWN files must change. Named, never edited.
hits = []
# THE POPULATION IS WHAT GIT TRACKS, not what the filesystem holds. A raw walk counted 324 files in
# gov by reaching into nested worktrees and build records; the tracked set is the one an owner can
# actually act on, and a report nobody can act on is a report nobody reads.
import subprocess
try:
    tracked = subprocess.run(["git", "-C", TARGET, "ls-files", "-z"],
                             capture_output=True, timeout=60).stdout.decode("utf-8", "replace").split("\0")
except Exception:
    tracked = []
needle = os.path.basename(SRC)
for rel in tracked:
    if not rel or rel in (os.path.relpath(SRC, TARGET).replace(os.sep, "/"),):
        continue
    p = os.path.join(TARGET, rel)
    try:
        if os.path.getsize(p) > 2_000_000:
            continue
        with open(p, encoding="utf-8", errors="ignore") as fh:
            if needle in fh.read():
                hits.append(rel)
    except OSError:
        continue
r.append("")
if hits:
    # SPLIT, because the two halves need different actions. A file under the memory root is almost
    # always a RECORD -- a spec, a review, a build note -- and records are history: they name what
    # was true when they were written and must not be rewritten. Everything else is live and reads
    # the manifest for real. Reporting one number for both makes the actionable half unfindable.
    mroot = os.environ.get("GOV_MEMORY_ROOT", "memory") + "/"
    live = [h for h in hits if not h.startswith(mroot)]
    recs = [h for h in hits if h.startswith(mroot)]
    r.append("FILES NAMING `%s`: %d live, %d under %s" % (os.path.basename(SRC), len(live), len(recs), mroot))
    if live:
        r.append("  LIVE — each reads the old manifest. Repoint it, or record why it still names it:")
        for h in sorted(live)[:40]:
            r.append("      %s" % h)
        if len(live) > 40:
            r.append("      … and %d more" % (len(live) - 40))
    if recs:
        r.append("  RECORDS — history, naming what was true when written. Do NOT rewrite them.")
else:
    # An empty report and a report nobody generated must be distinguishable.
    r.append("NO tracked file outside the manifest names `%s` — nothing to repoint."
             % os.path.basename(SRC))
r.append("")
r.append("The legacy file is NOT deleted. The runner reads it whenever the TOML is absent or the")
r.append("resolved interpreter predates CPython 3.11, so keeping it is the rollback and the floor.")
sys.stderr.write("\n".join(r) + "\n")

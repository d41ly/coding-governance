#!/usr/bin/env python3
"""The acceptance matrix — the deployer driven against repo SHAPES, not against kits.

WHAT THIS IS NOT. `selftest.py` grades MECHANISMS, one fixture per behaviour, and unit 3's
deployability leg grades every registry ENTRY. This grades the repo shapes the contract names,
and it CITES those two rather than re-asserting what they already assert: plan-equals-apply and
apply-twice stay with the deployability leg, and the per-mechanism arms stay in the selftest.

SHAPE 5 IS THE ONE THAT EXECUTES WHAT WAS INSTALLED. The first four grade the install; the fifth
grades the installed thing running. A Tier-2 review found all three of one build's newly shipped
gates broken in a scratch install — two dying with an uncaught traceback where their own docstrings
promised a Refusal — while gov's bar was green, because gov's bar runs every leg from gov's own root
where every default resolves. A leg that has only ever executed in gov is an untested leg.

EVERY ARM'S EXPECTED OUTCOME IS STATED HERE, in the table below, rather than read off the
implementation. An arm with no stated expectation is a test written after the fact against itself,
which is the shape the contract refuses by name. Each asserts a MESSAGE or an on-disk effect and
never an exit code alone — an exit code shared by six unrelated outcomes is the ambiguity the
descriptors' outcome probes exist to resolve.
"""

from __future__ import annotations

import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import govkit  # noqa: E402 — the deployer's OWN descriptor reader and token resolver. A second copy
               # here would be a second answer to "what argv does this leg actually get", which is
               # precisely the question shape 5 exists to settle.

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
GOVKIT = HERE / "govkit.py"
NL = chr(10)
FAILURES: list[str] = []

# ---------------------------------------------------------------------------------------- shape 5
#: The selection, STATED with its reason: the playbook template, its renderer and the two gates that
#: grade what the renderer produces. They are the entries whose legs run against a DEPLOYED artifact
#: rather than against a kit's own fixtures, which is where a gov-only default strands an adopter.
#: Widening this to the whole registry is a matter of supplying each entry's answers; every other
#: entry's legs stay unexecuted here and that is a known ceiling, not an assertion about them.
# ponytail: four entries, not the registry — widen when another entry's leg reads a deployed path.
SCRATCH_KITS = ["playbook", "playbook-render", "check-microformats", "check-line-length"]

#: EVERY DECLARED LEG'S EXPECTED VERDICT, stated here and never read off a run. They are not all
#: "green": `line length` is an opt-in gate whose install-day answer is NOT ADOPTED rather than a
#: measurement, and demanding green from it would be demanding that a gate certify a population it
#: was never given. The leg POPULATION is derived from the descriptors and asserted against these
#: keys in both directions, so a leg added to one of these entries reds until someone states what it
#: prints in a scratch install.
SCRATCH_EXPECT = {
    "playbook render wiring": "render-playbook OK — region matches a fresh render",
    # The arm COUNT is deliberately not stated: it moves every time the engine gains a predicate,
    # and a number here would make each new arm red this table for no reason it can name.
    "playbook render selftest": "render_playbook.selftest OK",
    "micro-format definitions": "microformats OK —",
    "micro-format gate selftest": "PASS (",
    "line length": "NOT ADOPTED — no declaration at",
    # `line-length gate selftest` USED to be here and its removal is the point. The suite it runs is
    # withheld from every target now: TOOL-aQuenchedHarness-6 ported it onto `tools/lib/lib-selftest.sh`,
    # which is gov-internal and travels to nobody, so a shipped copy would red on arrival with
    # `build_fixture: command not found`. It is a leg on GOV's bar with an [[exempt_leg]] row, and
    # this table states what a SCRATCH INSTALL prints — a leg no install receives has no verdict to
    # state. The both-directions assertion below is what caught the mismatch rather than letting the
    # table quietly describe a leg that had stopped being emitted.
}


def check(label: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"ok   {label}")
    else:
        FAILURES.append(label)
        # TRUNCATED FROM THE HEAD, WHICH IS THE END THAT CARRIES THE ANSWER. `detail[:400]` kept the
        # first 400 bytes, and for an `apply` detail those 400 bytes are the numbered step trace —
        # `[1/BASELINE] ...`, `[2/ATTRIBUTES] ...` — while the refusal naming the cause is the LAST
        # line the verb prints. Measured on the post-merge bar of the aFusedCharter merge: two arms
        # reported `[1/BASELINE] this target's descriptor declares no [gate_runner] at all`, which is
        # a step announcement and not a failure at all, and the line that actually explained the red
        # sat just past the cut. A traceback's last line is its exception and a stated Refusal is its
        # last line too, so the tail is the right end for every detail this file passes.
        print(f"FAIL {label}" + (f" — {detail[-400:]}" if detail else ""))


def git(cwd: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(GOVKIT), *args], capture_output=True, text=True)


DEPLOY = ('gov_source = "l"' + NL + 'prefix = "tools"' + NL + 'kits = ["check-wiring"]' + NL
          + "[answers]" + NL + 'memory_root = "memory"' + NL)


def shape(tmp: pathlib.Path, name: str, *, lang: str = "none", hook: str | None = None,
          policy: str = "") -> pathlib.Path:
    g = tmp / name
    g.mkdir(parents=True, exist_ok=True)
    (g / ".governance").mkdir(exist_ok=True)
    (g / ".governance" / "deploy.toml").write_text(DEPLOY + policy, encoding="utf-8", newline=NL)
    (g / "README.md").write_text("t" + NL, encoding="utf-8", newline=NL)
    if lang == "python":
        (g / "app.py").write_text("x = 1" + NL, encoding="utf-8", newline=NL)
    git(g, "init", "-q", "-b", "main")
    git(g, "config", "user.email", "t@e")
    git(g, "config", "user.name", "t")
    if hook is not None:
        hd = g / ".githooks"
        hd.mkdir(exist_ok=True)
        (hd / "pre-commit").write_text(hook, encoding="utf-8", newline=NL)
        (hd / "pre-commit").chmod(0o755)
        git(g, "config", "core.hooksPath", ".githooks")
    git(g, "add", "-A")
    git(g, "commit", "-qm", "base")
    return g


def check_outcome_probes(tmp: pathlib.Path) -> None:
    """AN ACCEPTED NON-ZERO STOP MUST NAME SOMETHING THAT EXISTS — the class, then its instance.

    `[[outcome]] ok = true` says "this adopter exited non-zero ON PURPOSE". A block that declares
    that meaning through an ABSENCE alone is satisfied by every run that DIED BEFORE WRITING,
    because what an adopter was writing is exactly what is absent after it fails. Measured, not
    theorised: `DEPL-cMendedVintage-5` shipped lexicon's `must_not_exist = ".lexicon.conf"`, and the
    failed first scaffold that block could not tell from the posture is the conf's own writer. So an
    accepted stop declared by an absence must also declare a PRESENCE. The two other shipped blocks
    (memory-tree, codebase-map) already carried one; lexicon's is what this arm was written for.

    THE CLASS, NOT THE ENTRY. Naming lexicon in the assertion would certify the one block that
    exists and say nothing about the next kit to declare the same shape, which is the could-not-fail
    shape one level up. The second half then grades lexicon's own two states, because a class rule
    over descriptors cannot show that the engine reaches the same verdict.

    WHAT IT DOES NOT CHECK: whether the entry's adopter actually WRITES the path its `must_not_exist`
    names — that would need a reading of a shell script, and no static rule gets it. The presence
    term is the cheap sufficient condition: with one declared, a run that wrote nothing cannot match.
    # ponytail: shape rule over the descriptors, not an argv analysis — widen only if a block ever
    # earns an exemption from it.
    """
    rep = govkit.Report()
    descs = govkit.read_descriptors(ROOT, govkit.load_toml(
        ROOT / "tools" / "govkit" / "registry.toml"), rep)
    stops = [(eid, b) for eid, (d, _p) in sorted(descs.items())
             for b in d.get("outcome", []) if b.get("ok")]
    # THE LIVENESS ASSERTION. Quantifying over an empty set prints nothing but ok lines, and a probe
    # that cannot move is not a green one.
    check("accepted stops: the registry declares at least one to grade", bool(stops),
          "no [[outcome]] carries ok = true, so the arm below graded nothing")
    for eid, b in stops:
        probe = b.get("probe") or {}
        check("accepted stops: '%s' %r names a file that must EXIST" % (eid, b.get("means")),
              bool(probe.get("must_exist")),
              "probe declares only %s, so a run that died before writing satisfies it"
              % sorted(probe))

    # AND THE ENGINE AGREES, over the shipped lexicon descriptor and the two states it has to
    # separate. Both have no `.lexicon.conf`; only one has the Skill the adopter renders beside it.
    g = tmp / "outcome-probe"
    (g / ".governance").mkdir(parents=True, exist_ok=True)
    (g / ".governance" / "deploy.toml").write_text(DEPLOY, encoding="utf-8", newline=NL)
    deploy = govkit.load_toml(g / ".governance" / "deploy.toml")
    d, _p = descs["lexicon"]
    ctx = govkit.target_context(g, deploy, "lexicon", d)
    skill = g / ".claude" / "skills" / "lexicon" / "SKILL.md"
    skill.parent.mkdir(parents=True, exist_ok=True)
    for label, rendered, want in (("a failed first scaffold", False, False),
                                  ("a declaration removed after one", True, True)):
        if rendered:
            skill.write_text("x" + NL, encoding="utf-8", newline=NL)
        elif skill.exists():
            skill.unlink()
        oc = govkit.classify_outcome(g, d, ctx, 1)
        got = govkit.outcome_accepted(1, oc, govkit.declares_outcome_for(d, 1))
        check("lexicon exit 1 after %s is %s" % (label, "ACCEPTED" if want else "REFUSED"),
              got is want, "means=%r accepted=%s" % (oc.get("means") if oc else None, got))


#: The fixture kit, in two vintages. The FIRST is what the target installs from; the SECOND is the
#: same descriptor with one destination carved out as `project-owned`. Stated as data rather than
#: built by a parameterised function so the difference between them is one visible block.
ROLE_KIT = ('id = "demo"' + NL + 'home = "tools/demo"' + NL
            + "version_from = { none = \"fixture\" }" + NL + NL
            + "[check]" + NL + 'none = "a fixture kit"' + NL + NL
            # NAMED, never `**`. A `**` pool also lands the descriptor itself, and editing the
            # descriptor is exactly what ages this fixture — so the arm would grade a second row
            # that legitimately moved bytes and the "nothing was written" assertion below could
            # never be read cleanly.
            + "[[files]]" + NL + 'include = ["kept.txt", "moved.txt", "gone.txt"]' + NL
            + 'role = "engine"' + NL + NL
            + "[adopt]" + NL + "argv = []" + NL + "mutates_index = false" + NL)
#: The carve-out is a LATER rule, because a `project-owned` rule removes its sources from every
#: EARLIER rule's contribution and a rule ahead of the pool would carve nothing.
ROLE_KIT_MOVED = ROLE_KIT + (NL + "[[files]]" + NL + 'include = ["moved.txt", "gone.txt"]' + NL
                             + 'role = "project-owned"' + NL)


def check_role_move(tmp: pathlib.Path) -> None:
    """A receipt row's role is RE-RESOLVED at every schema, and a disagreement is reported.

    THE FIXTURE IS AGED, NOT FRESH, and that is the whole arm. A fresh install and the descriptor it
    installed from agree by construction, so an arm built on one grades nothing and reports green —
    the shape that passes by finding nothing. So the target installs first, under a rule declaring
    its destination `engine`, edits its own copy, and only THEN does gov's descriptor claim that
    destination `project-owned`. The disagreement exists because the receipt is older than the rule,
    which is the only way it can exist at all.

    EXPECTED, stated here rather than read off a run. The untouched row reports `current`, exactly
    as it did before the re-resolution was un-gated. The moved row reports `role-moved` naming both
    roles, and its bytes do not move — where before it read `stale`, which is a RAW-WRITE verdict,
    so gov's copy went over the adopter's own edit. The receipt keeps recording `engine`, because
    recording the new role is `apply`'s job and not this verb's. And a schema-1 receipt carrying the
    SAME disagreement still REFUSES, because a schema-1 role is untrusted for a different reason and
    neither answer may be acted on there.

    WHAT IT DOES NOT CHECK: any other pair of roles, and any real adopter's receipt. One transition,
    end to end, on a fixture built for it.
    """
    env = dict(os.environ, GOVKIT_NO_REMOTE_PROBE="1")

    def build_gov(tag: str) -> pathlib.Path:
        """A scratch gov holding ONE `demo` entry plus a copy of the engine.

        THE COPY IS TAKEN HERE, at fixture-build time, so the arm runs the engine as this tree has
        it rather than whatever a later edit leaves behind.
        """
        g = tmp.resolve() / ("role-gov-" + tag)
        (g / "tools" / "govkit").mkdir(parents=True, exist_ok=True)
        (g / "tools" / "demo").mkdir(parents=True, exist_ok=True)
        shutil.copy2(GOVKIT, g / "tools" / "govkit" / "govkit.py")
        (g / "tools" / "govkit" / "registry.toml").write_text(
            '[surface]' + NL + 'globs = ["tools/*"]' + NL + NL
            + '[selection]' + NL + 'default = ["demo"]' + NL + NL
            + '[[entry]]' + NL + 'id = "demo"' + NL + 'descriptor = "tools/demo/kit.toml"' + NL + NL
            + '[[exempt]]' + NL + 'path = "tools/govkit"' + NL + 'why = "the deployer itself"' + NL,
            encoding="utf-8", newline=NL)
        (g / "tools" / "demo" / "kit.toml").write_text(ROLE_KIT, encoding="utf-8", newline=NL)
        (g / "tools" / "demo" / "kept.txt").write_text("gov's own bytes" + NL,
                                                       encoding="utf-8", newline=NL)
        (g / "tools" / "demo" / "moved.txt").write_text("gov's own bytes" + NL,
                                                        encoding="utf-8", newline=NL)
        (g / "tools" / "demo" / "gone.txt").write_text("gov's own bytes" + NL,
                                                       encoding="utf-8", newline=NL)
        git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
        git(g, "config", "user.name", "t"); git(g, "config", "core.autocrlf", "false")
        git(g, "add", "-A"); git(g, "commit", "-qm", "the vintage the target installs from")
        return g

    def run_in_gov(g: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(g / "tools" / "govkit" / "govkit.py"), *args],
                              capture_output=True, text=True, env=env)

    def read_verdict(out: str, path: str) -> str:
        """The verdict `update` printed for ONE row, keyed on the path the line ENDS with."""
        for ln in out.splitlines():
            if ln.startswith("  ") and ln.rstrip().endswith(" " + path):
                return ln[2:].split("[", 1)[0].strip()
        return "(no row)"

    OWN = "the adopter's own edit" + NL

    def build_target(tag: str, schema: int) -> tuple[pathlib.Path, pathlib.Path]:
        """Install, let the target edit one landed file, then AGE the descriptor under it."""
        g = build_gov(tag)
        t = tmp.resolve() / ("role-target-" + tag)
        t.mkdir(parents=True, exist_ok=True)
        (t / "README.md").write_text("t" + NL, encoding="utf-8", newline=NL)
        (t / ".governance").mkdir(exist_ok=True)
        (t / ".governance" / "deploy.toml").write_text(
            'gov_source = "local"' + NL + 'prefix = "tools"' + NL + 'kits = ["demo"]' + NL,
            encoding="utf-8", newline=NL)
        git(t, "init", "-q", "-b", "main"); git(t, "config", "user.email", "t@e")
        git(t, "config", "user.name", "t"); git(t, "config", "core.autocrlf", "false")
        git(t, "add", "-A"); git(t, "commit", "-qm", "base")
        ap = run_in_gov(g, "apply", "--target", str(t), "--kits", "demo")
        check("role move [%s]: the fixture installs at all" % tag,
              (t / ".governance" / "install.json").is_file(), ap.stdout + ap.stderr)
        # TWO SHAPES OF ADOPTER STATE, because one of them cannot reach the branch this arm is
        # about. An edit IN PLACE grids to `patched`, which writes nothing even at BASE, so an arm
        # built on that alone stays green over the very restore it was written to stop. A
        # destination the adopter has RENAMED AWAY grids to `missing`, which is a raw-write verdict:
        # at BASE gov puts its own bytes back at a path the adopter deliberately emptied. Measured
        # both ways against the engine as BASE has it, not reasoned.
        (t / "tools" / "demo" / "moved.txt").write_text(OWN, encoding="utf-8", newline=NL)
        (t / "tools" / "demo" / "gone.txt").unlink()
        git(t, "add", "-A"); git(t, "commit", "-qm", "the adopter edits one copy and moves one away")
        rec = t / ".governance" / "install.json"
        data = json.loads(rec.read_text(encoding="utf-8"))
        if schema != data.get("schema"):
            data["schema"] = schema
            rec.write_text(json.dumps(data, indent=2) + NL, encoding="utf-8", newline=NL)
        # THE AGEING. The descriptor moves AFTER the receipt was written, which is the one ordering
        # that produces a disagreement at all.
        (g / "tools" / "demo" / "kit.toml").write_text(ROLE_KIT_MOVED, encoding="utf-8", newline=NL)
        git(g, "add", "-A"); git(g, "commit", "-qm", "the destination becomes the project's own")
        return g, t

    # ---- THE FIXTURE'S OWN PRECONDITION. A receipt that did not record `engine` for the moved row
    # ---- would make every assertion below pass for the wrong reason.
    g3, t3 = build_target("s3", 3)
    rows = {w["path"]: w for w in json.loads(
        (t3 / ".governance" / "install.json").read_text(encoding="utf-8")).get("files", [])}
    check("role move: the aged receipt really records the moved destination as `engine`",
          (rows.get("tools/demo/moved.txt") or {}).get("role") == "engine",
          str(sorted(rows)))

    up = run_in_gov(g3, "update", "--target", str(t3), "--write")
    out = up.stdout + up.stderr
    check("role move: the run does not refuse over a descriptor transition",
          up.returncode == 0, out[-400:])
    # AC2 — the moved row is REPORTED, naming both roles and the path.
    check("role move: the moved row reports `role-moved`, not the recorded role's disposition",
          read_verdict(out, "tools/demo/moved.txt") == "role-moved", out[-800:])
    check("role move: ...and the line names the role it landed under AND the one gov declares now",
          any(ln.rstrip().endswith(" tools/demo/moved.txt")
              and "engine" in ln and "project-owned" in ln for ln in out.splitlines()),
          out[-800:])
    check("role move: ...and the bytes on disk are the adopter's, untouched",
          (t3 / "tools" / "demo" / "moved.txt").read_text(encoding="utf-8") == OWN,
          repr((t3 / "tools" / "demo" / "moved.txt").read_text(encoding="utf-8")))
    # THE RESTORE, which is the defect this whole unit exists to stop and the one an edited-in-place
    # row cannot reach. At BASE this path grades `missing` and gov writes its own bytes back over a
    # destination the adopter emptied on purpose.
    check("role move: the renamed-away destination also reports `role-moved`",
          read_verdict(out, "tools/demo/gone.txt") == "role-moved", out[-800:])
    check("role move: ...and gov does NOT put its bytes back at a path the adopter emptied",
          not (t3 / "tools" / "demo" / "gone.txt").exists(), "the file was restored")
    check("role move: ...and the run says what is now true rather than naming a disposition",
          "NOTHING was written for them" in out and "govkit apply" in out, out[-800:])
    # AC3 — the receipt is not rewritten, and the row counts as no change.
    after = {w["path"]: w for w in json.loads(
        (t3 / ".governance" / "install.json").read_text(encoding="utf-8")).get("files", [])}
    check("role move: the receipt row still records the role it landed under",
          (after.get("tools/demo/moved.txt") or {}).get("role") == "engine",
          str(after.get("tools/demo/moved.txt")))
    check("role move: ...and the run counted NO change at all — the write tally reads zero",
          "wrote 0, moved 0, deleted 0" in out, out[-800:])
    # THE ROW ITSELF, field for field, rather than a word-absence over the whole run. The verdict
    # names are ordinary English and this run prints several sentences containing them, so an
    # absence assertion over the output would be graded by the wrong text.
    check("role move: ...and not one field of the moved row was rewritten",
          after.get("tools/demo/moved.txt") == rows.get("tools/demo/moved.txt"),
          "%r -> %r" % (rows.get("tools/demo/moved.txt"), after.get("tools/demo/moved.txt")))
    # AC1 — the CONTROL. A row whose descriptor still resolves the role it landed under is graded
    # exactly as before, which is what makes the branch above a new path and not a new default.
    check("role move CONTROL: a row whose role did NOT move reports `current` as it always did",
          read_verdict(out, "tools/demo/kept.txt") == "current", out[-800:])

    # AC4 — the schema-1 branch SURVIVES. Same disagreement, untrusted role, still a refusal.
    g1, t1 = build_target("s1", 1)
    u1 = run_in_gov(g1, "update", "--target", str(t1))
    o1 = u1.stdout + u1.stderr
    check("role move: a schema-1 receipt carrying the same disagreement still REFUSES",
          "cannot be trusted about" in o1, o1[-800:])
    check("role move: ...and does NOT take the reporting path",
          read_verdict(o1, "tools/demo/moved.txt") != "role-moved", o1[-800:])


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        shapes = 0

        # The descriptor-shaped arms first: they need no install, so a registry that has re-opened
        # the accepted-stop hole says so in milliseconds rather than after five scratch installs.
        check_outcome_probes(tmp)
        check_role_move(tmp)

        # SHAPE 1 — a fresh, empty repository.
        # EXPECTED: the install COMPLETES and the receipt exists. This is the base case and every
        # other shape is measured as a departure from it.
        shapes += 1
        g = shape(tmp, "empty")
        p = run("apply", "--target", str(g), "--kits", "check-wiring")
        check("empty repo: the install completes", p.returncode == 0, p.stdout + p.stderr)
        check("empty repo: a receipt exists",
              (g / ".governance" / "install.json").is_file(), "")
        check("empty repo: the landed file is on disk, not merely recorded",
              (g / "tools" / "check-wiring.sh").is_file(), "")

        # SHAPE 2 — a repository with no Python of its own.
        # EXPECTED: the DEPLOYER runs on the deployer's interpreter regardless; the target having no
        # Python is irrelevant to landing. Stated because the opposite is the natural assumption.
        shapes += 1
        g = shape(tmp, "nopython", lang="none")
        p = run("apply", "--target", str(g), "--kits", "check-wiring")
        check("no-python repo: the deployer runs on ITS OWN interpreter and lands anyway",
              p.returncode == 0 and (g / "tools" / "check-wiring.sh").is_file(),
              p.stdout + p.stderr)

        # SHAPE 3 — a repository whose pre-commit hook REFUSES.
        # EXPECTED: the install COMPLETES and the receipt exists, because `apply` never commits and
        # therefore no hook fires during the install itself; and an ORDER carries the hook's own
        # output, so the operator meets the refusal here rather than when they try to land.
        shapes += 1
        g = shape(tmp, "hookblock", hook="#!/usr/bin/env bash" + NL + "echo NOPE >&2" + NL +
                  "exit 1" + NL)
        p = run("apply", "--target", str(g), "--kits", "check-wiring")
        check("blocking-hook repo: the install COMPLETES anyway — apply never commits",
              (g / ".governance" / "install.json").is_file(), p.stdout + p.stderr)
        ob = g / ".governance" / "outbox" / "hook-block.md"
        check("blocking-hook repo: an order carries the hook's OWN output",
              ob.is_file() and "NOPE" in ob.read_text(encoding="utf-8"),
              ob.read_text(encoding="utf-8") if ob.is_file() else "absent")
        check("blocking-hook repo: the probe records the state by NAME, not by an exit code",
              json.loads((g / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("hook_block", {}).get("state") == "block", "")
        # And the NEGATIVE half, which is what makes the three-valued probe worth having: with NO
        # hook the probe must record `no-hook`, NOT `pass` — measured, git's hook runner exits
        # non-zero for both, so an exit-code reading would collapse them.
        g2 = shape(tmp, "nohook")
        run("apply", "--target", str(g2), "--kits", "check-wiring")
        check("no-hook repo: recorded as no-hook, a state distinct from a refusing hook",
              json.loads((g2 / ".governance" / "install.json").read_text(
                  encoding="utf-8")).get("hook_block", {}).get("state") == "no-hook", "")

        # SHAPE 4 — a repository carrying a gate leg of its own that is ALREADY red.
        # EXPECTED with the default policy: the install COMPLETES, the pre-existing red leg is
        # REPORTED and does not fail it. With the policy flipped to refuse: apply exits non-zero
        # and leaves NO receipt, because the refusal happens at the baseline, before any write.
        shapes += 1
        runner = ("import json, subprocess" + NL +
                  "legs = json.load(open('tools/legs.json'))" + NL +
                  "for l in legs:" + NL +
                  "    c = subprocess.run(l['argv'], capture_output=True).returncode" + NL +
                  "    print(('GATE ok    ' if c == 0 else 'GATE FAIL  ') + l['name'])" + NL)
        decl = (NL + "[gate_runner]" + NL + 'kind = "manifest"' + NL +
                'file = "tools/legs.json"' + NL + 'grammar = "json-array"' + NL +
                'dedupe_key = "name"' + NL +
                'command = ["%s", "tools/runner.py"]' % sys.executable.replace(chr(92), "/") + NL +
                'run_all_env = { GATE_FULL = "1" }' + NL +
                'observed_ran = ["GATE ok    {name}"]' + NL +
                'observed_failed = ["GATE FAIL  {name}"]' + NL)

        for policy_val, label in (("proceed", "default"), ("refuse", "refuse")):
            g = tmp / ("prered-" + policy_val)
            (g / "tools").mkdir(parents=True, exist_ok=True)
            (g / "tools" / "runner.py").write_text(runner, encoding="utf-8", newline=NL)
            (g / "tools" / "legs.json").write_text(
                json.dumps([{"name": "theirs", "argv": ["false"]}], indent=2) + NL,
                encoding="utf-8", newline=NL)
            (g / ".governance").mkdir(exist_ok=True)
            (g / ".governance" / "deploy.toml").write_text(
                DEPLOY + NL + "[policy]" + NL + 'on_baseline_red = "%s"' % policy_val + NL + decl,
                encoding="utf-8", newline=NL)
            git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
            git(g, "config", "user.name", "t"); git(g, "add", "-A"); git(g, "commit", "-qm", "b")
            p = run("apply", "--target", str(g), "--kits", "check-wiring")
            if policy_val == "proceed":
                check("pre-existing-red repo: the install completes and REPORTS the red leg",
                      (g / ".governance" / "install.json").is_file()
                      and "ALREADY red" in p.stdout, p.stdout + p.stderr)
                # TOOL-dUnstalledConvoy-26 AC9: SUBJECT REACHES THE TARGET. Graded here rather than
                # in the selftest because this is the shape that matters — a real `apply` into a
                # real target, read back off the target's own manifest. Without the field the leg
                # arrives as an ordinary bar leg and the adopter runs the kit's self-test on every
                # push, which is the whole defect the unit exists to remove.
                _emitted = json.loads(
                    (g / "tools" / "legs.json").read_text(encoding="utf-8"))
                _by = {l.get("name"): l for l in _emitted}
                _wiring = _by.get("check-wiring self-test")
                check("AC9: the emitted leg reached the target's manifest at all",
                      _wiring is not None, str(sorted(_by)))
                check("AC9: and it carries subject = 'kit', so the target HOLDS it by default",
                      (_wiring or {}).get("subject") == "kit", str(_wiring))
                # ITS CONTROL: the target's OWN leg is untouched. govkit owning a NAME is not govkit
                # owning the ROW, and a deployer that stamped a subject onto a leg the target wrote
                # would be deciding that repository's bar for it.
                check("AC9 control: the target's own pre-existing leg gains no subject",
                      "subject" not in (_by.get("theirs") or {"subject": "leaked"}),
                      str(_by.get("theirs")))
            else:
                check("pre-existing-red repo, policy=refuse: apply refuses NAMING the leg",
                      "theirs" in p.stderr, p.stdout + p.stderr)
                check("pre-existing-red repo, policy=refuse: and leaves NO receipt — the refusal "
                      "is at the baseline, before any write",
                      not (g / ".governance" / "install.json").exists(), "")

        # SHAPE 5 — a scratch target that has just installed, running the legs it was GIVEN.
        # EXPECTED: `apply` renders the charter region into the target's own AGENTS.md, and every
        # gate leg the selected entries declare then runs THERE and prints the verdict stated in
        # SCRATCH_EXPECT. Each arm asserts that message plus the absence of a Python traceback —
        # never an exit code — because a traceback and a stated Refusal share rc=1, and telling them
        # apart is the whole point of the shape.
        shapes += 1
        # RESOLVED, not `tmp / ...`. `tempfile` hands back an 8.3 short path on Windows
        # (`C:\Users\DAILY-~1\...`), and one probe in the renderer echoes back whatever spelling the
        # caller used — so `apply` and the leg saw two names for one directory and the arm reported
        # a DRIFT that was the FIXTURE's, not the product's. The product's own sensitivity to that
        # spelling is real and recorded; this shape is not the place it gets measured, because a
        # fixture-induced red teaches the reader to distrust the arm.
        g = tmp.resolve() / "scratch-install"
        g.mkdir(parents=True, exist_ok=True)
        (g / "README.md").write_text("t" + NL, encoding="utf-8", newline=NL)
        git(g, "init", "-q", "-b", "main"); git(g, "config", "user.email", "t@e")
        git(g, "config", "user.name", "t"); git(g, "add", "-A"); git(g, "commit", "-qm", "base")

        # The answers are DERIVED from the descriptor's own placeholder rows, never listed. Every
        # key gets a stub, whatever its class: for a `derived` row the probe still wins when it can
        # see, and the stub is only the override the engine already honours when it cannot. A hand
        # list here would go stale the first time the charter grew a placeholder — which is the
        # rot this file's own header refuses.
        pdesc = govkit.load_toml(ROOT / "tools" / "govkit" / "entries" / "playbook.kit.toml")
        ans = {r["key"].lower(): "stated for the scratch install"
               for r in pdesc.get("placeholder", [])}
        ans["playbook_path"] = "docs/PARALLEL.md"
        (g / ".governance").mkdir(exist_ok=True)
        (g / ".governance" / "deploy.toml").write_text(
            'gov_source = "."' + NL + 'prefix = "tools"' + NL + "drop_blocks = []" + NL
            + "kits = [" + ", ".join('"%s"' % k for k in SCRATCH_KITS) + "]" + NL
            + "[answers]" + NL
            + NL.join('%s = "%s"' % (k, v) for k, v in sorted(ans.items())) + NL,
            encoding="utf-8", newline=NL)
        git(g, "add", "-A"); git(g, "commit", "-qm", "governance")

        p = run("apply", "--target", str(g), "--kits", ",".join(SCRATCH_KITS))
        check("scratch install: the charter template lands at the operator's chosen path",
              (g / "docs" / "PARALLEL.md").is_file(), p.stdout + p.stderr)
        check("scratch install: apply RENDERS the region into the target's own charter",
              (g / "AGENTS.md").is_file()
              and "<!-- gov:playbook -->" in (g / "AGENTS.md").read_text(encoding="utf-8"),
              p.stdout + p.stderr)

        deploy = govkit.load_toml(g / ".governance" / "deploy.toml")
        rep = govkit.Report()
        descs = govkit.read_descriptors(ROOT, govkit.load_toml(
            ROOT / "tools" / "govkit" / "registry.toml"), rep)
        legs: list[tuple[str, list[str]]] = []
        for eid in SCRATCH_KITS:
            d, _dp = descs[eid]
            ctx = govkit.target_context(g, deploy, eid, d)
            for leg in d.get("gate_leg", []):
                argv, miss = [], []
                for a in leg.get("argv", []):
                    s, m = govkit.resolve_tokens(a, ctx)
                    argv.append(s); miss += m
                check("scratch install: leg '%s' argv resolves every token" % leg.get("name"),
                      not miss, "unresolved: %s" % miss)
                legs.append((leg.get("name"), argv))

        # BOTH DIRECTIONS, so this table cannot drift from the descriptors it grades.
        check("scratch install: the declared leg set and the stated expectations are the same set",
              {n for n, _a in legs} == set(SCRATCH_EXPECT),
              "declared=%s stated=%s" % (sorted(n for n, _a in legs), sorted(SCRATCH_EXPECT)))

        for name, argv in legs:
            want = SCRATCH_EXPECT.get(name)
            if want is None:
                continue
            # Through govkit's own shell resolver, for the reason its docstring records: this
            # harness is a WINDOWS python running a leg whose argv names a bare `bash`, and the
            # Windows loader answers that with the System32 WSL launcher. A real operator's
            # runner is already inside bash and never sees it, so the harness has to ask for
            # the same shell the runner would have used, or it grades a leg nobody will run.
            lp = subprocess.run(govkit.resolve_shell_argv(argv), cwd=str(g), capture_output=True,
                                text=True)
            out = (lp.stdout or "") + (lp.stderr or "")
            check("scratch install: leg '%s' prints its stated verdict where it was installed"
                  % name, want in out, out)
            check("scratch install: leg '%s' answers with a message, not a traceback" % name,
                  "Traceback (most recent call last)" not in out, out)

        print(f"govkit-matrix: {shapes} repo shape(s) exercised")
        if shapes == 0:
            print("govkit-matrix: NO shape ran — a matrix over nothing is not a matrix")
            return 1
    if FAILURES:
        print(f"govkit-matrix: {len(FAILURES)} FAILED — " + "; ".join(FAILURES[:3]))
        return 1
    print("govkit-matrix: all arms held")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Atlas instruments: the fifth version's refusals and checks

The Closed Loop Atlas's fifth version carries every record in the build folder and compares today's
product with the target, area by area. Its generator refuses data it cannot place. This record keeps the
probe that saw each new refusal red, the browser checks on the generated page, and the procedure that
regenerates it.

## [procedure] Regenerate, look, publish

- `python memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check` derives
  everything and writes nothing.
- `--out <page.html>` writes the publishable page. The template beside the generator keeps an empty
  data region, so the page, about 4 MB, is never committed.
- The page is published to the existing artifact by passing its link as `url`:
  `https://claude.ai/artifact/GXivko4hRVxQG9mJNXUaZR`.
- For a local look, serve the page's directory with `python -m http.server`. The browser pane refused a
  `file://` open of the 4 MB page, while the 100 KB template opened.
- After a regeneration the browser can serve the old page from its cache. A query string on the URL
  loads the new one.

## [refusals] What the generator refuses

Carried from the fourth version, the generator refuses:
- a table row whose cell count differs from its header;
- a step whose item lines outnumber the items its table parsed, or an item tag the pattern cannot read;
- a gap line the register's table did not parse, a gap owned by no chain build or by two, and a gap a
  build owns that the register lacks;
- a review record without its verdict or its review-shape line.

New in the fifth, it refuses:
- a record whose sections do not rejoin to its exact text;
- a comparison area whose measured section does not resolve;
- a gap stage that no comparison area claims, or that two claim;
- principles not numbered P1 to Pn without a gap, or a principle line it cannot parse;
- a design record that records an owner's answer while no section of it joins the decision trail;
- an event bullet in the session log that the parser cannot place;
- a section of architecture v2 with no view declared for it;
- the build README without its opened date.

**What they do not check.**
- The decision trail is selected by section tags and titles. A decision section named by neither is
  missed whenever its record has another section in the trail.
- New content in a layer record reaches the Records view and its search, but no structured view until
  the template shows it.
- The page's script has no automated test. The checks under `[preview]` were run by hand.

## [reds] Each new refusal, seen red

The probe loads a fresh copy of the generator per arm, plants one defect and expects `derive()` to
refuse with the named message. Its control arm plants nothing and must derive cleanly.

```python
"""Plant one defect under each of the atlas generator's new refusals and confirm each derivation refuses.

Usage: python plant_reds.py <atlas.py>
Each arm loads a fresh copy of the generator, plants its defect, runs derive() and expects SystemExit with
the named message. The control arm plants nothing and must derive cleanly.
"""
import importlib.util
import sys

GEN = sys.argv[1]


def fresh():
    spec = importlib.util.spec_from_file_location("atlas_probe", GEN)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def arm(name, plant, expect):
    m = fresh()
    plant(m)
    try:
        m.derive()
    except SystemExit as e:
        msg = str(e.code)
        ok = expect in msg
        print(f"{'RED ' if ok else 'WRONG'} {name}: {msg[:110]}")
        return ok
    print(f"GREEN {name}: derived without refusing")
    return expect is None


def drop_v2_view(m):
    del m.V2_VIEWS["floor"]


def drop_area_stage(m):
    m.AREAS = [a for a in m.AREAS if a["key"] != "tooling"]


def lose_a_line(m):
    """Mutate the splitter itself so it drops each record's preamble; its input stays the record's text."""
    import pathlib
    src = pathlib.Path(GEN).read_text(encoding="utf-8")
    old = "        if a == b:\n            continue\n"
    if src.count(old) != 1:
        sys.exit("the splitter's skip line was not found once")
    ns = {"__file__": str(pathlib.Path(GEN).resolve()), "__name__": "atlas_mutant"}
    exec(compile(src.replace(old, "        if a == b or a == 0:\n            continue\n"), GEN, "exec"), ns)
    m.split_sections = ns["split_sections"]


def break_an_event(m):
    real = m.text

    def text(p):
        t = real(p)
        if p.name.endswith("session-log.md"):
            t = t.replace("- 2026-10-16, session 1799cb98: the owner said, verbatim:", "- 2026-10-16, session 1799cb9: the owner said, verbatim:", 1)
        return t
    m.text = text


def blind_the_trail(m):
    m.DECISION_TAGS = set()
    m.DECISION_TITLE = m.re.compile(r"(?!x)x")


def unparseable_principle(m):
    real = m.text

    def text(p):
        t = real(p)
        if p.name.endswith("architecture-v2.md"):
            t = t.replace("- **P7 ", "- **P70 ", 1)
        return t
    m.text = text


results = [
    arm("control: nothing planted", lambda m: None, None),
    arm("a v2 section with no declared view", drop_v2_view, "v2's sections and the views declared for them differ"),
    arm("a gap stage no area claims", drop_area_stage, "gap stages no comparison area claims"),
    arm("a split that loses a line", lose_a_line, "do not rejoin"),
    arm("an event bullet the parser cannot place", break_an_event, "event bullets but"),
    arm("a trail that selects nothing", blind_the_trail, "records an owner's answer, yet no section title marks it"),
    arm("a principle numbered out of sequence", unparseable_principle, "the principles are not P1 to"),
]
print(f"{sum(results)} of {len(results)} arms as expected")
sys.exit(0 if all(results) else 1)
```

Its run on 2026-10-16, exit status 0:

```text
GREEN control: nothing planted: derived without refusing
RED  a v2 section with no declared view: atlas: v2's sections and the views declared for them differ: ['floor']
RED  a gap stage no area claims: atlas: gap stages no comparison area claims: ['Tooling']
RED  a split that loses a line: atlas: a record's sections do not rejoin to its text
RED  an event bullet the parser cannot place: atlas: 54 event bullets but 53 parsed
RED  a trail that selects nothing: atlas: flow-interactions records an owner's answer, yet no section title marks it
RED  a principle numbered out of sequence: atlas: the principles are not P1 to P30 without a gap: [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
7 of 7 arms as expected
```

The split arm's first version stayed green. It changed the splitter's input, and the rejoin check
compares the parts with that same input, so nothing was planted. The arm now mutates the splitter.

## [preview] The generated page, in a browser

- The page was served from the scratchpad at `http://localhost:8765`, at 1440 by 900 and at 375 by 812.
- All 11 views built with no console error, and the markdown renderer loaded.
- At 375 wide, no view scrolls sideways: the page's scroll width equals the window's.
- Deploy's comparison renders its exit conditions as a five-item list.
- The decision trail names each level-3 section's parent, and an opened entry shows its section's text.

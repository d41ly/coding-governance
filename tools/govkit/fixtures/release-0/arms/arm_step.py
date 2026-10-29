"""arm_step.py — the upgrade-walk leg's defective steps, one per arm (TOOL-dSafePassage-5 S7).

    python arm_step.py <arm> <up|down|witness> <target> [<path>]

Each arm is a step that is wrong in exactly one way, so the case it must red can be watched going
red. It writes under <target>/.uw-arm/ unless its defect is about another path. Exit 0 or 1, as a
step's phase does.
"""
import pathlib
import sys
import time

arm, phase, target = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
path = target / sys.argv[4] if len(sys.argv) > 4 else None
d = target / ".uw-arm"


def write(name: str, text: str, mode: str = "w") -> None:
    d.mkdir(exist_ok=True)
    with open(d / name, mode, encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def remove_arm_dir() -> None:
    for f in d.glob("*") if d.is_dir() else []:
        f.unlink()
    if d.is_dir():
        d.rmdir()


MARK = "upgrade-walk plant engine-edit"
if arm == "breaks-isolation" and phase == "up":
    # The defect: a step that reaches the target's own code. The target's root first on the path,
    # then a module the isolation check plants there by the standard library's name.
    sys.path.insert(0, str(target))
    import json  # noqa: F401,E402
    raise SystemExit(0)
if phase == "witness":
    if arm == "witness-first":
        ok = (d / "0-witness").is_file()
    elif arm == "not-rerunnable":
        ok = (d / "1-done").is_file()
    elif arm == "lossy-down":
        ok = (d / "lossy").is_file() and (d / "lossy").read_text(encoding="utf-8") == "payload\n"
    elif arm == "drops-plant":
        ok = MARK not in path.read_text(encoding="utf-8")
    elif arm == "drops-shim":
        ok = not path.exists()
    else:  # no-op and breaks-isolation: a witness that always holds
        ok = True
    raise SystemExit(0 if ok else 1)
if phase == "up":
    if arm == "witness-first":  # the defect: its witness lands before its payload
        write("0-witness", "ok\n")
        time.sleep(0.05)
        write("1-payload", "payload\n")
    elif arm == "not-rerunnable":  # the defect: every run appends again
        write("0-lines", "one more line\n", "a")
        time.sleep(0.05)
        write("1-done", "done\n")
    elif arm == "lossy-down":
        write("lossy", "payload\n")
    elif arm == "drops-plant":  # the defect: an adopter's line overwritten with no order
        text = path.read_text(encoding="utf-8")
        path.write_text("".join(ln for ln in text.splitlines(True) if MARK not in ln), encoding="utf-8", newline="")
    elif arm == "drops-shim":  # the defect: a step unlinking a path a shim row still forwards from
        path.unlink(missing_ok=True)
    raise SystemExit(0)
if phase == "down":
    if arm == "lossy-down":  # the defect: its down leaves one byte behind
        write("lossy", "p")
    elif arm in ("witness-first", "not-rerunnable"):
        remove_arm_dir()
    raise SystemExit(0)
raise SystemExit(2)

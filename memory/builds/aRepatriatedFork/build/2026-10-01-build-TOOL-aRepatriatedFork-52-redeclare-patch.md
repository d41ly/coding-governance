# TOOL-aRepatriatedFork-52 — the relocated clone's re-declaration patch, as R2 measured it

**Serves:** research TOOL-aRepatriatedFork-52

VERIFYING repair R2 (2026-10-01) wrote this patch against the leg's relocated clone: it re-spells gov's own declarations (GOV_KITROOT in .githooks/gate-env.sh, the charter, the map and conf files, the renders) so they follow a moved tool root. With it applied the gov-declaration rows went green at foreign prefixes. It was reverted from the leg at the main loop's instruction, because the leg's design is TOOL-aRepatriatedFork-52's. It is recorded here verbatim so that unit builds from it rather than from a scratch file.

```diff
diff --git a/tools/run-gates/foreign-prefix.gov.test.sh b/tools/run-gates/foreign-prefix.gov.test.sh
index e3eb99a4..e8f5cd26 100644
--- a/tools/run-gates/foreign-prefix.gov.test.sh
+++ b/tools/run-gates/foreign-prefix.gov.test.sh
@@ -38,8 +38,10 @@
 #     prefix and read only at that prefix is self-consistent, so it passes at every host prefix —
 #     measured on this leg's red control. What reds here is a suite reading the HOST tree through a
 #     literal; the spelling inside a fixture is the install-prefix ban's to grade;
-#   * gov's wiring OUTSIDE the tool root — `.claude/`, the hooks path, the charter — which does not
-#     move, so a suite reading it sees gov's own spelling at every prefix;
+#   * gov's declarations spelled any way but the old root's path head. Each move re-spells the
+#     charter, `.claude/`, the hook config, the confs, the map and the listed renders by that head
+#     (`redeclare_wiring`), as an install at the new prefix carries them; a declaration naming the
+#     root another way still reads gov's own spelling, and the record corpus is never re-spelled;
 #   * an ADOPTER's tree. This moves GOV, it installs into nobody's repository: `govkit apply` has its
 #     own suites, and an apply target lacks the records and withheld suites this leg compares.
 # COST: hours. One calibrate and three pooled runs of the whole population, held, run once per build.
@@ -153,7 +155,51 @@ set_tool_root() { # $1 = the new prefix, empty for the repo root
         done ;;
     *) mkdir -p "$(dirname "$to")"; git mv "$TROOT" "$to" || return 1 ;;
   esac
-  git commit -q -m "foreign-prefix: tool root at ${to:-the repo root}"
+  redeclare_wiring "$to" || return 1
+  git add -A && git commit -q -m "foreign-prefix: tool root at ${to:-the repo root}, gov's declarations with it"
+}
+
+redeclare_wiring() { # $1 = the new prefix, empty for the repo root; the move is STAGED, not committed
+  # GOV'S OWN DECLARATIONS MOVE WITH ITS TOOL ROOT, as an install at that prefix carries them: the
+  # charter, the hook config's GOV_KITROOT, the conf files, the map, the waiver registries and the
+  # renders the install-prefix gate lists. Left naming the old root they made the first whole run red
+  # on rows that read them (both pre-push suites, the gov canary, the build harness, the map) for an
+  # install no adopter has (TOOL-aRepatriatedFork-30, gate repair at VERIFYING). NOTHING ELSE the move
+  # brought in is touched, so a literal an engine or a suite carries still reds where it should, and
+  # the record corpus keeps the history it recorded.
+  local to="$1" py renders
+  py=$(resolve_python) || return 1
+  renders=$(bash "${to:+$to/}check-install-prefix.sh" --list 2>/dev/null | awk '$1 == "render" { print $2 }')
+  [ -n "$renders" ] || { echo "foreign-prefix: the install-prefix gate listed no render at ${to:-the repo root} — REFUSING to re-spell blind"; return 1; }
+  git diff --cached --no-renames --name-only --diff-filter=A > "$TMPD/moved.txt"
+  printf '%s\n' "$renders" > "$TMPD/renders.txt"
+  "$py" -c '
+import re, subprocess, sys
+old, new, moved_f, renders_f = sys.argv[1:5]
+head = new + "/" if new else ""
+moved = set(open(moved_f, encoding="utf-8").read().split())
+renders = set(open(renders_f, encoding="utf-8").read().split()) & moved
+records = ("memory/builds/", "memory/archive/", "memory/ledger/", "memory/backlog/", "memory/DECISIONS.md")
+path = re.compile(rb"(?<![A-Za-z0-9_.~-])" + re.escape(old.encode()) + rb"/")
+kitroot = re.compile(rb"^(GOV_KITROOT=)" + re.escape(old.encode()) + rb"[ \t]*$", re.M)
+n = 0
+for f in subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout.decode("utf-8").split("\0"):
+    if not f or f.startswith(records) or (f in moved and f not in renders):
+        continue
+    try:
+        b = open(f, "rb").read()
+    except OSError:
+        continue
+    if b"\0" in b:
+        continue
+    r = path.sub(head.encode(), kitroot.sub(rb"\g<1>" + (new.encode() or b"."), b))
+    if r != b:
+        open(f, "wb").write(r)
+        n += 1
+print("foreign-prefix: %d declaration file(s) re-spelled from %s/ to %s" % (n, old, head or "the repo root"))
+if not n:
+    sys.exit("foreign-prefix: nothing re-spelled, so the moved tree still names the old root")
+' "$TROOT" "$to" "$TMPD/moved.txt" "$TMPD/renders.txt"
 }
 
 run_at_prefix() { # $1 = prefix, empty for the repo root
```

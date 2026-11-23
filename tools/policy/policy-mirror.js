#!/usr/bin/env node
// policy-mirror.js — the one reader of the policy file's JSON mirror, for hooks (TOOL-dGroundRules-5).
//
//   const { readPolicy, PolicyRefusal } = require("<this kit>/policy-mirror.js");
//   readPolicy(key, { repo })   // -> { value, source, reason }, or throws a PolicyRefusal
//   node <this kit>/policy-mirror.js get <key> [--repo <dir>] [--explain]
//
// A hook cannot parse TOML, so it reads policy through `.governance/policy.json`, which
// `policy.py mirror --write` renders and every landing regenerates. THE ONE EVALUATION ORDER:
//   1. top is `git -C <repo> rev-parse --show-toplevel`; the kit's place is this file's directory
//      relative to it.
//   2. L, the landed revision: `bash <kit>/policy-shim.sh landed`, run in top. Its refusal is a
//      PolicyRefusal carrying the shim's reason.
//   3. The mirror text, `git cat-file blob L:.governance/policy.json`, and the blob ids of
//      `.governance/policy.toml`, `<kit>/catalogue.toml`, each name of MIRROR_KIT_INPUTS as
//      `<kit>/<name>`, and each path of MIRROR_LEGACY_INPUTS, at L, null where absent: the reader's
//      own list, never the stored mirror's keys (KICK-dKeptSession-49, KICK-dKeptSession-62). A
//      missing mirror, or text that does not parse as a JSON mirror, is ABSENT.
//   4. Every recorded id equals its id at L: the mirror is FRESH, and a key it holds is returned
//      with its recorded source and reason, each `{rev}` the render wrote in the reason filled with
//      `<L8>, the landed revision` (TOOL-dGroundRules-65). A key it does not hold goes to step 6.
//   5. Any id differing, a legacy input's among them, an expected input the mirror does not record,
//      a legacy input's included, or no `legacy_blobs` at all: the mirror is
//      STALE (TOOL-dGroundRules-21 S17), so a landing that changes `.agent-cap.conf` alone is never
//      read through a mirror holding the old limit.
//   6. ABSENT, STALE or a missing key: `policy-shim.sh get policy-file.on-invalid`. Any value but
//      `last-valid` throws `policy: refused · .governance/policy.json:0 · <absent|stale> at <L8>;
//      policy-file.on-invalid is <value>`; a missing key is no mirror failure and skips that
//      refusal. Otherwise the shim's `get <key>` is returned, its reason prefixed
//      `mirror <absent|stale> at <L8>; ` where the mirror failed.
// The working-tree mirror is never opened. A shim refusal, exit 2 with the reader's line, is a
// PolicyRefusal with that line, so a stale mirror over an invalid file with no valid revision
// refuses exactly as the TOML reader does. Every other shim outcome, exit 1 or 127, a null status, a
// signal or a spawn error, is a PolicyRefusal naming the status, the signal and the shim's stderr
// (TOOL-dGroundRules-21 S16). Each read spawns git and the shim; only the bash that runs the shim is
// found once per process, by running each candidate as the policy kit's checker finds it.
"use strict";
const { spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const MIRROR_REL = ".governance/policy.json";
const POLICY_REL = ".governance/policy.toml";
// The location variables git exports to a hook, dropped as the reader drops them, so the helper
// reads the repository it was pointed at.
const GIT_LOCATION_VARS = new Set(["GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
  "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE", "GIT_PREFIX"]);
const ENV = Object.fromEntries(Object.entries(process.env).filter(([k]) => !GIT_LOCATION_VARS.has(k.toUpperCase())));
// Forward slashes: the shim finds its kit by cutting its own path at the last `/`.
const SHIM = path.join(__dirname, "policy-shim.sh").split(path.sep).join("/");
// The kit-relative inputs the reader owes, by name: each is compared at L whether or not the stored
// mirror records it, so a mirror rendered before one joined its render reads STALE
// (KICK-dKeptSession-49 S1). The preset store, which the preset step reads (KICK-dKeptSession-40).
const MIRROR_KIT_INPUTS = ["presets.toml"];
// The repository-relative inputs the reader owes, a copy of policy.py's LEGACY_INPUTS compared at L
// as MIRROR_KIT_INPUTS is, so a mirror missing one reads STALE (KICK-dKeptSession-62 S24). The
// policy fixtures' `mirror-input-parity` holds both lists to policy.py's; adding an input is THE RULE
// in this kit's README, "The mirror".
const MIRROR_LEGACY_INPUTS = [".agent-cap.conf", ".governance/instructions.toml"];

class PolicyRefusal extends Error {}

function runGit(cwd, args, input) {
  return spawnSync("git", args, { cwd, env: ENV, input, encoding: "utf8", windowsHide: true });
}

// >>> resolve_bash_js -- canonical copy: resolve_bash.js in the gov lib dir (byte-identical; gated)
// `{found, tried, refusal}`: resolve_bash.py's `scan_bash`, the same candidates, walk and acceptance.
// GOV_BASH first, and when set nothing after it is tried; then Git's own `bin/bash.exe`, the third
// parent of `git --exec-path`; then each PATH directory's `bash.exe` and `bash`, a System32 or
// WindowsApps launcher reported and never run. A candidate passes when one run prints `uname -s` as
// its first line and exits 0, `test -f` on `script` included when one is given; on a `windows` host
// the answer must start MINGW or MSYS, so WSL's launcher is refused under any name. Past GOV_BASH every
// candidate is run and reported once; `found` is the first that passed, or "" with `refusal` naming
// every `tried` line. The bare name `bash` is never returned, and nothing is memoised here. On a
// `posix` host the hosting file is judged first: WSL running it from a Windows checkout under `/mnt/`
// returns no `found`, an empty `tried` and the wrong-shell refusal, before any candidate is tried.
// `wrongShellAt` is resolve_bash.py's `wrong_shell_at` and the shell block `refuse_wrong_shell`'s:
// true when `wsl` is set and the path sits under a single-letter `/mnt/<drive>/` (TOOL-dWitnessedBar-27).
function wrongShellAt(path, wsl) {
  return Boolean(wsl) && /^\/mnt\/[a-z]\//.test(String(path));
}
function scanBash({ script = "", host = "" } = {}) {
  const cp = require("child_process"), fs = require("fs"), path = require("path");
  const hostRule = host || (process.platform === "win32" ? "windows" : "posix");
  if (hostRule === "posix") {
    const here = path.resolve(__filename);
    const wsl = Boolean(process.env.WSL_DISTRO_NAME) || fs.existsSync("/proc/sys/fs/binfmt_misc/WSLInterop");
    if (wrongShellAt(here, wsl)) return { found: "", tried: [], refusal: "WSL is running " + here +
      " from a Windows checkout under /mnt/; run it with Git's bash (C:/Program Files/Git/bin/bash.exe)" };
  }
  const tried = [], seen = new Set();
  const runProbe = (cand) => {
    const r = cp.spawnSync(cand, ["-c", 'uname -s && { [ -z "$1" ] || test -f "$1"; }', "_", String(script)],
      { stdio: ["ignore", "pipe", "pipe"], timeout: 20000, windowsHide: true });
    if (r.error || r.status === null) return "did not run";
    const u = (r.stdout || Buffer.alloc(0)).toString("utf8").replace(/\0/g, "").split("\n")[0].trim();
    if (!u) return "did not run";
    if (hostRule === "windows" && !u.startsWith("MINGW") && !u.startsWith("MSYS")) return "answered " + u;
    return r.status === 0 ? "runs" : "cannot see " + String(script);
  };
  const checkCandidate = (cand) => {
    const key = hostRule === "windows" ? cand.toLowerCase() : cand;
    if (seen.has(key)) return false;
    seen.add(key);
    const low = cand.toLowerCase();
    const why = low.includes("/system32/") || low.includes("/windowsapps/") ? "a launcher" : runProbe(cand);
    tried.push(cand + ": " + why);
    return why === "runs";
  };
  const checkFile = (p) => { try { return fs.statSync(p).isFile(); } catch (_e) { return false; } };
  const gov = process.env.GOV_BASH || "";
  if (gov) {
    const why = runProbe(gov);
    tried.push(gov + ": " + why);
    if (why === "runs") return { found: gov, tried, refusal: "" };
    return { found: "", tried, refusal: "GOV_BASH is set to '" + gov + "' and " + why + ", so nothing after it is tried: " +
      "an override that is set and unusable is refused, never a fall-through" };
  }
  const g = cp.spawnSync("git", ["--exec-path"], { stdio: ["ignore", "pipe", "pipe"], timeout: 20000, windowsHide: true });
  const ex = !g.error && g.status === 0 ? (g.stdout || Buffer.alloc(0)).toString("utf8").trim().replace(/\\/g, "/") : "";
  let found = "";
  if (!ex) {
    tried.push("git --exec-path: did not run");
  } else {
    const cand = ex.replace(/\/+$/, "").split("/").slice(0, -3).join("/") + "/bin/bash.exe";
    if (!checkFile(cand)) tried.push(cand + ": absent");
    else if (checkCandidate(cand)) found = cand;
  }
  for (const d of (process.env.PATH || "").split(path.delimiter)) {
    for (const name of ["bash.exe", "bash"]) {
      const cand = (d.replace(/[/\\]+$/, "") + "/" + name).replace(/\\/g, "/");
      if (d && checkFile(cand) && checkCandidate(cand)) found = found || cand;
    }
  }
  if (found) return { found, tried, refusal: "" };
  return { found: "", tried, refusal: "no bash runs" + (script ? " that can see " + String(script) : "") + ": " +
    tried.join("; ") + "; set GOV_BASH to Git's bash" };
}
// <<< resolve_bash_js

// The bash that can SEE the shim: the one `resolve_bash_js` block above (TOOL-dWitnessedBar-26) run
// with the shim, GOV_BASH first, then Git's own `bin/bash.exe`, then PATH, each candidate RUN and a
// WSL launcher refused under any name, never the bare name (gotcha
// subprocess-resolves-a-different-shell). null where none resolves, which `runShim` turns into its
// PolicyRefusal; `export GOV_BASH=<path>` names one. Found once per process.
let BASH;
function resolveBash() {
  if (BASH === undefined) BASH = scanBash({ script: SHIM }).found || null;
  return BASH;
}

// The shim's outcome: its stdout on exit 0, else a PolicyRefusal. Its own refusal, exit 2 with the
// reader's line, passes that line through; every other outcome names the status, the signal and the
// shim's stderr. Deny by default: a shim that did not run refuses too.
function runShim(top, args) {
  const bash = resolveBash();
  if (!bash) throw new PolicyRefusal(`policy: refused · ${MIRROR_REL}:0 · no bash can see ${SHIM}: GOV_BASH, Git's own bin/bash.exe and each bash on PATH were each run; export GOV_BASH=<path> naming one that can`);
  const r = spawnSync(bash, [SHIM, ...args], { cwd: top, env: ENV, encoding: "utf8", windowsHide: true });
  if (r.status === 0) return r.stdout;
  const err = (r.stderr || "").trim();
  if (r.status === 2 && err.startsWith("policy: refused · ")) throw new PolicyRefusal(err);
  throw new PolicyRefusal(`policy: refused · ${MIRROR_REL}:0 · policy-shim.sh ${args[0]} failed: status ${r.status}, ` +
    `signal ${r.signal || "none"}: ${err || (r.error ? r.error.message : "no stderr")}`);
}

function readLandedRevision(top) {
  return runShim(top, ["landed"]).trim();
}

// -> { doc, policyBlob, catalogueBlob, legacyStale } at the landed revision L: the parsed mirror or
// null (ABSENT), the two blob ids, null where absent, and whether any input of the expected list,
// each name of MIRROR_KIT_INPUTS by the kit's place and then each path of MIRROR_LEGACY_INPUTS, has
// a recorded id differing from L, an input the map does not record differing from every id, or the
// map is absent. A key the map records beyond that list is never read.
function readMirrorAt(top, landed, kitRel) {
  const m = runGit(top, ["cat-file", "blob", `${landed}:${MIRROR_REL}`]);
  let doc = null;
  if (m.status === 0) {
    try {
      doc = JSON.parse(m.stdout);
    } catch (_e) {
      doc = null;
    }
  }
  if (!doc || typeof doc !== "object" || !doc.keys || typeof doc.keys !== "object") doc = null;
  const kit = kitRel ? kitRel + "/" : "";
  const recorded = doc && doc.legacy_blobs && typeof doc.legacy_blobs === "object" ? doc.legacy_blobs : null;
  const legacy = [...MIRROR_KIT_INPUTS.map((n) => kit + n), ...MIRROR_LEGACY_INPUTS];
  // One call for every id: `rev-parse` stops at the first absent path, `--batch-check` says `missing`.
  const ids = runGit(top, ["cat-file", "--batch-check"],
    [POLICY_REL, `${kit}catalogue.toml`, ...legacy].map((p) => `${landed}:${p}\n`).join(""));
  const [policyBlob, catalogueBlob, ...legacyIds] = (ids.stdout || "").split("\n")
    .map((ln) => (/^[0-9a-f]{40,64} blob /.test(ln) ? ln.split(" ")[0] : null));
  // An input the map does not record is `undefined`, which differs from every id, null included.
  const legacyStale = !!doc && (!recorded || legacy.some((p, i) =>
    (Object.prototype.hasOwnProperty.call(recorded, p) ? recorded[p] : undefined) !== (legacyIds[i] || null)));
  return { doc, policyBlob: policyBlob || null, catalogueBlob: catalogueBlob || null, legacyStale };
}

function runReader(top, key) {
  const out = runShim(top, ["get", key]);
  try {
    const hit = JSON.parse(out);
    return { value: hit.value, source: hit.source, reason: hit.reason };
  } catch (_e) {
    throw new PolicyRefusal(`policy: refused · ${MIRROR_REL}:0 · the reader's answer for ${key} is not JSON: ${out.trim()}`);
  }
}

function readPolicy(key, { repo = process.cwd() } = {}) {
  const t = runGit(repo, ["rev-parse", "--show-toplevel"]);
  if (t.status !== 0) throw new PolicyRefusal(`policy: refused · ${MIRROR_REL}:0 · ${repo} is in no git repository`);
  const top = t.stdout.trim();
  // realpath on both sides: git and node may spell one directory differently (an 8.3 name on Windows).
  const kitRel = path.relative(fs.realpathSync.native(top), fs.realpathSync.native(__dirname)).split(path.sep).join("/");
  const landed = readLandedRevision(top);
  const m = readMirrorAt(top, landed, kitRel);
  let failed = "";
  if (!m.doc) failed = "absent";
  else if (m.doc.policy_blob !== m.policyBlob || m.doc.catalogue_blob !== m.catalogueBlob || m.legacyStale) failed = "stale";
  else if (Object.prototype.hasOwnProperty.call(m.doc.keys, key)) {
    const hit = m.doc.keys[key];
    const reason = typeof hit.reason === "string"
      ? hit.reason.split("{rev}").join(`${landed.slice(0, 8)}, the landed revision`) : hit.reason;
    return { value: hit.value, source: hit.source, reason };
  }
  const at = `${failed} at ${landed.slice(0, 8)}`;
  if (failed) {
    const on = runReader(top, "policy-file.on-invalid").value;
    if (on !== "last-valid") throw new PolicyRefusal(`policy: refused · ${MIRROR_REL}:0 · ${at}; policy-file.on-invalid is ${on}`);
  }
  const hit = runReader(top, key);
  return failed ? { ...hit, reason: `mirror ${at}; ${hit.reason}` } : hit;
}

// The value as `policy.py get` prints it: a string as itself, a list one member per line.
// ponytail: JSON keeps no int/float split, so a whole float such as 2.0 prints as 2.
function main(argv) {
  const usage = "usage: node <this kit>/policy-mirror.js get <key> [--repo <dir>] [--explain]";
  let key = null, repo = process.cwd(), explain = false;
  for (let i = 1; i < argv.length; i++) {
    if (argv[i] === "--explain") explain = true;
    else if (argv[i] === "--repo" && i + 1 < argv.length) repo = argv[++i];
    else if (key === null && !argv[i].startsWith("--")) key = argv[i];
    else key = undefined;
  }
  if (argv[0] !== "get" || !key) {
    process.stderr.write(usage + "\n");
    return 2;
  }
  let hit;
  try {
    hit = readPolicy(key, { repo });
  } catch (e) {
    if (!(e instanceof PolicyRefusal)) throw e;
    process.stderr.write(e.message + "\n");
    return 2;
  }
  for (const v of Array.isArray(hit.value) ? hit.value : [hit.value]) {
    process.stdout.write((typeof v === "string" ? v : typeof v === "object" ? JSON.stringify(v) : String(v)) + "\n");
  }
  if (explain) process.stderr.write(`policy: ${key} · ${hit.source} · ${hit.reason}\n`);
  return 0;
}

// POLICY_REL is exported for the hooks kit's write gate, whose policy-file arm denies a tool write to
// this path and names the loop kit's policy_edit.py as the door (TOOL-dDeclaredLoop-2 S10).
module.exports = { readPolicy, PolicyRefusal, readLandedRevision, POLICY_REL };

if (require.main === module) process.exitCode = main(process.argv.slice(2));

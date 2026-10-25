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
//      `.governance/policy.toml`, `<kit>/catalogue.toml` and each path of the mirror's
//      `legacy_blobs` at L, null where absent. A missing mirror, or text that does not parse as a JSON
//      mirror, is ABSENT.
//   4. Every recorded id equals its id at L: the mirror is FRESH, and a key it holds is returned
//      with its recorded source and reason, each `{rev}` the render wrote in the reason filled with
//      `<L8>, the landed revision` (TOOL-dGroundRules-65). A key it does not hold goes to step 6.
//   5. Any id differing, a legacy input's among them, or no `legacy_blobs` at all: the mirror is
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

class PolicyRefusal extends Error {}

function runGit(cwd, args, input) {
  return spawnSync("git", args, { cwd, env: ENV, input, encoding: "utf8", windowsHide: true });
}

// The bash that can SEE the shim, by RUNNING each candidate, never by its place on PATH, in the order
// the policy kit's checker's `resolve_bash` takes: GOV_BASH, then the first `bash` PATH names, then
// Git for Windows' two paths, then the bare name, each kept only when `test -f` on the shim exits 0
// under it. On Windows the bare name reaches the System32 WSL launcher, which cannot open a `C:/`
// path (gotcha subprocess-resolves-a-different-shell). Found once per process.
let BASH;
function resolveBash() {
  if (BASH !== undefined) return BASH;
  const onPath = (ENV.PATH || ENV.Path || "").split(path.delimiter).filter(Boolean)
    .flatMap((d) => [path.join(d, "bash.exe"), path.join(d, "bash")]).filter((p) => fs.existsSync(p));
  const cands = [ENV.GOV_BASH, onPath[0], "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"];
  BASH = null;
  for (const c of [...new Set(cands.filter(Boolean))]) {
    const r = spawnSync(c, ["-c", 'test -f "$1"', "_", SHIM], { env: ENV, windowsHide: true, timeout: 20000 });
    if (r.status === 0) { BASH = c; break; }
  }
  return BASH;
}

// The shim's outcome: its stdout on exit 0, else a PolicyRefusal. Its own refusal, exit 2 with the
// reader's line, passes that line through; every other outcome names the status, the signal and the
// shim's stderr. Deny by default: a shim that did not run refuses too.
function runShim(top, args) {
  const bash = resolveBash();
  if (!bash) throw new PolicyRefusal(`policy: refused · ${MIRROR_REL}:0 · no bash can see ${SHIM}: GOV_BASH, PATH's bash and Git for Windows' two were each run`);
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
// null (ABSENT), the two blob ids, null where absent, and whether any `legacy_blobs` entry, or its
// absence, differs from L.
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
  const legacy = doc && doc.legacy_blobs && typeof doc.legacy_blobs === "object" ? Object.keys(doc.legacy_blobs) : [];
  // One call for every id: `rev-parse` stops at the first absent path, `--batch-check` says `missing`.
  const ids = runGit(top, ["cat-file", "--batch-check"],
    [POLICY_REL, `${kitRel ? kitRel + "/" : ""}catalogue.toml`, ...legacy].map((p) => `${landed}:${p}\n`).join(""));
  const [policyBlob, catalogueBlob, ...legacyIds] = (ids.stdout || "").split("\n")
    .map((ln) => (/^[0-9a-f]{40,64} blob /.test(ln) ? ln.split(" ")[0] : null));
  const legacyStale = !!doc && (!doc.legacy_blobs || typeof doc.legacy_blobs !== "object"
    || legacy.some((p, i) => doc.legacy_blobs[p] !== (legacyIds[i] || null)));
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

module.exports = { readPolicy, PolicyRefusal };

if (require.main === module) process.exitCode = main(process.argv.slice(2));

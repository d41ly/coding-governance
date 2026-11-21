#!/usr/bin/env node
// resolve_bash.js — the one bash a gov JavaScript file runs, found by RUNNING each candidate
// (TOOL-dWitnessedBar-26). The canonical `resolve_bash_js` block, the twin of `resolve_bash.py`'s
// `resolve_bash_py` beside it: one rule, one truth table, which
// `<prefix>/lib/resolve-python.test.sh`'s section 2j runs both over. `<prefix>/lib/` ships nothing, so
// a hook carries the block INLINE, byte-identical, and keeps its own name and failure contract as a
// thin adapter over the `{found, tried, refusal}` the block returns; the parity table reds a drift.
//
//   node <prefix>/lib/resolve_bash.js [--script <path>] [--host windows|posix]
//
// prints one `tried: <candidate>: <why>` line per candidate, then `bash: <path>` and exit 0, or the
// refusal line and exit 2.
"use strict";

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

function main(argv) {
  const opts = { script: "", host: "" };
  for (let i = 0; i < argv.length; i++) {
    const k = argv[i].replace(/^--/, "");
    if (!(k in opts) || i + 1 >= argv.length) {
      process.stderr.write("usage: node resolve_bash.js [--script <path>] [--host windows|posix]\n");
      return 2;
    }
    opts[k] = argv[++i];
  }
  if (opts.host && opts.host !== "windows" && opts.host !== "posix") {
    process.stderr.write("resolve_bash.js: --host is windows or posix, not " + opts.host + "\n");
    return 2;
  }
  const { found, tried, refusal } = scanBash(opts);
  const out = tried.map((t) => "tried: " + t);
  out.push(found ? "bash: " + found : "refused: " + refusal);
  process.stdout.write(out.join("\n") + "\n");
  return found ? 0 : 2;
}

module.exports = { scanBash, wrongShellAt };

if (require.main === module) process.exitCode = main(process.argv.slice(2));

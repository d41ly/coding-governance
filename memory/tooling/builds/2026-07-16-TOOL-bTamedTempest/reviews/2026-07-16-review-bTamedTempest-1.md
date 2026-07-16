# Review 1 — pre-code adversarial review of spec rev-1 (wf_d878c8a9-bb3)

3 primed finder lenses (truthfulness · house-integration · portability) + 1 batched skeptic,
boundedParallel ≤3+1. 15 raw findings → **11 confirmed, 4 refuted**. All 11 folded into spec rev-2.

## Confirmed (folded)

1. MEDIUM · §4 claimed `session_timeout` "bounds a wedged single test whose per-test timer never
   armed" — mechanically FALSE. pytest-timeout compares expiry only AFTER a test's
   `pytest_runtest_protocol` completes; a wedged test never reaches the check. `session_timeout`
   only turns a slow-but-COMPLETING run red; the per-test `timeout` is the ONLY hang bound.
   (Also corrects the upstream inCMS pyproject comment + ARCH-eVigilantCanary-1 clause this was
   ported from — erratum owed upstream.)
2. HIGH · crashprobe's import-time `faulthandler.enable(file=<log>)` is silently superseded:
   pytest's builtin faulthandler plugin calls `enable(file=dup(stderr))` at `pytest_configure`,
   and `enable` is process-global last-wins. Fix: probe re-arms in `pytest_configure`
   (`@pytest.hookimpl(trylast=True)`). `faulthandler_timeout` is unaffected either way — it uses
   `dump_traceback_later(file=...)` per call, independent of `enable`.
3. HIGH · self-test was static-only (`py_compile` parses, never imports) while §5 claimed
   "a syntax/import regression cannot ship". Fix: additionally import-execute `crashprobe.py`
   under bare stdlib with `CRASHPROBE_DIR` pointed at a temp dir (gate-platform import proof);
   the seam snippet stays compile-only (needs aiosqlite) — stated honestly.
4. MEDIUM · `-p crashprobe` with the file merely copied into the rootdir does NOT load under the
   pytest console script (empirically verified). Supported invocations documented instead:
   `PYTHONPATH` env, `pythonpath = ["."]` ini, or `python -m pytest`.
5. MEDIUM · kit version marker homed in the one artifact adopters are told to DELETE
   (crashprobe.py) — defeats deployer version detection in target repos (aKitHardener
   convention). Fix: `gov:kit pytest-parallel-guardrails@X.Y` doc-markers in the KEPT artifacts
   (pyproject snippet + seam snippet + test template); `check-kit-versions.sh` asserts the
   constant/marker pair agrees (memory-tree precedent).
6. MEDIUM · `test_aiosqlite_worker_resilience.template.py` matches pytest's default `test_*.py`
   glob (fnmatch `*` spans dots) → a bare pytest crawl over a vendored kit dir collects it and
   ERRORS. Renamed `aiosqlite_worker_resilience.test-template.py`; README says "rename to
   `test_*.py` when copying into your suite".
7. MEDIUM · S3's source artifact (session crashprobe.py) no longer exists on disk — §1's
   "proven" wording overreached for S3. Reworded: the probe is a reconstruction of the session
   tool whose technique + outputs are recorded in inCMS ARCH-eVigilantCanary-1; S2/S4/S5 sources
   verified present in inCMS.
8. LOW · §4 dropped the "Windows-only" qualifier on the fd 2 devnull redirection (execnet
   redirects fd 0/1 everywhere, fd 2 only under `os.name == "nt"`). Qualifier restored.
9. LOW · §5 "import regression cannot ship" overclaim — superseded by fix 3's honest wording.
10. LOW · AGENTS.md has TWO lists to update: the kit list AND the gate-suite "kit self-tests"
    enumeration; S6 covered only the first. Both now in scope.
11. LOW · the self-test's numeric knob comparison is CRLF-fragile on `text=auto` Windows
    checkouts (`300\r`). Self-test strips `\r` before comparing (check-template-size.sh
    precedent).

## Refuted (no action)

- §1 provenance figures "not present in cited records" — they are (journal + records).
- Constant name "drifts from KIT_<NAME>_VERSION scheme" — no such rigid scheme ratified.
- Template-test adopter-edit seam "layout-dependent" — one documented edit line is the design.
- §4/§8 warn-vs-fail "contradiction" — §4 states the recommendation §8 carries; template-legal.

# Profiling the gate legs with `measure_legs.py`

**What it is.** The merge bar runs a leg and records how long it took. The gate profiler runs every
leg of the manifest itself, with no knob, ceiling, guard, reuse or retry, and records what each leg
did: how many processes it started, its CPU, memory and I/O, the cost of each spawn, and the load the
reading was taken under. Use it to argue a ceiling, a width or a spawn claim from a measurement. It
runs on Windows only and refuses anywhere else.

The tool is `<prefix>/run-gates/measure_legs.py`, which is `tools/run-gates/measure_legs.py` in this
repository. The run-gates kit README's section "The gate profiler" is the full reference.

## How to use it

- **One leg at a time:** `python tools/run-gates/measure_legs.py --serial`. Each leg starts when the
  previous one ends, as the bar's serial run would. A serial reading is the one to argue a ceiling
  from.
- **Under a load cap:** `python tools/run-gates/measure_legs.py --concurrent`. The next leg is
  admitted only on a fresh sample at or under 80% CPU and 90% memory, or when no leg of the run is
  running. Use it for width profiles.
- **Another manifest or record root:** add `--legs <path>` or `--out <root>`.
- **Census and stall settings:** `--census-every <s>` (default 5), `--stall-window <s>` (default 300)
  and `--stall-cpu <s>` (default 1.0). A leg that does no work and writes nothing for a whole window
  prints `STALLED`. Nothing is ever killed: a leg that never ends keeps the run open.
- **Start it outside any bar.** A profile started inside a bar queues each leg's own bars behind
  that bar.

## What it writes

Every run writes one directory, `<git-dir>/gate-profile/<run id>/`. Nothing prunes it.

- `envelope.json`: the run. It holds the scrubbed variable names and their rules, the environment
  digests and tool versions, `substitutions`, and the scratch dir in both spellings, `scratch` as
  Python opens it and `scratch_posix` as the legs see it. Its `raw_recovered` names each raw capture
  this run recovered from a dead run, described below.
- `legs.tsv`: one row per leg, the table to sort. Per-leg detail is in `<i>.json`, and the redacted
  output is in `<i>.log`. A leg whose process could not be put in its job or started reads `fail`
  with rc 1, and its `<i>.json` carries `launch_error`, `launch: <call> <winerror>`. Its process is
  stopped before it runs anything, and the run goes on.
- `host.tsv` and `census.tsv`: the load timeline and each process census.

A run that was killed or crashed can leave a leg's raw output, unredacted, in its scratch dir. Each
run writes `owner.json` into its own scratch dir, and a later run sweeps a dead run's raw captures:
once it has proved that run's process gone, by its pid and creation time, it redacts each capture
into `<i>.log.recovered` in that run's record dir, or under `recovered/` in its own record when that
dir is gone, and deletes the raw file. A scratch dir whose owner might still be running is left alone.

Per leg, `procs_total` is the job's exact process count, and `unseen` is how many of those the census
never saw. `ts_wait_s` is the time the leg's own bars waited in the host turnstile queue, and
`work_s` is the rest of its wall time. `foreign` counts gate work from someone else beside the leg.

## Substituted runs are not the bar's

A Microsoft Store App Execution Alias, such as the `python3` in `WindowsApps`, starts every process
outside the leg's job, so its readings would count one process per leg. When PYBIN is such an alias,
the profiler runs the interpreter the alias starts instead and sets `GOV_PYTHON` to it for the legs.
The start of the run prints `measure-legs: SUBSTITUTED <launcher> <alias> -> <resolved>`, and the
envelope's `substitutions` lists each one. Those readings leave out the alias's own process per
launch, so they are **not exactly the bar's**.

## Carrying a reading into the ceilings

Only a serial `ok` reading whose `.leg` row has `0` as its eighth field is uncontended. Carry it with
`python tools/run-gates/derive-ceilings.py --write --observed '<leg>=<s>' --how 'measure_legs <run id>'`.
If the run's `substitutions` is not empty, write `substituted` into the `--how` text as well.

## Example

```bash
python tools/run-gates/measure_legs.py --serial --legs my-legs.json --census-every 1
sort -t$'\t' -k5,5nr "$(git rev-parse --absolute-git-dir)/gate-profile/<run id>/legs.tsv" | head
```

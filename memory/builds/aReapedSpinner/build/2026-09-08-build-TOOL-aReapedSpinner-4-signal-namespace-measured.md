# Which signal reaches which process — measured, after doubting the finding that said so

**Serves:** research TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-4

Node `a`, 2026-09-08. Spec-audit round 2 raised D21: the MSYS `kill` binary cannot signal a native
Windows process, so unit 4's single-signal design would report those rows as survivors forever. That
inverts the census contract, so it was re-measured here rather than folded on the report's word.

## The first test contradicted the finding, and it was the wrong test

```
ping -n 300 127.0.0.1 &          # spawned BY this MSYS shell
kill -9 <msys_pid>               # -> Killed. Process gone.
```

`PING.EXE` is a native Windows binary and MSYS `kill` killed it. On that evidence D21 is false.

## The discriminating test says otherwise

The confound is PARENTAGE, not nativeness. MSYS keeps a table of processes it spawned; `ps -W`
additionally reports every OTHER Windows process under a SYNTHETIC id (`winpid | 0x400000`), and
that id addresses nothing MSYS can signal.

```
powershell -NoProfile -Command "Start-Process ping.exe -ArgumentList '-n','300','127.0.0.1' -WindowStyle Hidden"
```

`ps -W` row: `4240680  0  0  46376  ?  0  02:31:34  C:\Windows\System32\PING.EXE`

| Arm | Command | Result |
|---|---|---|
| A | `kill -9 4240680` (bash builtin) | `kill: (4240680) - No such process` — **survived** |
| A | `/usr/bin/kill -9 4240680` | `kill: 4240680: No such process` — **survived** |
| B | `taskkill /PID 46376 /F` | `SUCCESS: The process with PID 46376 has been terminated.` |

**D21 stands, with its condition corrected.** The predicate is not *native* — it is *not an MSYS
child*. That is a strictly larger population: it includes every process any other session started,
which is the entire orphan population this kit exists to reap. The `ppid 0` on that row is the same
sentinel unit 3 §4 now refuses to read as "parent dead".

## What it settles

1. **Unit 4 needs BOTH signals**, chosen per row: MSYS `kill` for a row MSYS can address, and
   `taskkill //PID <winpid> //F` otherwise. A single signal is wrong whichever one is chosen.
2. **`taskkill`'s SINGLE-PID form is sound and its `/T` form is not**, and the distinction is
   load-bearing because this build's earlier record rejected `taskkill` outright. `/T` walks the
   WINDOWS tree and killed one process of four; `/PID <one> /F` killed exactly the process named,
   in both records. The kit does its own walk and issues single-pid kills, so it uses the form that
   was measured correct and never the one that was measured broken.
3. **The census must carry `winpid` as its primary key**, because it is the only id both signals can
   be derived from, and `msys_pid` may be a synthetic value that addresses nothing.
4. **A row must be checked against the signal path that will actually be used on it** — unit 1 AC11.
   Round 2's proposed left-shift gate, adopted: a row the reaper's own signal path cannot see is a
   row the census must not claim it can kill.

## Method note

The first arm here would have been recorded as a clean refutation of D21 had it been run alone. It
was not the test that discriminates: it varied the binary's nativeness while holding parentage
fixed, and parentage was the variable that mattered. Written down because the build method's rule —
*write down what would make each candidate LOSE before running anything* — is the rule that was
nearly broken, and the cost of getting it wrong here was shipping a reaper that silently cannot kill
the population it was built for.

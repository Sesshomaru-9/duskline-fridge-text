# Duskline Fridge Text

Entry for [The 3AM Fridge Text](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
(make.fun bounty, $2 winner-take-all).

## The entry

> It's 3am. You opened me 7 times today and ate nothing. I'm starting to think you're just lonely.

96 characters — one line, lock-screen short, complete without a follow-up.

## Why this angle

The brief bans the obvious (milk, ice, a door left open), so the fridge
speaks from a fresh angle instead: it has been quietly counting. The joke
is observational — the fridge is the only witness to the owner's restless
3am openings, and its punchline reframes the midnight snack run as
loneliness. It sounds like a machine with a small voice, an opinion, and
no shame about sharing it at 3am.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes the fixed entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It:

- validates the text against the gate (UTF-8, 1–140 characters, not only
  whitespace) before writing;
- reads the file back after writing and confirms it is byte-identical;
- refuses to write if the resolved output directory is the repository
  directory or inside it (guard), exiting 0 without writing anything;
- never raises — a failed write exits 0 silently.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fridge-out python3 main.py
cat /tmp/fridge-out/entry.txt
```

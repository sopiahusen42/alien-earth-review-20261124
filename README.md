# alien-earth-review-20261124

[![make.fun · Alien Field Notes: The Two Day Earth Review](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/sopiahusen42/alien-earth-review-20261124/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/sopiahusen42/alien-earth-review-20261124/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An alien tourist's two-star review of Earth: not poisonous enough to be interesting, and blanketed in other people's opinions. This is the entry for make.fun's "Alien Field Notes: The Two Day Earth Review" bounty.

## The line

> Two stars. Nothing here is poisonous enough to be interesting and everything is covered in a thin film of someone else's opinion.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the review in the `ENTRY` constant. Before writing, `validate_entry(text)` checks that it is a `str`, not blank, 1 to 200 Unicode code points, free of `\n` and `\r` so it stays one line, and identical to its stripped form. On failure the program prints one line to stderr and exits 1. On success it creates the output directory if needed (default `/output`, overridable with `MAKEFUN_OUTPUT_DIR`), writes `ENTRY` plus a single newline as UTF-8 with `newline=""`, reads the bytes back to confirm they match, prints nothing and exits 0. It uses only the standard library, reads no clock and no randomness, so it produces identical bytes on every run.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp

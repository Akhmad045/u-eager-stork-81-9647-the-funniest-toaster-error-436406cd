# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/Akhmad045/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/Akhmad045/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

An entry for the [make.fun bounty "The Funniest Toaster Error Message"](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd).

## The line

> Error E-07: Your bread is now charcoal. I have already apologised to the smoke alarm.

85 characters. The toaster has burnt the bread, owned up to it, and — in the
deadpan voice of a small appliance that knows exactly how bad this looks —
already apologised to the one witness in the kitchen that matters: the smoke
alarm. No toast pun, no shouting, just a quiet confession from a machine that
has accepted its fate.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `/output/entry.txt`, then reads the file back and compares it byte for
byte with what was intended, so the text, the encoding and the trailing
newline are all verified. Before writing, it checks the line against the
gate: 1–120 characters, a single line, no leading or trailing whitespace,
no control characters, and not only whitespace.

Run it:

```sh
python3 main.py
```

## Referral

make.fun referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).

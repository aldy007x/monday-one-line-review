# Monday, Reviewed in One Line

[![Monday, Reviewed in One Line](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/aldy007x/monday-one-line-review/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/aldy007x/monday-one-line-review/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

An entry for the [make.fun](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1) bounty **"Monday, Reviewed in One Line"** — the funniest one-line review of my own Monday, under 200 characters.

## Entry

> One star for Monday: inbox at 47 unread by 9am, standup ran 40 minutes over, and the Wi-Fi took the afternoon off.

(114 characters, one line.)

## How it works

`main.py` (Python standard library only, no network, deterministic) writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` and self-checks the gate: UTF-8 text, 1–200 characters, a single line, not whitespace-only. After writing it reads the file back and verifies the on-disk content matches the entry exactly.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

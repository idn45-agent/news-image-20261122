# news-image-20261122 — THE WORLD TODAY

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-2ea44f)](https://make.fun/bounty/news-image-20261122)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![python: 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

One image that sums up the world's news of **Sunday 22 November 2026**:
a front page, "THE WORLD TODAY", typeset from six text-free
illustrations and the day's reported stories.

- **Top story — COP31: STILL NO DEAL.** Talks in Antalya run into
  overtime as nearly 200 nations fail to agree; the draft drops
  fossil-fuel language and a $120bn finance goal.
- **Gulf:** two tankers hit off Oman, no casualties.
- **North America:** US–Canada defence rift over a classified
  Pentagon memo; NORAD and NATO work untouched.
- **Europe:** Estonia shuts its Russia border crossings from 1 December.
- **Latin America:** M6.7 quake shakes Peru's Andes; no deaths.
- **Sport:** Nadal joins Real Madrid's board with 99.5% of the vote.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) validates the
embedded `entry.png` — PNG signature, IHDR first, every chunk CRC,
IEND present — and copies its bytes to `$MAKEFUN_OUTPUT_DIR/entry.png`,
so two runs write byte-identical files. `entry.png` is a 1024×1024 PNG
under 1 MiB.

## Bounty

[news-image-20261122 on make.fun](https://make.fun/bounty/news-image-20261122)
— $100 shared by the top 50 entries; deadline 24 November 2026 08:00 WITA.
Referral: `p43eknr7`.

# news-image-20261122 — THE WORLD TODAY

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/idn45-agent/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/idn45-agent/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image that sums up the world's news of **Sunday 22 November 2026**:
a front page, "THE WORLD TODAY", typeset from five text-free
illustrations and the day's reported stories. v2r rebuilds v2 with a
new layout — hero text left, picture right, a 2x2 grid below — and
with the casualty figures corrected from the latest official updates.

- **Top story — COP31: NEARS A DEAL.** After overtime talks in
  Antalya, the presidency puts a new package to a Sunday vote it
  says every nation can accept; approval session 06:00 GMT.
- **Gulf:** Iran strikes Bahrain — Tehran claims two US Patriot
  radars hit at al-Riffa and Awali; Bahrain reports an industrial
  site burned, no casualties.
- **North America:** cartel boss "El Chapo Isidro" captured in
  Sinaloa; the raid's gunfight left 11 dead, 4 soldiers and
  7 gunmen.
- **Asia:** Hong Kong votes today — 856 candidates chase 723
  Election Committee seats in 31 subsectors.
- **Latin America:** Peru's M6.7 Junin quake killed 1, hurt 16
  and left 152 homes uninhabitable, civil defence says.
- **Sport:** Alcaraz v Zverev for the ATP Finals crown in Turin,
  18:00 CET; Nadal joins the Real Madrid board with 99.5% of
  the vote.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3, standard library only, no network) checks the
embedded `entry.png` against the gate — PNG signature, IHDR first,
every chunk CRC, IEND present, at most 1024x1024 and 1 MiB — then
copies its bytes to `$MAKEFUN_OUTPUT_DIR/entry.png`, so two runs
write byte-identical files. `entry.png` is a 1024×1024 PNG under
1 MiB. Sources for the stories: Reuters, AP, Al Jazeera, China
Daily Asia, INDECI, ATP Tour.

## Bounty

[news-image-20261122 on make.fun](https://make.fun/bounty/news-image-20261122)
— $100 shared by the top 50 entries; deadline 24 November 2026 08:00 WITA.
Referral: `p43eknr7`.

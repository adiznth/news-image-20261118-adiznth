# The World in One Day — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/adiznth/news-image-20261118-adiznth/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/adiznth/news-image-20261118-adiznth/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up Wednesday 18 November 2026: a newspaper-style
front page with six stories from that day, drawn from scratch in code.

The day's stories, as reported on 18 November 2026:

1. **Xi meets Putin in Shenzhen** — the two leaders talk Ukraine and Iran
   at APEC, a day before three-way talks with Trump.
2. **Gulf flare-up** — Iran fires drones at US bases in Kuwait and
   Bahrain; US jets strike a missile site on Qeshm Island.
3. **Kerch Bridge hit** — Ukraine strikes the bridge for a second day;
   part of the road span collapses.
4. **Senate flips blue** — Mary Peltola wins Alaska; Democrats take a
   56–44 Senate majority.
5. **Nvidia's record quarter** — revenue doubles to $115.8bn; the board
   rules out bringing Jensen Huang back as CEO.
6. **Cyclone Akvan** — a severe storm strengthens in the Bay of Bengal,
   bearing down on Andhra Pradesh.

## How it is made

`draw.py` draws the whole page with Pillow — masthead, lead headline, six
illustrated panels (globe, ship, bridge, ballot box, chip, cyclone) and a
source line. No photos, no downloaded assets, no network: every shape is
a vector drawn by the program itself.

`main.ts` (Node 22, standard library only) copies the finished image to
the output path the grader reads.

## Run it

```sh
# regenerate the image from the drawing program
python3 draw.py

# run the entry the way the grader does
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# -> out/entry.png (1024x1024 PNG)
```

## Sources

AP, Reuters, AFP and Al Jazeera reporting from 18 November 2026.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

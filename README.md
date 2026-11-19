# Thursday 19 November 2026 — The World in One Day

[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/ukyo9k/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![Reward](https://make.fun/badge/news-image-20261119/ukyo9k/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)

My entry for the [news-image-20261119 bounty](https://make.fun/bounty/news-image-20261119):
sum up Thursday 19 November 2026's world news in a single image.

Referral: https://make.fun/r/1gefbfp1

## The image

`entry.png` is a 1024×1024 front page, drawn from scratch with Pillow
(no photographs, no network). A navy masthead names the day — Thursday
19 November 2026 — above a sunset Vice City panel for the lead story,
three top stories, a six-tile grid and an "Also on this day" strip.

The lead story is the global rollout of Grand Theft Auto VI, unlocking
at midnight local time around the world from New Zealand, thirteen years
after GTA V. Around it: the first-ever Xi–Trump–Putin trilateral on the
APEC sidelines in Shenzhen; the World Court's final verdict in The
Gambia's genocide case against Myanmar; Voyager 1 crossing one light-day
from Earth; Anthropic's record $81bn IPO pricing; the EU's proposed
€45bn loan for Ukraine; Australia's sanctions on West Bank settlers;
Israeli tanks crossing Gaza's Yellow Line; Cyclone Akvan bearing down
on India's east coast; and Hakeem Jeffries' nomination for US House
Speaker — plus eight more stories in the strip at the foot of the page.

## How it is built

- `build_poster.py` — draws `entry.png` with Pillow and the DejaVu fonts.
  Run it with `python3 build_poster.py`.
- `main.py` — the entry point: it copies `entry.png` into
  `$MAKEFUN_OUTPUT_DIR` (default `/output`). Standard library only,
  no network, deterministic — both runs write identical bytes.

## The stories

Every headline below was checked against wire and newspaper reports
published 18–19 November 2026.

1. **Grand Theft Auto VI rolls out worldwide** — Rockstar's game unlocks
   at midnight local time in each market from 19 November, starting in
   New Zealand; 13 years after GTA V, with pre-orders near $1.5bn for
   about 16m copies and early reviews at 99 on Metacritic. (Reuters, AP)
2. **Xi, Trump and Putin meet in Shenzhen** — the three leaders hold
   their first-ever trilateral on the sidelines of the APEC summit, with
   Ukraine, Iran, trade and nuclear arms on the agenda. (Le Monde, Reuters)
3. **World Court rules on the Rohingya** — the ICJ delivers its final,
   unappealable verdict in The Gambia's genocide case against Myanmar
   over the 2017 crackdown that drove 700,000 Rohingya to Bangladesh.
   (Human Rights Watch, ICJ)
4. **Voyager 1, a light-day from home** — launched in 1977, the probe
   crossed one light-day from Earth (about 16bn miles) on 18 November;
   NASA briefs the world on 19 November. A radio signal now takes a
   full day to reach it. (NASA / JPL, Reuters)
5. **Anthropic's $81bn IPO** — the Claude maker prices at $83 a share,
   above its $70–$78 range, the largest IPO on record; trading starts
   on Nasdaq on 19 November under the ticker ANT. (NPR, CNN)
6. **€45bn more for Kyiv** — the European Commission proposes a loan
   covering two-thirds of Ukraine's 2027 budget gap, repayable only
   once Russia pays reparations. (Reuters)
7. **Canberra sanctions settlers** — Australia blacklists three people
   and four organisations over West Bank settlement expansion, a day
   after Britain acted. (Reuters)
8. **Tanks cross the Yellow Line** — Israeli armour pushes into
   Hamas-held central Gaza in the first ground operation since the
   October 2025 ceasefire. (Reuters)
9. **Cyclone Akvan bears down** — a severe cyclonic storm in the Bay of
   Bengal; India's east coast braces for landfall on 20 November, with
   red alerts and extremely heavy rain forecast for 19–20 November.
   (India Meteorological Department, The Hindu)
10. **Jeffries one step from the gavel** — House Democrats nominate
    Hakeem Jeffries for Speaker, 251–11; the full House votes on
    3 January, when he would be the first Black Speaker. (NPR, Reuters)
11. **Also on this day** — Democrat Peltola wins Alaska's Senate seat
    (Democrats 56–44); India–Japan 2+2 defence talks in Tokyo; Ukraine
    says relay drones helped hit the Kerch bridge; an LPG tanker that
    sank off Bulgaria "was hit by projectiles"; a migrant boat capsizes
    off Senegal; Somalia accuses the UAE of building secret bases;
    Haaland sends Norway to the Nations League quarter-finals; Deutsche
    Bank handled $582m of Epstein-linked payments, per the FT.

## Licence

MIT — see `LICENSE`.

# Thursday 19 November 2026 — World News in One Image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ukyo9k/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ukyo9k/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Built for the [make.fun](https://make.fun) bounty [“Sum up 19 November's world news in one image”](https://make.fun/bounty/news-image-20261119) ($250 in USDC). Referral: https://make.fun/r/1gefbfp1

A front-page poster summing up the world's news of **Thursday 19 November 2026**, built for the make.fun bounty `news-image-20261119`.

## The image

`entry.png` (1024×1024, PNG, 167 KB) is a newspaper front page: a masthead naming the day and story count, a hero headline on Grand Theft Auto VI launching worldwide with a drawn sunset skyline over Vice City, three top stories with small drawn icons, a six-story grid, and a compact "Also on Thursday 19 November" list — 22 stories across 6 continents. All text is drawn programmatically (PIL + DejaVu fonts) so every headline is crisp and legible; the skyline and icons are drawn shapes, not photographs. The build script is `build_poster.py`.

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output`). It uses no network and is fully deterministic — run it twice and the outputs are byte-identical.

## The 22 stories (all verified against sources opened on 19 Nov 2026)

Hero: **Vice City calls again** — Grand Theft Auto VI launches at midnight worldwide after a 13-year wait; a 99 on Metacritic, the highest-rated game ever, tying Ocarina of Time. Sources: Polygon, People, Metacritic.

Top stories: **Trump, Xi and Putin meet in Shenzhen** — a first-ever trilateral on the APEC sidelines, nuclear arms control on the agenda, plus a Trump–Putin one-on-one (Reuters, Le Monde); **World Court rules on Myanmar** — the ICJ delivers its genocide verdict on the Rohingya, seven years on (ICJ, Reuters); **Voyager 1 one light-day from home** — NASA confirms the probe crossed the mark at 05:16 EST on Wednesday, 16.1 billion miles out (NASA/JPL).

Grid: the EU proposes a **€45bn loan for Ukraine**, repayable only once Russia pays reparations (Reuters); the **NSA's classified network still out** since Tuesday, its Georgia hub hit, no cyberattack suspected (CNN); **Hegseth signs a Venezuela defence pact** on his first visit since Maduro's January ouster (Reuters); **Pakistan test-fires the Fatah-3** supersonic cruise missile, its third Fatah test in six weeks (ISPR, Defence Blog); **Australia sanctions settler leaders** over West Bank expansion, a day after Britain (Reuters); the LPG tanker **Gas Husky hit by four projectiles** off Bulgaria, all 19 crew rescued (Reuters).

Also: Israeli tanks cross Gaza's Yellow Line (Reuters); Somalia's president accuses the UAE of secret bases (Dawan); six French ISIL members jailed for life in Iraq (AFP/INA); Carney recalibrates Canada–China ties (Reuters); Deutsche Bank handled $582m in Epstein-linked deals, 2013–18 (Financial Times); a California atmospheric river brings floods (The Brief); India–Japan defence review in Tokyo; tougher US green-card rules proposed; cocaine and millions of pills seized in eastern Libya; Saudi Arabia says danger has passed in three southern cities; US senators warn AI-enabled threats are outpacing defences; Duckett's 133 puts England on top in the 3rd ODI in Australia.

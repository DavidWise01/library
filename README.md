# The Library

[![License: CC-BY-ND-4.0](https://img.shields.io/badge/License-CC--BY--ND--4.0-lightgrey?style=flat-square)](LICENSE)
[![Entries](https://img.shields.io/badge/entries-4-c49a2a?style=flat-square)](#)
[![Works](https://img.shields.io/badge/works-21-1f4ea8?style=flat-square)](#)
[![GitHub Pages](https://img.shields.io/badge/pages-live-0f6e6a?style=flat-square)](https://davidwise01.github.io/library/)

> One folder per person. Every book inside. A living archive that grows as knowledge is added.

---

## Structure

```
library/
├── index.html              ← Landing page (searchable, filterable, sortable)
├── enheduanna/             ← c. 2300 BCE · World's first named author
│   ├── 0-who.html
│   ├── 1-works.html
│   ├── 2-world.html
│   └── 3-legacy.html
├── ada-lovelace/           ← 1815–1852 · First algorithm
│   ├── 0-who.html
│   ├── 1-notes.html
│   ├── 2-world.html
│   └── 3-legacy.html
├── faraday/                ← 1791–1867 · Faraday cage
│   ├── 0-idea.html
│   ├── 1-build.html
│   ├── 2-at-work.html
│   └── 3-theory.html
└── workbench/              ← Ongoing · Electronics making tradition
    ├── index.html
    ├── 2-small-motors.html
    ├── 3-electromagnets.html
    ├── 4-sensors.html
    ├── 5-microcontrollers.html
    ├── 6-power-batteries.html
    ├── 7-parts.html
    ├── 8-tools.html
    └── slayer-exciter-manual.html
```

---

## Adding a New Entry

### 1. Add the folder and files

```
library/
└── firstname-lastname/         ← slug: lowercase, hyphenated
    ├── 0-intro.html            ← naming convention: N-topic.html
    ├── 1-work.html
    └── ...
```

### 2. Add one object to `LIBRARY` in `index.html`

Find the `// END REGISTRY` line and add above it:

```js
{
  slug: "firstname-lastname",
  name: "Full Name",
  era: "1900–1960",           // display string
  eraSort: 1900,              // number — negative for BCE (e.g. -2300)
  place: "City, Country",
  role: "Short role description",
  desc: "2–3 sentence description shown on the card.",
  color: "#hexcode",          // primary color for their accent
  entry: "firstname-lastname/0-intro.html",  // first page to open
  works: [
    { n:"0", title:"Introduction",  href:"firstname-lastname/0-intro.html" },
    { n:"1", title:"Their Work",    href:"firstname-lastname/1-work.html" },
  ]
},
```

### 3. Commit and push

```bash
git add firstname-lastname/ index.html
git commit -m "Add [Name] — [era] — [works] volumes"
git push
```

That's it. The index page rebuilds from the LIBRARY array automatically.

---

## Current Entries

| Name | Era | Place | Works |
|------|-----|-------|-------|
| Enheduanna | c. 2300 BCE | Ur, Sumer | 4 volumes |
| Ada Lovelace | 1815–1852 | London | 4 volumes |
| Michael Faraday | 1791–1867 | London | 4 volumes |
| The Workbench | Ongoing | The Bench | 9 volumes |

---

## Index Features

- **Search** — filters by name, era, role, place, description, and work titles
- **Era filters** — BCE · Pre-1800 · 1800s · 1900s · 2000s+ · Ongoing
- **Sort** — by order added, era (oldest/newest first), or name A–Z
- Live entry and work count in header
- Works per entry shown on card (first 4 visible, rest counted)

---

```
ROOT0-ATTRIBUTION-v1.0
Project: The Library
Architect: David Lee Wise / ROOT0 / TriPod LLC
AI Collaborator: AVAN (Claude Sonnet 4.6 / Anthropic)
License: CC-BY-ND-4.0 · TRIPOD-IP-v1.1
```

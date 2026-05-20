# Changelog

A record of all changes made to get the repository into its current state.

## Structure

```
lego-spike-mentorship/
├── README.md              ← Clean repo landing (links to Pages site)
├── CHANGELOG.md
├── index.md               ← Redirect to docs/
├── Files.md               ← Complete file index
├── _config.yml            ← Jekyll configuration
├── _layouts/              ← Jekyll theme layouts
├── .gitignore
├── 2024-2025/             ← Year 1 content
│   ├── line-follower/     ← Line-follower project files
│   │   ├── README.md      ← Jekyll page with nomarkdown video
│   │   ├── Line_Following.llsp3
│   │   ├── Line_Following_mid1.llsp3
│   │   └── videos/
│   ├── project-car/       ← RC car project files
│   │   ├── README.md      ← Jekyll page with nomarkdown videos
│   │   ├── car_devine.py
│   │   ├── images/
│   │   ├── videos/
│   │   └── reference/
│   └── README.md
├── 2025-2026/             ← Year 2 content
│   ├── README.md          ← Jekyll page with nomarkdown videos
│   ├── DriveBase_1.py
│   ├── driving-base-gripper/
│   │   ├── images/
│   │   └── videos/
│   ├── showcase/
│   │   └── images/
│   └── xbox_1.png
└── docs/                  ← GitHub Pages source (set main/docs in repo settings)
    └── index.md           ← Homepage with embedded videos, images, and project links
```

## Changes Made

### 1. Moved Pages source to `docs/`
All Pages content lives in `docs/index.md`. The repo root is kept clean for GitHub.com visitors.

### 2. Root `README.md` → clean redirect
The root README is a lightweight landing page with a link to the Pages site. No embedded media — just a clear call to action for GitHub.com visitors.

### 3. `docs/index.md` → Pages homepage
The full project overview (with embedded videos, images, and project links) lives here. This is what visitors see at `gordonoboh.github.io/lego-spike-prime-robotics-mentorship/`.

### 4. Sub-project READMEs → Jekyll pages with nomarkdown wrappers
Each sub-project README (`2024-2025/line-follower/README.md`, `2024-2025/project-car/README.md`, `2025-2026/README.md`) got:
- **Jekyll frontmatter** (`--- layout: default title: ... ---`) so Pages renders them as HTML
- **`{::nomarkdown}`** wrappers around `<video>` tags so Jekyll doesn't strip them

### 5. Jekyll configuration
`_config.yml` and `_layouts/default.html` provide the theme and layout for Pages rendering.

## Key Settings

- **GitHub Pages source**: `main /docs` (set in repo Settings > Pages)
- **No file duplication**: Everything lives in one place

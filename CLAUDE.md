# Federal Data Science Handbook — Site

GitHub Pages site for the Federal Data Science Handbook. Hand-rolled HTML/CSS/JS — no build step, no framework, no npm.

**Live site**: https://aporb.github.io/federal-ds-handbook-site/

## Site Structure

| File | Size | Purpose |
|------|------|---------|
| `index.html` | 34K | Homepage — hero, chapter grid, platform strip, toolkit cards |
| `chapters/01-introduction.html` through `chapters/13-advanced-topics.html` | 27-55K each | 13 chapter pages with full content, code blocks, diagrams |
| `platforms/advana.html`, `databricks.html`, `navy-jupiter.html`, `palantir.html`, `qlik.html` | 21-33K each | 5 platform guide pages |
| `docker.html` | 20K | Docker development environment reference |
| `security.html` | 19K | Security/compliance overview |
| `css/style.css` | 42K (2116 lines) | Single comprehensive stylesheet with CSS custom properties |
| `css/prism-theme.css` | 5K | Syntax highlighting theme |
| `js/main.js` | 13K | Navigation, sidebar, dark mode toggle, code copy, mobile menu |
| `js/mermaid-init.js` | 3.7K | Mermaid diagram rendering with theme support |
| `assets/favicon.svg` | SVG | Custom favicon |
| `chapters/template.html` | 18.5K | Documented authoring template with `{{PLACEHOLDERS}}` |
| `platforms/template.html` | 15.2K | Platform page authoring template |

## Design System

CSS custom properties defined in `:root` of `style.css`:

**Platform brand colors** (used throughout for badges, borders, accents):
- `--palantir-blue: #1B2A4A` (also the primary brand color)
- `--databricks-red: #FF3621`
- `--qlik-green: #009845`
- `--jupiter-navy: #003B5C`
- `--advana-gold: #C5A572`

**Dark mode**: `[data-theme="dark"]` selector overrides all semantic tokens. Background `#0F1117`, accent shifts from Palantir blue to Advana gold.

**Typography**: System serif for headings, system sans-serif for body, system monospace for code. Type scale via `--text-xs` through `--text-6xl`.

**Layout**: Fixed nav (64px), fixed sidebar (260px), CSS Grid `1fr 280px` for chapter content + in-page TOC. Collapses at 1200px (hide TOC), 900px (off-canvas sidebar), 600px (single column).

**External CDN dependencies**:
- Mermaid.js v11 — diagram rendering
- Prism.js v1.29.0 — syntax highlighting (Python, Bash, SQL)

## Design Principles — DO NOT VIOLATE

1. **No frameworks.** No React, no Vue, no Tailwind, no npm. Hand-rolled HTML/CSS/JS only.
2. **No build step.** Every HTML file is authored directly. No static site generator.
3. **No new CDN dependencies** without explicit approval.
4. **Respect the design system.** Use existing CSS custom properties — don't add new colors or font stacks.
5. **Dark mode must work.** Any new CSS must include `[data-theme="dark"]` overrides.
6. **Responsive must work.** Test at 1200px, 900px, and 600px breakpoints.

## Source of Truth

Content comes from the handbook repo (`../handbook/`). When updating a chapter page:
1. Read the corresponding handbook README: `../handbook/chapters/NN-name/README.md`
2. Update the HTML to reflect content changes
3. Handbook content is QA-signed-off — do not alter the substance, only the HTML rendering

## Common Agent Tasks

- **"Update chapter N page"** → Read `../handbook/chapters/NN-name/README.md` → update `chapters/NN-name.html`
- **"Add a new section"** → Follow existing HTML structure in that file. Use `.prose` class for content.
- **"Fix nav/UI bug"** → `js/main.js` handles all interactivity
- **"Update platform colors"** → CSS custom properties at top of `css/style.css`
- **"Add a new chapter page"** → Copy `chapters/template.html`, fill in `{{PLACEHOLDERS}}`
- **"Add a new platform page"** → Copy `platforms/template.html`

## Component Inventory

Key CSS classes for authoring:
- `.chapter-layout`, `.chapter-main`, `.chapter-toc` — page structure
- `.prose` — full typography system for content (h2-h4, p, lists, tables, code, blockquotes)
- `.callout-note`, `.callout-warning`, `.callout-tip` — highlighted callout boxes
- `.failure-card` — red-bordered failure mode sections
- `.exercises-callout` — gold-bordered exercise sections
- `.mermaid-wrapper`, `.mermaid-caption` — diagram containers
- `.code-block-wrapper`, `.code-block-header` — code block containers with copy button
- `.platform-badge` — inline platform reference pills

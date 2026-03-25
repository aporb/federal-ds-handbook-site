# Agent Guide — Federal Data Science Handbook Site

## What This Is

GitHub Pages site: https://aporb.github.io/federal-ds-handbook-site/

Hand-rolled HTML/CSS/JS. No build step. No framework. No npm. 26 HTML pages, 2 CSS files, 2 JS files.

This is the reading experience for the Federal Data Science Handbook. The source content lives in the companion handbook repo (`../handbook/`).

## For Any AI Agent

### When updating content
The handbook repo is the source of truth. Site pages render handbook content — they do not originate it. Always read the corresponding handbook README before editing a chapter page.

### When fixing bugs or improving UI
Read the affected file fully before editing. The CSS uses custom properties extensively — understand the variable system (`:root` in `css/style.css`) before adding styles. Dark mode (`[data-theme="dark"]`) must work for any CSS change.

### When adding new pages
Use `chapters/template.html` or `platforms/template.html`. These have documented `{{PLACEHOLDER}}` markers.

## What Agents Should NOT Do

- Install npm packages or build tooling
- Add JavaScript frameworks or libraries
- Change CDN dependency versions without checking compatibility
- Modify the design system (colors, typography, spacing) without explicit instruction
- Edit content substance — only the HTML rendering of handbook content

## Suggested Prompts

- "Update the chapter 9 page with new content from the handbook"
- "Fix the mobile navigation on the chapter pages"
- "Add syntax highlighting to a code block"
- "Check that all chapter and platform links work"
- "Add dark mode support to [new component]"
- "Create a new chapter page from the template"

## Cross-Repo Reference

Source handbook: `../handbook/` — read `../handbook/CLAUDE.md` for content map.

When content diverges between site and handbook: **handbook is authoritative**.

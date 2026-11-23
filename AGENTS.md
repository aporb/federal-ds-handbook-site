# Agent Guide — Federal Data Science Handbook Site

## What This Is

GitHub Pages site: https://aporb.github.io/federal-ds-handbook-site/

Hand-rolled HTML/CSS/JS. No build step. No framework. No npm. 24 HTML files (22 reader pages and 2 authoring templates), 2 CSS files, 2 JS files.

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

## Source mapping

Each page renders one handbook file. Read the source first, then mirror it.

| Site page | Handbook source |
|-----------|-----------------|
| `chapters/NN-name.html` | `chapters/NN-name/README.md` |
| `platforms/databricks.html` | `platform-guides/databricks/README.md` |
| `platforms/palantir.html` | `platform-guides/palantir-aip-foundry/README.md` |
| `platforms/navy-jupiter.html` | `platform-guides/navy-jupiter/README.md` |
| `platforms/advana.html` | `platform-guides/advana/README.md` |
| `platforms/qlik.html` | `platform-guides/qlik/README.md` |
| `docker.html` | `docs/LOCAL_ENVIRONMENT.md` and `docker-compose.yml` |
| `security.html` | `security-compliance/security-policy.md` and `security-compliance/CLAUDE.md` |
| `agents.html` | `AGENTS.md` and `CLAUDE.md` |
| `index.html` | `README.md` |

Only mirror content the handbook already states. Do not add independent policy, authorization, or performance claims.

## Checks before you report done

Run the local checker. It needs Python 3.11 and no packages:

```bash
python3 scripts/check_site.py
```

It checks local links and fragments, duplicate ids, the 24-file page count, and a list of retired claims such as "production-grade", "tamper-proof", "FIPS 140-2 encryption", and "expected early 2027". A pass means the structure is intact. It does not prove the prose is accurate or the design is usable.

Then load a changed page in a browser and confirm light and dark mode at 1280px and 390px. Record what you actually saw.

# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-10: First version of the site

- **Asked:** "那你可以直接幫我做嗎" (asked the agent to build the Part 1 site from the assignment instructions).
- **Agent produced:** `scripts/build_city_summary.py`, `data/city_summary.json`, and a new `index.html` comparing median price, price per sq ft, size and days on market for all 18 cities, with Champaign, Urbana and Savoy highlighted. Filled in the README.
- **Checked or changed:** Compared the city medians with the table in `docs/data_description_sheet.md` (e.g. Champaign $240,000, Davis $889,000 match). The first draft would have shown Pittsboro at $876,985.5, so prices are rounded to whole dollars.

# College-Town Home Prices

## What this site is for

Is Champaign–Urbana a bargain among college towns? The site compares median sale price, price per square foot, home size and days on market across the 18 cities in the dataset, with the University of Illinois cities highlighted. It is meant for students, families and anyone weighing where to buy near a campus.

## Live site

https://brian0201-c.github.io/campustown-home-sales-site/

## Data notes

- **Prices:** only sales from $10,000 to $5,000,000 are used (71 of 35,442 rows left out as implausible).
- **Medians**, not averages, for every figure; prices rounded to whole dollars.
- **Price per sq ft:** rows with `living_area_sqft` of 0 are left out of that measure.
- **Days on market:** `contract_date - list_date`, only for rows with both dates. Blanks are not zero.
- **No deduplication by address:** rows are keyed by `listing_id`.
- **`home_type` is not used**, because it is unreliable.
- `scripts/build_city_summary.py` makes `data/city_summary.json`, which the page reads.

## Tools we used

Claude (Anthropic) as the coding agent; Python with pandas for the summary script; plain HTML, CSS and JavaScript for the page.

## Citation

College-town home sales dataset, version 1.0 (2026). University of Illinois-Deloitte Foundation Center for Business Emerging Technologies. Data collected March 2026.

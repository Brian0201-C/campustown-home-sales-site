"""Build data/city_summary.json from data/college_town_home_sales.csv.

Rules (also stated on the site):
- Prices: keep sales from $10,000 to $5,000,000 inclusive.
- Price per square foot: only rows with living_area_sqft > 0.
- Days on market: contract_date - list_date, only rows with both dates (blanks are not zero).
- Rows are keyed by listing_id; nothing is deduplicated by address.

Run from the repository root:  python scripts/build_city_summary.py
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "college_town_home_sales.csv"
OUT = ROOT / "data" / "city_summary.json"

PRICE_MIN, PRICE_MAX = 10_000, 5_000_000

df = pd.read_csv(SRC, dtype={"zipcode": str, "county_fips": str, "parcel_number": str})
total_rows = len(df)

priced = df[(df.sale_price >= PRICE_MIN) & (df.sale_price <= PRICE_MAX)].copy()
priced["ppsf"] = priced.sale_price / priced.living_area_sqft.where(priced.living_area_sqft > 0)
priced["dom"] = (pd.to_datetime(priced.contract_date) - pd.to_datetime(priced.list_date)).dt.days
priced["sale_year"] = pd.to_datetime(priced.sale_date).dt.year


def r(x):
    return None if pd.isna(x) else int(round(x))


cities = []
for (city, state), g in priced.groupby(["city", "state"]):
    dom = g.dom.dropna()
    cities.append({
        "city": city,
        "state": state,
        "university": g.university.mode().iat[0],
        "sales": int(len(g)),
        "median_price": r(g.sale_price.median()),
        "median_ppsf": r(g.ppsf.median()),
        "median_dom": r(dom.median()),
        "dom_sales": int(len(dom)),
        "median_sqft": r(g.living_area_sqft.where(g.living_area_sqft > 0).median()),
        "median_year_built": r(g.year_built.median()),
    })
cities.sort(key=lambda c: -c["median_price"])

years = sorted(int(y) for y in priced.sale_year.dropna().unique())
by_year = (priced.dropna(subset=["sale_year"]).groupby(["sale_year"]).sale_price
           .agg(["median", "size"]).reset_index())

summary = {
    "total_rows": total_rows,
    "rows_used": int(len(priced)),
    "rows_excluded_price": int(total_rows - len(priced)),
    "price_rule": [PRICE_MIN, PRICE_MAX],
    "overall_median_price": r(priced.sale_price.median()),
    "sale_years": [years[0], years[-1]],
    "by_year": [{"year": int(y), "median_price": r(m), "sales": int(n)}
                for y, m, n in by_year.itertuples(index=False)],
    "cities": cities,
}
OUT.write_text(json.dumps(summary, indent=1))
print(f"Wrote {OUT} ({len(cities)} cities, {len(priced)} sales used of {total_rows})")

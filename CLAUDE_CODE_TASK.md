# Task: Generate 50 State Flyers from Markdown Analyses

## Overview
Generate a printable 5.5" × 8.5" HTML flyer for each of the 50 US states using data from the state analysis markdown files in this repo.

## Repo Structure

```
├── [state analysis markdown files]     ← Source data (one .md per state)
├── flyer_template.html                 ← Jinja2-style HTML template
├── CLAUDE_CODE_TASK.md                 ← This file
└── docs/
    └── flyers/                         ← Output directory (create if needed)
        ├── AL_flyer.html
        ├── AK_flyer.html
        ├── ...
        └── WY_flyer.html
```

## Step-by-Step Process

### Step 1: Locate All State Analysis Files

Scan the repo for markdown files matching state analysis content. They may be named like:
- `Alaska - State Analysis & Strategy.md`
- `alaska.md`
- `AK_analysis.md`
- Or similar patterns

List all 50 and map each to its state name and abbreviation. If any states are missing, note them at the end.

### Step 2: For Each State File, Extract Structured Data

Read the markdown file and extract these fields:

```json
{
  "state_name": "Colorado",
  "state_abbrev": "CO",
  "state_slug": "colorado",
  "tier_class": "green",
  "tier_label": "Strong Viability",
  "state_tagline": "Constitutional Home Rule • First State to Repeal Firearms Preemption",

  "home_rule": "Constitutional (Art. XX) — 103 cities, ~93% of population",
  "key_advantage": "First state to repeal firearms preemption. Vote Without Fear Act already bans guns at polls.",
  "key_risk": "Camp v. Westminster (Dec 2025) limits criminal penalties for home rule cities.",
  "recommended_framing": "Police resource allocation under home rule authority. Supplements state baseline.",
  "anti_sanctuary_note": "✓ None. HB19-1124 protects non-cooperation policies. No legal barrier.",

  "city1_name": "Boulder",
  "city1_meta": "Pop. 105K • Charter",
  "city1_why": "<strong>Launch city.</strong> Sanctuary ord., police oversight panel, progressive 9-member council.",
  "city2_name": "Denver",
  "city2_meta": "Pop. 715K • Oldest Charter",
  "city2_why": "<strong>Max visibility.</strong> Immigration ord. already limits fed cooperation. 13-member council.",
  "city3_name": "Aurora",
  "city3_meta": "Pop. 386K • Charter",
  "city3_why": "<strong>Time-sensitive.</strong> Nov '25 flipped council to 6-4 progressive. 3rd largest city.",

  "org_tags_html": "<span class=\"partner-tag\">COVRA (45+ orgs)</span><span class=\"partner-tag\">CO Common Cause</span><span class=\"partner-tag\">ACLU of CO</span>"
}
```

#### Extraction Rules

**tier_class / tier_label** — Look for viability tier in the opening summary or a line like `Viability Tier: 🟢 GREEN`:
- 🟢 GREEN / "Strong" / "exceptionally favorable" → `tier_class: "green"`, `tier_label: "Strong Viability"`
- 🟡 YELLOW / "Moderate" / "requires careful framing" → `tier_class: "yellow"`, `tier_label: "Moderate — Careful Framing Required"`
- 🔴 RED / "Challenging" / "Difficult" / "significant obstacles" → `tier_class: "red"`, `tier_label: "Challenging — Creative Strategy Needed"`

**state_tagline** — Compose from the home rule type + the single most notable legal feature from the Key Advantages section. Keep under 80 characters. Use `•` as separator. Examples:
- "Constitutional Home Rule • No Anti-Sanctuary Law"
- "Dillon's Rule • Local Affairs Doctrine"
- "Strongest Home Rule in the Nation • All Powers Not Prohibited"

**home_rule** — Pull from the Home Rule Authority or Legal Framework section. Include the constitutional article and any notable stat (number of home rule cities, % of population). Keep concise — one line.

**key_advantage** — The single strongest legal argument. Pull from Key Advantages or the opening summary. Two sentences max.

**key_risk** — The single biggest legal obstacle. Pull from Key Risks/Challenges or Preemption Framework. Two sentences max. State it honestly.

**recommended_framing** — How should the ordinance be framed to survive legal challenge? Pull from Strategic Notes or Drafting Recommendations. One to two sentences.

**anti_sanctuary_note** — Check for anti-sanctuary law discussion:
- If no anti-sanctuary law: `"✓ None. [brief supporting detail]. No legal barrier."`
- If anti-sanctuary law exists or is pending: `"⚠ [law name/number] — [brief risk]. Requires careful framing."`

When the anti-sanctuary situation is risky (⚠), also change the styling on the anti-sanctuary legal-item in the rendered HTML:
- Change `style="border-left-color: var(--green-400); background: var(--green-50);"` to `style="border-left-color: #F59E0B; background: #FEF9C3;"`
- Change `style="color: var(--green-700);"` to `style="color: #92400E;"`

**city1/2/3** — Pull from Target Municipalities section, Tier 1 first:
- `city_name`: City name only
- `city_meta`: Format as `Pop. [rounded] • [Charter/Home Rule/Code City/etc.]`
- `city_why`: Start with a `<strong>2-3 word hook.</strong>` then a brief reason. Keep total under 80 chars including the HTML tag.
- If a state has fewer than 3 target cities, remove the extra `<div class="city-card">` blocks from that state's output.
- If a state has no specific target cities listed, use the 2-3 largest cities with home rule authority and note them as potential targets.

**org_tags_html** — Pull 3-5 organizations from Coalition Partners section:
- Format each as: `<span class="partner-tag">[Name]</span>`
- Abbreviate long names (e.g., "League of Women Voters Colorado" → "LWV Colorado")
- Include member counts in parens if mentioned (e.g., "COVRA (45+ orgs)")
- If no coalition section exists, use statewide ACLU affiliate, League of Women Voters chapter, and Common Cause chapter as defaults.

### Step 3: Render Each Flyer

For each state:
1. Read `flyer_template.html`
2. Replace all `{{ variable }}` placeholders with the extracted data
3. Ensure no `{{ }}` placeholders remain in output
4. Save to `docs/flyers/[STATE_ABBREV]_flyer.html`

### Step 4: Generate Index File

Create `docs/flyers/index.html` — a simple page listing all 50 state flyers with links, organized alphabetically. Include the tier badge color next to each state name so someone browsing can quickly see the viability landscape.

### Step 5: Commit

```bash
git add docs/flyers/
git commit -m "Add 50-state printable flyers (5.5x8.5)"
```

---

## Colorado Reference (Already Validated)

Use this exact data for Colorado — it's been reviewed and approved. Generate Colorado first and compare against this to confirm extraction + rendering works before doing the other 49.

```
state_name: Colorado
state_abbrev: CO
state_slug: colorado
tier_class: green
tier_label: Strong Viability
state_tagline: Constitutional Home Rule • First State to Repeal Firearms Preemption
home_rule: Constitutional (Art. XX) — 103 cities, ~93% of population
key_advantage: First state to repeal firearms preemption. Vote Without Fear Act already bans guns at polls.
key_risk: Camp v. Westminster (Dec 2025) limits criminal penalties for home rule cities.
recommended_framing: Police resource allocation under home rule authority. Supplements state baseline.
anti_sanctuary_note: ✓ None. HB19-1124 protects non-cooperation policies. No legal barrier.
city1: Boulder | Pop. 105K • Charter | <strong>Launch city.</strong> Sanctuary ord., police oversight panel, progressive 9-member council.
city2: Denver | Pop. 715K • Oldest Charter | <strong>Max visibility.</strong> Immigration ord. already limits fed cooperation. 13-member council.
city3: Aurora | Pop. 386K • Charter | <strong>Time-sensitive.</strong> Nov '25 flipped council to 6-4 progressive. 3rd largest city.
orgs: COVRA (45+ orgs), CO Common Cause, ACLU of CO, LWV Colorado, CIRC (80+ orgs)
```

---

## Quality Checks

After generating each flyer, verify:
- [ ] State name appears in: header, legal landscape label, cities label, action step 3, footer URL
- [ ] Tier pill uses correct CSS class (`tier-green-pill`, `tier-yellow-pill`, or `tier-red-pill`)
- [ ] All city cards populated (or reduced if <3 available)
- [ ] Org tags populated from coalition section
- [ ] Footer URL uses correct lowercase hyphenated slug (e.g., `new-york`, `north-carolina`)
- [ ] Anti-sanctuary row styling matches state situation (green = safe, amber = risk)
- [ ] No `{{ }}` template placeholders remain in rendered output
- [ ] File saved to `docs/flyers/[ABBREV]_flyer.html`

---

## State Abbreviations & Slugs

```
AL alabama          AK alaska           AZ arizona
AR arkansas         CA california        CO colorado
CT connecticut      DE delaware          FL florida
GA georgia          HI hawaii            ID idaho
IL illinois         IN indiana           IA iowa
KS kansas           KY kentucky          LA louisiana
ME maine            MD maryland          MA massachusetts
MI michigan         MN minnesota         MS mississippi
MO missouri         MT montana           NE nebraska
NV nevada           NH new-hampshire     NJ new-jersey
NM new-mexico       NY new-york          NC north-carolina
ND north-dakota     OH ohio              OK oklahoma
OR oregon           PA pennsylvania      RI rhode-island
SC south-carolina   SD south-dakota      TN tennessee
TX texas            UT utah              VT vermont
VA virginia         WA washington        WV west-virginia
WI wisconsin        WY wyoming
```

---

## Batch Strategy

Process alphabetically. Do Colorado first to validate output against the reference data above. Then proceed with the remaining 49. If any state markdown file is missing or has incomplete data for required fields, generate the flyer with what's available and log the gap in `docs/flyers/GAPS.md` with the state name and what was missing.

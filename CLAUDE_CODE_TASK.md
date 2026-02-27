# Task: Generate 50 State Flyers & Add to Notion

## Overview
Generate a printable 5.5" x 8.5" HTML flyer for each of the 50 US states using data from existing Notion state analysis pages, then add each flyer as a child page to its corresponding state guide in Notion.

## Files
- `flyer_template.html` — Jinja2-style HTML template with `{{ variable }}` placeholders
- This file — Task instructions

## Step-by-Step Process

### Step 1: Get All State Page IDs from Notion

Fetch the project summary page to get all state page URLs:

```
Notion page ID: 2f585922-17c2-811d-8054-e449236bde17
Title: "Municipal Elections Ordinances Project - Summary"
```

This page lists all 50 state child pages. Collect every page URL that matches the pattern `[State Name] - State Analysis & Strategy`.

### Step 2: For Each State, Fetch & Extract Data

For each state page, fetch the full content from Notion, then extract these fields:

```json
{
  "state_name": "Colorado",
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
  
  "org_tags": "<span class=\"partner-tag\">COVRA (45+ orgs)</span><span class=\"partner-tag\">CO Common Cause</span><span class=\"partner-tag\">ACLU of CO</span><span class=\"partner-tag\">LWV Colorado</span><span class=\"partner-tag\">CIRC (80+ orgs)</span>"
}
```

#### Extraction Rules

**tier_class** — Determine from the viability tier mentioned in the page:
- "GREEN" or "Strong" → `"green"`
- "YELLOW" or "Moderate" → `"yellow"`  
- "RED" or "Challenging" or "Difficult" → `"red"`

**tier_label** — Use the tier descriptor from the page:
- Green states: `"Strong Viability"`
- Yellow states: `"Moderate — Careful Framing Required"`
- Red states: `"Challenging — Creative Strategy Needed"`

**state_tagline** — Compose from the home rule type + single most notable legal feature. Keep under 80 characters. Use bullet character `•` as separator.

**anti_sanctuary_note** — If no anti-sanctuary law: `"✓ None. [brief detail]. No legal barrier."`
If anti-sanctuary law exists or is pending: `"⚠ [law name/number] — [brief risk description]."`
Adjust the CSS styling: for states WITH anti-sanctuary risk, change the legal-full item's `style` to `border-left-color: #F59E0B; background: var(--gold-100);` and text color to `color: #92400E`.

**city1/2/3** — Pull the top 3 target cities from Section 3 (Target Municipalities). Use Tier 1 cities first. Keep `city_why` under 80 characters including HTML strong tag. If a state has fewer than 3 target cities, reduce the cities-row to show only what's available.

**org_tags** — Pull the top 3-5 organizations from the Coalition Partners section. Format each as `<span class="partner-tag">[Org Name]</span>`. Abbreviate long names. If the page lists sub-counts like "45+ organizations", include in parens.

### Step 3: Render Each Flyer

For each state's extracted data:
1. Read `flyer_template.html`
2. Replace all `{{ variable }}` placeholders with the state's data
3. Save as `flyers/[STATE_ABBREV]_flyer.html` (e.g., `flyers/CO_flyer.html`)

### Step 4: Add Each Flyer to Notion

For each state, create a new child page under the state's analysis page in Notion:

- **Parent**: The state's `[State Name] - State Analysis & Strategy` page
- **Title**: `[State Name] — Printable Flyer (5.5" × 8.5")`
- **Content**: The full rendered HTML wrapped in a code block, plus a brief intro:

```markdown
# Printable Flyer — [State Name]

Download or print this 5.5" × 8.5" flyer for distribution at council meetings, community events, and public spaces.

**To print:** Open the HTML file in any browser → File → Print → Set paper size to "Half Letter" (5.5 × 8.5) or print on Letter and trim.

---

## HTML Source

\`\`\`html
[FULL RENDERED HTML HERE]
\`\`\`
```

### Step 5: Update the Colorado Page

The Colorado flyer already exists as a finalized design. Use this exact Colorado data (already validated):

- state_name: Colorado
- state_slug: colorado  
- tier_class: green
- tier_label: Strong Viability
- state_tagline: Constitutional Home Rule • First State to Repeal Firearms Preemption
- home_rule: Constitutional (Art. XX) — 103 cities, ~93% of population
- key_advantage: First state to repeal firearms preemption. Vote Without Fear Act already bans guns at polls.
- key_risk: Camp v. Westminster (Dec 2025) limits criminal penalties for home rule cities.
- recommended_framing: Police resource allocation under home rule authority. Supplements state baseline.
- anti_sanctuary_note: ✓ None. HB19-1124 protects non-cooperation policies. No legal barrier.
- Cities: Boulder (105K, Charter), Denver (715K, Oldest Charter), Aurora (386K, Charter)
- Orgs: COVRA (45+ orgs), CO Common Cause, ACLU of CO, LWV Colorado, CIRC (80+ orgs)

## Quality Checks

After generating each flyer, verify:
- [ ] State name appears correctly in header, legal landscape label, cities label, action section, and footer URL
- [ ] Tier pill uses correct class (green/yellow/red) matching the analysis
- [ ] All 3 city cards are populated (or reduced if <3 cities available)
- [ ] Org tags are populated from the state's coalition section
- [ ] Footer URL uses lowercase state slug (e.g., `new-york`, `north-carolina`)
- [ ] Anti-sanctuary styling matches the state's situation (green for safe, amber for risk)
- [ ] No placeholder `{{ }}` variables remain in output

## State Slugs Reference

Use these URL slugs in the footer:

alabama, alaska, arizona, arkansas, california, colorado, connecticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachusetts, michigan, minnesota, mississippi, missouri, montana, nebraska, nevada, new-hampshire, new-jersey, new-mexico, new-york, north-carolina, north-dakota, ohio, oklahoma, oregon, pennsylvania, rhode-island, south-carolina, south-dakota, tennessee, texas, utah, vermont, virginia, washington, west-virginia, wisconsin, wyoming

## Batch Strategy

Process states alphabetically. If you hit rate limits on Notion API, batch in groups of 10 with brief pauses between batches.

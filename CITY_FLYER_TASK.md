# Task: Generate City-Level Flyers from State Analyses + Public Research

## Overview
Generate a printable 5.5" × 8.5" HTML flyer for every target city listed in the state analysis markdown files. Each flyer is hyper-local — it includes the city's council meeting schedule, city hall address, council structure, and phone number, all researched from public sources.

Expected output: **200-300 city flyers** across all 50 states.

## Repo Structure

```
├── [state analysis markdown files]       ← Source: city names + legal context
├── city_flyer_template.html              ← Jinja2-style HTML template
├── CITY_FLYER_TASK.md                    ← This file
└── docs/
    └── flyers/
        ├── state/                        ← State-level flyers (already generated)
        └── city/                         ← Output directory (create if needed)
            ├── CO_boulder.html
            ├── CO_denver.html
            ├── CO_aurora.html
            ├── ...
            └── index.html
```

## Step-by-Step Process

### Step 1: Build City List from State Files

Scan every state analysis markdown file. For each state, find the **Target Municipalities** section (or similar — may be labeled "Target Cities", "Municipal Targets", etc.). Extract ALL listed cities from both Tier 1 and Tier 2. 

For each city, capture whatever the state file already provides:
- City name
- Population (if listed)
- Political lean (if noted)
- Home rule status (if noted)
- Brief strategic notes

Save as a working list: `[state_abbrev, city_name, existing_notes]`

### Step 2: Research City Council Details

For each city on the list, research and fill in these fields from **official city government websites** (.gov, .us, or official city domains):

```json
{
  "city_name": "Boulder",
  "state_abbrev": "CO",
  "state_slug": "colorado",
  "city_population": "105,000",
  "city_government_type": "Council-Manager",
  "city_home_rule_status": "Home Rule Charter City",

  "legal_authority": "Art. XX home rule charter. City supersedes state law on local matters.",
  "why_it_works": "Sanctuary ord. (2017), police oversight panel, progressive 9-member council.",
  "ordinance_description": "Direct city police not to assist armed federal personnel near polling places. No new criminal penalties — just a policy on how Boulder's resources are used.",

  "council_size": "9",
  "council_structure": "Council-Manager · Mayor elected by council",
  "council_note": "All seats nonpartisan. Next election: Nov 2027.",
  "city_hall_name": "Boulder City Hall",
  "city_hall_address": "1777 Broadway, Boulder, CO 80302",
  "contact_phone": "(303) 441-3002",
  "contact_email_or_url": "bouldercolorado.gov/city-council",
  "meeting_day": "Tues",
  "meeting_time": "6:00 PM",
  "meeting_frequency": "1st & 3rd Tues",

  "org_tags_html": "<span class=\"partner-tag\">COVRA (45+ orgs)</span><span class=\"partner-tag\">ACLU of CO</span><span class=\"partner-tag\">LWV Boulder County</span>"
}
```

#### Research Strategy

For each city, look for this information in order:

1. **City council/government page** — usually `[city].gov/council` or `[city].gov/city-council`
   - Council size, structure, meeting schedule, city hall address
2. **Meeting agendas page** — confirms meeting days/times and frequency
3. **Contact page** — main city hall phone, clerk's office, or council office
4. **City charter or code** — confirms home rule status, government type

#### Research Rules

- **Use only official sources.** City .gov/.us sites, or clearly official city websites.
- **If you can't find a specific detail, use reasonable defaults:**
  - Meeting time unknown → leave as `"Check city website"`
  - Phone unknown → use city hall main line
  - Council note unknown → omit the subtle line
- **Meeting day format:** Use 3-letter abbreviation: `Mon`, `Tue`, `Wed`, `Thu`, `Fri`
- **Meeting time format:** `6:00 PM`, `7:30 PM`, etc.
- **Meeting frequency format:** `1st & 3rd Tue`, `Every Mon`, `2nd & 4th Thu`, etc.
- **Population:** Round to nearest thousand for <100K, nearest 10K for >100K. Use `~` prefix.
- **Government type:** Use standard labels: `Council-Manager`, `Mayor-Council`, `Commission`, `Town Meeting`, etc.

### Step 3: Fill in Legal/Strategy Fields

These fields come from the **state analysis file**, adapted to the city level:

**legal_authority** — Condense the state's home rule framework into one line specific to this city. Example: "Art. XX home rule charter. City supersedes state law on local matters." For Dillon's Rule states: "Local affairs doctrine under [statute]. Police resource allocation is a local matter."

**why_it_works** — Pull from the city's notes in the state file + any relevant city-level context. Keep to one sentence. Start with the strongest hook.

**ordinance_description** — Adapt based on the state's recommended framing. Keep it plain English, one to two sentences. Always end with a framing that neutralizes "this is radical" objections — e.g., "just a policy on how [City]'s resources are used."

**org_tags_html** — Use the state-level coalition partners, but prefer local chapters when they exist. If the state file mentions a city-specific organization, prioritize it. Format: `<span class="partner-tag">[Name]</span>`. 3-5 tags max.

### Step 4: Render Each Flyer

For each city:
1. Read `city_flyer_template.html`
2. Replace all `{{ variable }}` placeholders
3. Verify no `{{ }}` placeholders remain
4. Save to `docs/flyers/city/[STATE_ABBREV]_[city_slug].html`
   - City slug: lowercase, hyphens for spaces (e.g., `fort-collins`, `new-york-city`, `st-paul`)

### Step 5: Generate Index

Create `docs/flyers/city/index.html` with:
- States as section headers (alphabetical)
- Cities listed under each state with links
- Population shown next to each city name

### Step 6: Generate Research Log

Create `docs/flyers/city/RESEARCH_LOG.md` documenting:
- For each city: sources used for council data
- Any cities where data was incomplete + what's missing
- Any cities where the official website was unavailable

### Step 7: Commit

```bash
git add docs/flyers/city/
git commit -m "Add city-level flyers for all target municipalities"
```

---

## Boulder Reference (Validated)

Use this data for Boulder to validate your output matches the approved design:

```
city_name: Boulder
state_abbrev: CO
state_slug: colorado
city_population: ~105,000
city_government_type: Council-Manager
city_home_rule_status: Home Rule Charter City

legal_authority: Art. XX home rule charter. City supersedes state law on local matters.
why_it_works: Sanctuary ord. (2017), police oversight panel, progressive 9-member council.
ordinance_description: Direct city police not to assist armed federal personnel near polling places. No new criminal penalties — just a policy on how Boulder's resources are used.

council_size: 9
council_structure: Council-Manager · Mayor elected by council
council_note: All seats nonpartisan. Next election: Nov 2027.
city_hall_name: Boulder City Hall
city_hall_address: 1777 Broadway, Boulder, CO 80302
contact_phone: (303) 441-3002
contact_email_or_url: bouldercolorado.gov/city-council
meeting_day: Tue
meeting_time: 6:00 PM
meeting_frequency: 1st & 3rd Tue

orgs: COVRA (45+ orgs), ACLU of CO, LWV Boulder County
```

---

## Quality Checks Per City

- [ ] City name matches state file exactly
- [ ] State abbreviation is correct
- [ ] Population is reasonable (cross-check if it seems off)
- [ ] Government type matches city charter (council-manager vs mayor-council matters)
- [ ] Meeting schedule is current (from official city site, not outdated cached data)
- [ ] Phone number is a working city government number (not a personal line)
- [ ] City hall address is the actual council meeting location
- [ ] Legal authority field reflects THIS city's actual home rule status
- [ ] Ordinance description uses the state's recommended framing
- [ ] Footer URL uses state slug (city flyers link to state page)
- [ ] No `{{ }}` template placeholders remain
- [ ] File is named `[STATE]_[city-slug].html`

---

## Batch Strategy

Process by state, alphabetically. Within each state, process cities alphabetically. 

For research efficiency, batch cities by state — the council website patterns are often similar within a state (e.g., many Colorado cities use `cityof[name].gov`, many Minnesota cities use `[name]mn.gov`).

If a city's official website is unreachable or has no council information, log it in `RESEARCH_LOG.md` and generate the flyer with available data, using `"Check city website"` for missing meeting/contact fields.

**Expected volume:** ~200-300 cities across 50 states. Plan for this to take multiple sessions. Process 5-10 states per session.

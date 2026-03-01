#!/usr/bin/env python3
"""
Generate city-level printable HTML flyers from state analysis markdown files.

Reads each state's markdown in docs/state-guides/, extracts all target cities
from Section 3, merges with state legal context from Section 1, and renders
city_flyer_template.html for each city.

Usage:
    python3 generate_city_flyers.py              # Generate all cities
    python3 generate_city_flyers.py CO           # Generate Colorado cities only
    python3 generate_city_flyers.py CO boulder   # Generate Boulder, CO only
"""

import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "city_flyer_template.html"
STATE_GUIDES_DIR = BASE_DIR / "docs" / "state-guides"
OUTPUT_DIR = BASE_DIR / "docs" / "flyers" / "city"
RESEARCH_LOG_PATH = OUTPUT_DIR / "RESEARCH_LOG.md"

# Full 50-state mapping: (abbreviation, slug, display name)
STATES = [
    ("AL", "alabama", "Alabama"),
    ("AK", "alaska", "Alaska"),
    ("AZ", "arizona", "Arizona"),
    ("AR", "arkansas", "Arkansas"),
    ("CA", "california", "California"),
    ("CO", "colorado", "Colorado"),
    ("CT", "connecticut", "Connecticut"),
    ("DE", "delaware", "Delaware"),
    ("FL", "florida", "Florida"),
    ("GA", "georgia", "Georgia"),
    ("HI", "hawaii", "Hawaii"),
    ("ID", "idaho", "Idaho"),
    ("IL", "illinois", "Illinois"),
    ("IN", "indiana", "Indiana"),
    ("IA", "iowa", "Iowa"),
    ("KS", "kansas", "Kansas"),
    ("KY", "kentucky", "Kentucky"),
    ("LA", "louisiana", "Louisiana"),
    ("ME", "maine", "Maine"),
    ("MD", "maryland", "Maryland"),
    ("MA", "massachusetts", "Massachusetts"),
    ("MI", "michigan", "Michigan"),
    ("MN", "minnesota", "Minnesota"),
    ("MS", "mississippi", "Mississippi"),
    ("MO", "missouri", "Missouri"),
    ("MT", "montana", "Montana"),
    ("NE", "nebraska", "Nebraska"),
    ("NV", "nevada", "Nevada"),
    ("NH", "new-hampshire", "New Hampshire"),
    ("NJ", "new-jersey", "New Jersey"),
    ("NM", "new-mexico", "New Mexico"),
    ("NY", "new-york", "New York"),
    ("NC", "north-carolina", "North Carolina"),
    ("ND", "north-dakota", "North Dakota"),
    ("OH", "ohio", "Ohio"),
    ("OK", "oklahoma", "Oklahoma"),
    ("OR", "oregon", "Oregon"),
    ("PA", "pennsylvania", "Pennsylvania"),
    ("RI", "rhode-island", "Rhode Island"),
    ("SC", "south-carolina", "South Carolina"),
    ("SD", "south-dakota", "South Dakota"),
    ("TN", "tennessee", "Tennessee"),
    ("TX", "texas", "Texas"),
    ("UT", "utah", "Utah"),
    ("VT", "vermont", "Vermont"),
    ("VA", "virginia", "Virginia"),
    ("WA", "washington", "Washington"),
    ("WV", "west-virginia", "West Virginia"),
    ("WI", "wisconsin", "Wisconsin"),
    ("WY", "wyoming", "Wyoming"),
]


# ---------------------------------------------------------------------------
# Helpers (reused from generate_flyers.py)
# ---------------------------------------------------------------------------

def clean_md(text):
    """Strip markdown bold/italic markers, headings, and clean up whitespace."""
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def html_escape(text):
    """Minimal HTML escaping for template values."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def first_sentences(text, n=2):
    """Extract first n sentences from text."""
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    result = ' '.join(parts[:n])
    if len(result) > 200:
        result = result[:197] + '...'
    return result


def extract_section(content, section_num):
    """Extract content of a numbered section (## Section N: ...)."""
    pattern = rf'##\s+Section\s+{section_num}\b[^\n]*\n(.*?)(?=##\s+Section\s+\d|##\s+Conclusion|$)'
    m = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


def extract_subsections(section_text):
    """Split a section into subsections by ### headings."""
    parts = re.split(r'###\s+', section_text)
    result = []
    for part in parts[1:]:
        lines = part.split('\n', 1)
        heading = lines[0].strip()
        body = lines[1].strip() if len(lines) > 1 else ""
        result.append((heading, body))
    return result


def get_opening_paragraph(content):
    """Get the opening paragraph(s) between the first # heading and first ---."""
    m = re.search(r'^#\s+[^\n]+\n+(.*?)(?=\n---)', content, re.MULTILINE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def extract_tier(content):
    """Extract tier from YAML frontmatter tags."""
    fm = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm:
        frontmatter = fm.group(1)
        if 'tier-green' in frontmatter:
            return 'green'
        elif 'tier-yellow' in frontmatter:
            return 'yellow'
        elif 'tier-red' in frontmatter:
            return 'red'
    return 'red'


def city_slug(name):
    """Convert city name to URL slug."""
    slug = name.lower().strip()
    slug = slug.replace('/', '-')  # Jackson/Teton -> Jackson-Teton
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


# ---------------------------------------------------------------------------
# City Extraction — Get ALL target cities from Section 3
# ---------------------------------------------------------------------------

def extract_all_cities(section3, state_name):
    """Extract all target cities from Section 3 (not capped at 3)."""
    cities = []

    # Pattern 1: ### subsection headings
    city_headings = re.finditer(
        r'###\s+(?:#?\d+\s+)?(.+?)'
        r'(?:\s*\((?:Primary|Secondary|Scale|Additional|University|Tertiary)\s*Target\))?'
        r'(?:\s*--\s*Population\s*~?([\d,]+))?'
        r'(?:\s*--\s*Passage\s+Probability:\s*(\w[\w\s-]*))?'
        r'\s*\n(.*?)(?=###|\n##|\Z)',
        section3,
        re.DOTALL
    )

    for match in city_headings:
        raw_name = match.group(1).strip()
        pop_from_heading = match.group(2)
        body = match.group(4).strip()

        # Clean city name — remove descriptive phrases after the city name
        # First: strip trailing parentheticals (Primary Target), (Secondary Target), etc.
        name = re.sub(r'\s*\([^)]*\)\s*$', '', raw_name).strip()
        # Split on colon followed by space (handles "CityName: description")
        name = re.split(r':\s+', name)[0].strip()
        # Split on descriptive verb phrases and em-dash (case-insensitive)
        name = re.split(
            r'\s+(?:offer|provid|lead|creat|has\s|is\s|rank|emerg|combin|represent|'
            r'present|optimal|fresh|primary|recent|campaigns?|—|\bthe\b|\bwith\b)',
            name, flags=re.IGNORECASE
        )[0].strip()
        name = re.split(r'\s*/\s*', name)[0].strip()
        name = re.sub(r"'s\s+.*$", '', name).strip()

        # Skip non-city headings (check cleaned name, not raw heading)
        skip_words = ['deprioritize', 'non-starter', 'county-level', 'ordinance',
                      'cities to', 'recommended', 'additional target', 'strategic',
                      'drafting', 'general note', 'no city', 'tier 1', 'tier 2',
                      'tier 3', 'strong secondary', 'recent campaign',
                      'model', 'overview', 'non-starters', 'alternative',
                      'parish-level', 'faulkner act', 'ndcc chapter',
                      'governing body summary', 'chiesman', 'municipal target',
                      'pathway', 'considerations', 'additional prospects',
                      'the section', 'state-level', 'selection methodology',
                      'primary strategy', 'recent municipal', 'governing body',
                      'non-binding', 'resolution strategy', 'tier 1', 'tier 2']
        if any(w in name.lower() for w in skip_words):
            continue

        if len(name) > 30 or len(name) < 2:
            continue

        # Final validation: skip names that still contain descriptive words
        desc_words = ['optimal', 'ranks', 'fresh', 'primary', 'recent',
                      'campaigns', 'action', 'strategy', 'methodology',
                      'council', 'governing']
        if any(w in name.lower().split() for w in desc_words):
            continue

        # Handle combined headings: "Ashland and Eugene" -> two separate cities
        if ' and ' in name and len(name.split(' and ')) == 2:
            parts = name.split(' and ')
            for part in parts:
                part = part.strip()
                if 2 <= len(part) <= 30:
                    city_data = _parse_city_body(part, pop_from_heading, body)
                    if city_data:
                        cities.append(city_data)
            continue

        city_data = _parse_city_body(name, pop_from_heading, body)
        if city_data:
            cities.append(city_data)

    # Also try other patterns and merge results (some states mix formats)
    seen_slugs = {c['city_slug'] for c in cities}

    # Pattern 2: Bold narrative paragraphs
    for c in _extract_cities_from_paragraphs(section3, state_name):
        if c['city_slug'] not in seen_slugs:
            cities.append(c)
            seen_slugs.add(c['city_slug'])

    # Pattern 3: Bullet list format
    for c in _extract_cities_from_bullets(section3):
        if c['city_slug'] not in seen_slugs:
            cities.append(c)
            seen_slugs.add(c['city_slug'])

    # Pattern 4: Table format
    for c in _extract_cities_from_table(section3, state_name):
        if c['city_slug'] not in seen_slugs:
            cities.append(c)
            seen_slugs.add(c['city_slug'])

    return cities


def _parse_city_body(name, pop_from_heading, body):
    """Parse city body text to extract population, gov type, governing body, and description."""
    # Extract population — try multiple patterns
    pop = pop_from_heading
    if not pop:
        pop_patterns = [
            r'\*\*Population:?\*\*\s*~?([\d,]+)',
            r'Pop(?:ulation)?\.?\s*~?([\d,]+)',
            r'\*\*([\d,]+)\s*(?:residents|population|people)\*\*',
            r'\*\*~?([\d,]+)\s*-?resident',
            r'([\d,]+(?:,\d+)*)\s*residents',
            r'city(?:\'s)?\s+.*?([\d,]+(?:,\d+)*)\s*(?:residents|population|people)',
            r'at\s+\*\*([\d,]+(?:,\d+)*)\s*residents',
            r'third-largest\s+city\s+at\s+\*\*([\d,]+)',
        ]
        for pat in pop_patterns:
            pop_match = re.search(pat, body, re.IGNORECASE)
            if pop_match:
                candidate = pop_match.group(1).replace(',', '')
                try:
                    num = int(candidate)
                    if num >= 5000:  # Only accept if it looks like a real population
                        pop = pop_match.group(1)
                        break
                except ValueError:
                    pass

    pop_str = ""
    if pop:
        try:
            pop_num = int(pop.replace(',', ''))
            if pop_num >= 1_000_000:
                pop_str = f"~{pop_num / 1_000_000:.1f}M"
            elif pop_num >= 1000:
                pop_str = f"~{pop_num:,}"
            else:
                pop_str = f"~{pop_num}"
        except ValueError:
            pass

    # Extract government type
    gov_match = re.search(
        r'(council-manager|mayor-council|strong[- ]mayor|commission-manager|'
        r'commission|unified government|town meeting|council-administrator|'
        r'town manager|borough|township)',
        body, re.IGNORECASE
    )
    gov_type = gov_match.group(1).title() if gov_match else ""

    # Extract home rule / charter status
    charter_match = re.search(
        r'(home rule charter|charter city|home rule|code city|code home rule|'
        r'first-class|independent city|statutory city)',
        body, re.IGNORECASE
    )
    charter = charter_match.group(1).title() if charter_match else ""

    # Extract governing body details
    gov_body_match = re.search(r'\*\*Governing\s+[Bb]ody\*\*:?\s*([^\n]+)', body)
    gov_body = ""
    if gov_body_match:
        gov_body = clean_md(gov_body_match.group(1).strip())

    # Extract council size from governing body or body text
    council_size = ""
    size_match = re.search(r'(\d+)[\s-]*member', body, re.IGNORECASE)
    if size_match:
        council_size = size_match.group(1)

    # Build description — the full body cleaned, used for "why it works" extraction
    cleaned = clean_md(body)
    desc = cleaned[:500]  # Keep more text for better extraction later

    return {
        'city_name': name,
        'city_slug': city_slug(name),
        'population': pop_str,
        'gov_type': gov_type,
        'charter_status': charter,
        'governing_body': gov_body,
        'council_size': council_size,
        'description': desc,
    }


def _extract_cities_from_paragraphs(section3, state_name):
    """Extract cities from narrative paragraph format where city names are bold."""
    cities = []
    para_matches = re.finditer(
        r'(?:^|\n)\s*\*\*([A-Z][^*]{2,40}?)\*\*\s+'
        r'((?:(?:emerges?|represents?|offers?|provides?|presents?|ranks?|combines?|has|is|the|operates?|leads?)\b)'
        r'[^\n]*(?:\n(?!\s*\*\*[A-Z]|\s*###|\s*##|\s*\n\s*\*\*[A-Z]).*)*)',
        section3,
        re.MULTILINE
    )

    for match in para_matches:
        raw_name = match.group(1).strip()
        body = match.group(2).strip()

        skip_words = ['population', 'key consideration', 'governing body',
                      'weakness', 'note', 'secondary target', 'the most',
                      'no city', 'target city']
        if any(w in raw_name.lower() for w in skip_words):
            continue
        if len(raw_name) > 30 or len(raw_name) < 2:
            continue

        city_data = _parse_city_body(raw_name, None, body)
        if city_data:
            cities.append(city_data)

    return cities


def _extract_cities_from_bullets(section3):
    """Extract cities from bullet list format: - **CityName** -- description."""
    cities = []
    bullet_matches = re.finditer(
        r'[-*]\s+\*\*([^*]+?)\*\*\s*(?:—|--|-)\s*(.+)',
        section3
    )
    for match in bullet_matches:
        raw_name = match.group(1).strip()
        desc = match.group(2).strip()

        # Handle "Norfolk / Virginia Beach" style combined entries
        if ' / ' in raw_name:
            parts = raw_name.split(' / ')
        else:
            parts = [raw_name]

        for name in parts:
            name = name.strip()
            if len(name) > 30 or len(name) < 2:
                continue
            cities.append({
                'city_name': name,
                'city_slug': city_slug(name),
                'population': '',
                'gov_type': '',
                'charter_status': '',
                'governing_body': '',
                'council_size': '',
                'description': clean_md(desc)[:150],
            })
    return cities


def _extract_cities_from_table(section3, state_name):
    """Extract cities from markdown table format."""
    cities = []
    rows = re.findall(r'\|\s*\*?\*?([^|*]+?)\*?\*?\s*\|\s*~?([\d,]+)\s*\|([^|]+)\|', section3)
    for row in rows:
        name = row[0].strip()
        pop = row[1].strip()
        rest = row[2].strip()
        if name.lower() in ('municipality', 'city', 'target', '-', '---', 'state',
                              'city council', 'common council', 'council', 'governing body',
                              'government', 'county', 'borough', 'town'):
            continue
        if re.match(r'^-+$', name):
            continue
        name = re.sub(r'\[([^\]]+)\].*', r'\1', name).strip()
        try:
            pop_num = int(pop.replace(',', ''))
            pop_str = f"~{pop_num:,}"
        except ValueError:
            pop_str = ""
        cities.append({
            'city_name': name,
            'city_slug': city_slug(name),
            'population': pop_str,
            'gov_type': '',
            'charter_status': '',
            'governing_body': '',
            'council_size': '',
            'description': clean_md(rest)[:150],
        })
    return cities


# ---------------------------------------------------------------------------
# State Legal Context Extraction
# ---------------------------------------------------------------------------

def extract_state_context(content_body, state_name, state_abbrev):
    """Extract state-level legal context for city flyers."""
    opening_para = get_opening_paragraph(content_body)
    section1 = extract_section(content_body, 1)
    section4 = extract_section(content_body, 4)

    # Home rule / legal authority
    legal_authority = _extract_legal_authority(section1)

    # Recommended framing -> ordinance description
    ordinance_description = _extract_ordinance_description(section1, extract_section(content_body, 3))

    # Organizations
    orgs = _extract_orgs(section4, state_name, state_abbrev)
    org_tags = ''.join(f'<span class="partner-tag">{html_escape(org)}</span>' for org in orgs)

    return {
        'legal_authority': legal_authority,
        'ordinance_description': ordinance_description,
        'org_tags_html': org_tags,
    }


def _extract_legal_authority(section1):
    """Extract legal authority summary for city flyers."""
    subsections = extract_subsections(section1)

    for heading, body in subsections:
        if re.search(r'home\s*rule|article\s+(xi|xx|xii|iv|v)|municipal\s+power|legal\s+framework',
                      heading, re.IGNORECASE):
            lines = body.split('\n')
            for line in lines:
                line = line.strip()
                if not line or line.startswith('|') or line.startswith('-'):
                    continue
                cleaned = clean_md(line)
                if re.search(r'(Article\s+[XIVL]+|Art\.\s+[XIVL]+|Constitution|home rule|Dillon)',
                             cleaned, re.IGNORECASE):
                    result = first_sentences(cleaned, 1)
                    if len(result) > 130:
                        result = result[:127] + '...'
                    return result

    # Fallback
    lines = section1.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('|'):
            continue
        cleaned = clean_md(line)
        if re.search(r'(home rule|Dillon|constitution|Article)', cleaned, re.IGNORECASE):
            result = first_sentences(cleaned, 1)
            if len(result) > 130:
                result = result[:127] + '...'
            return result

    return "See state guide for legal framework details."


def _extract_ordinance_description(section1, section3):
    """Extract ordinance description based on recommended framing."""
    framing_keywords = ['fram', 'resource allocation', 'police power', 'draft',
                        'ordinance should', 'language must', 'recommended approach',
                        'should be framed', 'strategic recommendation']

    # Check Section 3 for drafting principles
    subsections = extract_subsections(section3)
    city_heading_skip = re.compile(
        r'(Target\b|Primary\b|Secondary\b|Tertiary\b|First Target|'
        r'Population|County-Level|Non-Starter)',
        re.IGNORECASE
    )
    for heading, body in subsections:
        if (re.search(r'(draft|fram|recommend|approach|principle)', heading, re.IGNORECASE)
                and not city_heading_skip.search(heading)):
            cleaned = clean_md(body)
            sents = re.split(r'(?<=[.!?])\s+', cleaned)
            for sent in sents:
                if any(kw in sent.lower() for kw in framing_keywords) and len(sent) > 20:
                    result = first_sentences(sent, 2)
                    if len(result) > 180:
                        result = result[:177] + '...'
                    return result
            if sents and len(sents[0]) > 20:
                return first_sentences(sents[0], 2)[:180]

    # Fallback
    return ("Direct city police not to assist armed federal personnel near polling places. "
            "No new criminal penalties — just a policy on how the city's own resources are used.")


def _extract_orgs(section4, state_name, state_abbrev):
    """Extract coalition partner organizations from Section 4."""
    orgs = []
    org_matches = re.findall(r'(?:^|\n)\s*[-*]?\s*\*\*([^*]+?)\*\*', section4)
    if not org_matches:
        org_matches = re.findall(r'\d+\.\s*\*\*([^*]+?)\*\*', section4)

    seen = set()
    skip = ['key', 'contact', 'opposition', 'governor', 'ag ', 'attorney general',
            'legislature', 'secretary', 'republican', 'population', 'status',
            'anti-sanctuary', 'legislative', 'judicial', 'strategic', 'note',
            'weakness', 'key consideration', 'governing body', 'probability']

    for org in org_matches:
        org = org.strip()
        if any(s in org.lower() for s in skip):
            continue
        if len(org) < 3 or len(org) > 60:
            continue
        # Abbreviate long names
        org = re.sub(r'League of Women Voters of\s+', 'LWV ', org)
        org = re.sub(r'League of Women Voters\s+', 'LWV ', org)
        org = re.sub(r'American Civil Liberties Union of\s+', 'ACLU of ', org)
        if len(org) > 35:
            org = org[:32] + '...'
        if org.lower() not in seen:
            seen.add(org.lower())
            orgs.append(org)
        if len(orgs) >= 5:
            break

    if len(orgs) < 3:
        defaults = [
            f"ACLU of {state_name}",
            f"LWV {state_name}",
            f"Common Cause {state_name}",
        ]
        for d in defaults:
            if d.lower() not in seen:
                orgs.append(d)
                seen.add(d.lower())
            if len(orgs) >= 3:
                break

    return orgs[:5]


# ---------------------------------------------------------------------------
# City-specific context extraction from Section 3 body
# ---------------------------------------------------------------------------

def _is_metadata_sentence(sent):
    """Check if a sentence is structural/metadata rather than strategic content."""
    stripped = sent.strip().lstrip('- ')
    return bool(re.match(
        r'^(Population:?\s*~?[\d,]|Government:|Military |Key advantage:|'
        r'Passage |Governing Body:?|Council size|City Manager:|'
        r'Next election|Term limit)',
        stripped, re.IGNORECASE
    ))


def extract_why_it_works(city_description, city_name):
    """Extract 'why it works' from city description text.

    Looks for sentences about existing ordinances, political composition, or
    progressive achievements that explain why this city is a good target.
    """
    sentences = re.split(r'(?<=[.!?])\s+', city_description)

    # Filter out metadata/population sentences
    strategic_sentences = [s for s in sentences if not _is_metadata_sentence(s)]

    # First priority: sentences that mention concrete civic achievements
    achievement_keywords = ['sanctuary', 'ordinance', 'oversight', 'passed',
                            'established', 'adopted', 'voted', 'enacted',
                            'progressive council', 'progressive 9-member',
                            'progressive majority', 'flipped']
    for sent in strategic_sentences:
        lower = sent.lower()
        if any(kw in lower for kw in achievement_keywords) and 20 < len(sent) < 200:
            result = sent.strip()
            if len(result) > 130:
                result = result[:127] + '...'
            return result

    # Second priority: sentences about political alignment
    political_keywords = ['democrat', 'progressive', 'liberal', 'strong',
                          'already', 'existing', 'infrastructure', 'rights',
                          'coalition', 'activist', 'diverse', 'immigrant']
    for sent in strategic_sentences:
        lower = sent.lower()
        if any(kw in lower for kw in political_keywords) and 20 < len(sent) < 200:
            result = sent.strip()
            if len(result) > 130:
                result = result[:127] + '...'
            return result

    # Fallback: first substantial non-metadata sentence
    for sent in strategic_sentences:
        if 20 < len(sent) < 200:
            result = sent.strip()
            if len(result) > 130:
                result = result[:127] + '...'
            return result

    return "See state guide for strategic analysis."


# ---------------------------------------------------------------------------
# Council Research Data
# ---------------------------------------------------------------------------

# Pre-researched council data for all target cities.
# Each key is "STATE_ABBREV:city_slug"
COUNCIL_DATA = {}


def load_council_data_file():
    """Load council research data from JSON file if it exists."""
    global COUNCIL_DATA
    data_path = BASE_DIR / "city_council_data.json"
    if data_path.exists():
        COUNCIL_DATA.update(json.loads(data_path.read_text(encoding='utf-8')))


def get_council_data(state_abbrev, slug):
    """Get researched council data for a city, or defaults."""
    key = f"{state_abbrev}:{slug}"
    if key in COUNCIL_DATA:
        return COUNCIL_DATA[key]
    return {
        'council_size': '',
        'council_structure': '',
        'council_note': '',
        'city_hall_name': 'City Hall',
        'city_hall_address': 'Check city website',
        'contact_phone': 'Check city website',
        'contact_email_or_url': 'Check city website',
        'meeting_day': 'Check',
        'meeting_time': 'city website',
        'meeting_frequency': '',
    }


# ---------------------------------------------------------------------------
# Template Rendering
# ---------------------------------------------------------------------------

def render_city_flyer(template, data):
    """Render the city flyer template with data."""
    html = template

    replacements = {
        '{{ city_name }}': data.get('city_name', ''),
        '{{ state_abbrev }}': data.get('state_abbrev', ''),
        '{{ state_slug }}': data.get('state_slug', ''),
        '{{ city_population }}': data.get('population', ''),
        '{{ city_government_type }}': data.get('gov_type', ''),
        '{{ city_home_rule_status }}': data.get('charter_status', ''),
        '{{ legal_authority }}': data.get('legal_authority', ''),
        '{{ why_it_works }}': data.get('why_it_works', ''),
        '{{ ordinance_description }}': data.get('ordinance_description', ''),
        '{{ council_size }}': data.get('council_size', ''),
        '{{ council_structure }}': data.get('council_structure', ''),
        '{{ council_note }}': data.get('council_note', ''),
        '{{ city_hall_name }}': data.get('city_hall_name', 'City Hall'),
        '{{ city_hall_address }}': data.get('city_hall_address', 'Check city website'),
        '{{ contact_phone }}': data.get('contact_phone', 'Check city website'),
        '{{ contact_email_or_url }}': data.get('contact_email_or_url', 'Check city website'),
        '{{ meeting_day }}': data.get('meeting_day', 'Check'),
        '{{ meeting_time }}': data.get('meeting_time', 'city website'),
        '{{ meeting_frequency }}': data.get('meeting_frequency', ''),
        '{{ org_tags_html }}': data.get('org_tags_html', ''),
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html


# ---------------------------------------------------------------------------
# Index Generation
# ---------------------------------------------------------------------------

def generate_index(all_cities):
    """Generate index.html listing all city flyers grouped by state."""
    # Group cities by state
    by_state = {}
    for city in all_cities:
        state = city['state_name']
        if state not in by_state:
            by_state[state] = []
        by_state[state].append(city)

    state_sections = []
    total = 0
    for state_name in sorted(by_state.keys()):
        cities = sorted(by_state[state_name], key=lambda c: c['city_name'])
        rows = []
        for c in cities:
            abbrev = c['state_abbrev']
            slug = c['city_slug']
            pop = c.get('population', '')
            gov = c.get('gov_type', '')
            rows.append(
                f'      <tr>'
                f'<td><a href="{abbrev}_{slug}.html"><strong>{html_escape(c["city_name"])}</strong></a></td>'
                f'<td>{html_escape(pop)}</td>'
                f'<td>{html_escape(gov)}</td>'
                f'</tr>'
            )
            total += 1

        table_rows = '\n'.join(rows)
        state_sections.append(f"""
    <h2>{html_escape(state_name)} ({len(cities)} cities)</h2>
    <table>
      <thead><tr><th>City</th><th>Population</th><th>Gov. Type</th></tr></thead>
      <tbody>
{table_rows}
      </tbody>
    </table>""")

    sections_html = '\n'.join(state_sections)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>City Flyers — Protections for Elections</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'DM Sans', sans-serif; background: #F1F5F9; padding: 40px 20px; }}
  .container {{ max-width: 900px; margin: 0 auto; }}
  h1 {{ font-family: 'DM Serif Display', serif; color: #0D3B1E; font-size: 32px; margin-bottom: 8px; }}
  p.subtitle {{ color: #475569; font-size: 14px; margin-bottom: 32px; }}
  h2 {{ font-family: 'DM Serif Display', serif; color: #14532D; font-size: 22px; margin: 28px 0 12px; padding-top: 16px; border-top: 2px solid #E2E8F0; }}
  h2:first-of-type {{ border-top: none; padding-top: 0; }}
  table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 16px; }}
  th {{ background: #14532D; color: white; text-align: left; padding: 10px 14px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.8px; }}
  td {{ padding: 8px 14px; border-bottom: 1px solid #E2E8F0; font-size: 13px; }}
  tr:hover {{ background: #F0FDF4; }}
  a {{ color: #166534; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<div class="container">
  <h1>City-Level Election Protection Flyers</h1>
  <p class="subtitle">{total} city flyers across {len(by_state)} states. Printable 5.5&quot; &times; 8.5&quot; format with local council details.</p>
{sections_html}
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Research Log Generation
# ---------------------------------------------------------------------------

def generate_research_log(all_cities, research_sources):
    """Generate RESEARCH_LOG.md documenting sources and gaps."""
    lines = [
        "# City Flyer Research Log\n",
        f"Generated: {len(all_cities)} city flyers\n",
        "",
    ]

    # Group by state
    by_state = {}
    for city in all_cities:
        state = city['state_name']
        if state not in by_state:
            by_state[state] = []
        by_state[state].append(city)

    gaps_count = 0
    for state_name in sorted(by_state.keys()):
        cities = sorted(by_state[state_name], key=lambda c: c['city_name'])
        lines.append(f"\n## {state_name}\n")
        for c in cities:
            key = f"{c['state_abbrev']}:{c['city_slug']}"
            source = research_sources.get(key, "State analysis markdown only")
            has_gaps = any(
                c.get(f) in ('', 'Check city website', 'Check')
                for f in ['contact_phone', 'city_hall_address', 'meeting_day']
            )
            if has_gaps:
                gaps_count += 1
                lines.append(f"- **{c['city_name']}** — Source: {source} ⚠ *Some fields incomplete*")
            else:
                lines.append(f"- **{c['city_name']}** — Source: {source}")

    lines.append(f"\n---\n\n**Summary:** {gaps_count} cities with incomplete council data.\n")
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# City Flyer Link Insertion into State Guides
# ---------------------------------------------------------------------------

def add_city_flyer_links(all_cities):
    """Add city flyer links to state guide pages below the existing Printable Flyer section."""
    # Group cities by state slug
    by_state = {}
    for city in all_cities:
        slug = city['state_slug']
        if slug not in by_state:
            by_state[slug] = []
        by_state[slug].append(city)

    count = 0
    for slug in sorted(by_state.keys()):
        cities = sorted(by_state[slug], key=lambda c: c['city_name'])
        md_path = STATE_GUIDES_DIR / f"{slug}.md"
        if not md_path.exists():
            continue

        text = md_path.read_text(encoding='utf-8')

        # Skip if already has city flyer links
        if '### City-Level Flyers' in text:
            continue

        # Build city flyer link block
        city_links = []
        for c in cities:
            abbrev = c['state_abbrev']
            city_link = (
                f'    - [:material-file-download: **{c["city_name"]}**]'
                f'(../flyers/city/{abbrev}_{c["city_slug"]}.html)'
                f'{{:target="_blank"}}'
            )
            city_links.append(city_link)

        block = (
            '\n### City-Level Flyers\n\n'
            f'!!! info "{len(cities)} City-Specific Election Protection Flyers"\n\n'
            '    Printable flyers with local council details for target cities:\n\n'
            + '\n'.join(city_links) + '\n'
        )

        # Insert after the Printable Flyer section
        if '## Printable Flyer' in text:
            # Find the end of the Printable Flyer section (next --- or ## or end)
            flyer_pos = text.index('## Printable Flyer')
            # Find the end of the tip admonition block
            rest = text[flyer_pos:]
            # Look for the end of the block (empty line after content ends)
            lines = rest.split('\n')
            insert_idx = len(lines)
            in_admonition = False
            for i, line in enumerate(lines):
                if line.strip().startswith('!!!'):
                    in_admonition = True
                elif in_admonition and line.strip() and not line.startswith('    '):
                    insert_idx = i
                    break
                elif in_admonition and not line.strip():
                    # Check if next non-empty line is indented
                    next_content = False
                    for j in range(i + 1, len(lines)):
                        if lines[j].strip():
                            if lines[j].startswith('    '):
                                next_content = True
                            break
                    if not next_content:
                        insert_idx = i + 1
                        break

            before = '\n'.join(lines[:insert_idx])
            after = '\n'.join(lines[insert_idx:])
            text = text[:flyer_pos] + before + block + after
        else:
            # No existing flyer section — append at end
            if not text.endswith('\n'):
                text += '\n'
            text += block

        md_path.write_text(text, encoding='utf-8')
        count += 1
        print(f"  Added city flyer links: {slug} ({len(cities)} cities)")

    return count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    filter_abbrev = None
    filter_city = None

    if len(sys.argv) > 1:
        filter_abbrev = sys.argv[1].upper()
    if len(sys.argv) > 2:
        filter_city = sys.argv[2].lower()

    # Load template
    template = TEMPLATE_PATH.read_text(encoding='utf-8')

    # Load council research data if available
    load_council_data_file()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    states_to_process = STATES
    if filter_abbrev:
        states_to_process = [(a, s, n) for a, s, n in STATES if a == filter_abbrev]
        if not states_to_process:
            print(f"ERROR: State abbreviation '{filter_abbrev}' not found.")
            sys.exit(1)

    all_cities = []
    research_sources = {}
    generated = 0
    errors = []

    for abbrev, slug, state_name in states_to_process:
        md_path = STATE_GUIDES_DIR / f"{slug}.md"
        if not md_path.exists():
            print(f"  SKIP {abbrev} — no markdown file")
            continue

        content = md_path.read_text(encoding='utf-8')
        content_body = re.sub(r'^---\n.*?\n---\n', '', content, count=1, flags=re.DOTALL)

        # Extract section 3
        section3 = extract_section(content_body, 3)
        if not section3:
            print(f"  SKIP {abbrev} — no Section 3 found")
            continue

        # Extract all cities
        cities = extract_all_cities(section3, state_name)

        # Supplement with cities from city_council_data.json not found by extraction
        extracted_slugs = {c['city_slug'] for c in cities}
        prefix = f"{abbrev}:"
        for key, cdata in COUNCIL_DATA.items():
            if not key.startswith(prefix):
                continue
            json_slug = key[len(prefix):]
            if json_slug in extracted_slugs:
                continue
            # Build a city entry from JSON data — use proper display name
            display_names = {
                'lexington-fayette': 'Lexington-Fayette',
                'kansas-city-ks': 'Kansas City, KS',
                'kansas-city-mo': 'Kansas City, MO',
                'columbia-mo': 'Columbia, MO',
                'st-louis-city': 'St. Louis City',
                'st-louis-county': 'St. Louis County',
                'st-paul': 'St. Paul',
                'st-petersburg': 'St. Petersburg',
                'la-crosse': 'La Crosse',
                'new-york-city': 'New York City',
                'salt-lake-city': 'Salt Lake City',
                'salt-lake-county': 'Salt Lake County',
                'jackson-teton-county': 'Jackson/Teton County',
                'bloomington-monroe-county': 'Bloomington/Monroe County',
                'indianapolis-marion-county': 'Indianapolis/Marion County',
                'johnson-county-iowa-city': 'Johnson County/Iowa City',
            }
            display_name = display_names.get(json_slug, json_slug.replace('-', ' ').title())
            cities.append({
                'city_name': display_name,
                'city_slug': json_slug,
                'population': cdata.get('population', ''),
                'gov_type': cdata.get('gov_type', ''),
                'charter_status': cdata.get('charter_status', ''),
                'governing_body': '',
                'council_size': cdata.get('council_size', ''),
                'description': '',
            })

        if not cities:
            print(f"  SKIP {abbrev} — no cities found")
            continue

        # Extract state legal context
        state_ctx = extract_state_context(content_body, state_name, abbrev)

        print(f"  {abbrev}: {len(cities)} cities found — ", end="")

        for city in cities:
            # Filter by city if specified
            if filter_city and city['city_slug'] != filter_city:
                continue

            # Merge state context
            city['state_name'] = state_name
            city['state_abbrev'] = abbrev
            city['state_slug'] = slug
            city['legal_authority'] = state_ctx['legal_authority']
            city['ordinance_description'] = state_ctx['ordinance_description']
            city['org_tags_html'] = state_ctx['org_tags_html']

            # Extract city-specific "why it works"
            city['why_it_works'] = extract_why_it_works(city.get('description', ''), city['city_name'])

            # Get council data (from pre-researched file or defaults)
            council = get_council_data(abbrev, city['city_slug'])
            for k, v in council.items():
                if k not in city or not city[k]:
                    city[k] = v

            # If council_size from extraction, use it
            if city.get('council_size') and not council.get('council_size'):
                pass  # keep extracted value

            # Render
            try:
                html = render_city_flyer(template, city)

                # Check for remaining placeholders
                remaining = re.findall(r'\{\{.*?\}\}', html)
                if remaining:
                    errors.append(f"{abbrev}_{city['city_slug']}: {len(remaining)} unresolved placeholders")

                # Write output
                out_path = OUTPUT_DIR / f"{abbrev}_{city['city_slug']}.html"
                out_path.write_text(html, encoding='utf-8')
                generated += 1

                all_cities.append(city)
                research_sources[f"{abbrev}:{city['city_slug']}"] = council.get(
                    '_source', 'State analysis markdown + defaults'
                )

            except Exception as e:
                errors.append(f"{abbrev}_{city['city_slug']}: {e}")

        city_names = [c['city_name'] for c in cities if not filter_city or c['city_slug'] == filter_city]
        print(', '.join(city_names) if city_names else 'filtered out')

    # Generate index
    if not filter_city:
        index_html = generate_index(all_cities)
        index_path = OUTPUT_DIR / "index.html"
        index_path.write_text(index_html, encoding='utf-8')
        print(f"\n  Index: {index_path}")

    # Generate research log
    log_content = generate_research_log(all_cities, research_sources)
    RESEARCH_LOG_PATH.write_text(log_content, encoding='utf-8')
    print(f"  Research log: {RESEARCH_LOG_PATH}")

    if errors:
        print(f"\n  ERRORS ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")

    print(f"\n  Generated {generated} city flyers in {OUTPUT_DIR}")

    # Add city flyer links to state guide pages
    if '--add-links' in sys.argv and not filter_city:
        print("\n  Adding city flyer links to state guide pages...")
        n = add_city_flyer_links(all_cities)
        print(f"  → {n} state guides updated with city flyer links")


if __name__ == '__main__':
    main()

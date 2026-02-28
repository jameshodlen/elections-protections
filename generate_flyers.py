#!/usr/bin/env python3
"""
Generate 50-state printable HTML flyers from state analysis markdown files.

Reads each state's markdown in docs/state-guides/, extracts structured data,
and renders flyer_template.html with the extracted values.

Usage:
    python3 generate_flyers.py              # Generate all 50 states
    python3 generate_flyers.py CO           # Generate Colorado only (for validation)
"""

import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "flyer_template.html"
STATE_GUIDES_DIR = BASE_DIR / "docs" / "state-guides"
OUTPUT_DIR = BASE_DIR / "docs" / "flyers"
GAPS_PATH = OUTPUT_DIR / "GAPS.md"

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

TIER_MAP = {
    "green": "Strong Viability",
    "yellow": "Moderate — Careful Framing Required",
    "red": "Challenging — Creative Strategy Needed",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_md(text):
    """Strip markdown bold/italic markers, headings, and clean up whitespace."""
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)  # strip headings
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # [text](url) -> text
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def html_escape(text):
    """Minimal HTML escaping for template values."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def first_sentences(text, n=2):
    """Extract first n sentences from text."""
    # Split on sentence boundaries
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
    for part in parts[1:]:  # skip text before first ###
        lines = part.split('\n', 1)
        heading = lines[0].strip()
        body = lines[1].strip() if len(lines) > 1 else ""
        result.append((heading, body))
    return result


def get_opening_paragraph(content):
    """Get the opening paragraph(s) between the first # heading and first ---."""
    # Find content after the first # heading
    m = re.search(r'^#\s+[^\n]+\n+(.*?)(?=\n---)', content, re.MULTILINE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


# ---------------------------------------------------------------------------
# Field Extractors
# ---------------------------------------------------------------------------

def extract_tier(content):
    """Extract tier from YAML frontmatter tags."""
    # Look in frontmatter
    fm = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm:
        frontmatter = fm.group(1)
        if 'tier-green' in frontmatter:
            return 'green'
        elif 'tier-yellow' in frontmatter:
            return 'yellow'
        elif 'tier-red' in frontmatter:
            return 'red'
    return 'red'  # default


def extract_home_rule(section1):
    """Extract home rule summary from Section 1."""
    subsections = extract_subsections(section1)

    # Find the home rule subsection
    for heading, body in subsections:
        if re.search(r'home\s*rule|article\s+(xi|xx|xii|iv|v)|municipal\s+power|legal\s+framework', heading, re.IGNORECASE):
            # Look for a strong summary sentence with constitutional reference
            lines = body.split('\n')
            for line in lines:
                line = line.strip()
                if not line or line.startswith('|') or line.startswith('-'):
                    continue
                cleaned = clean_md(line)
                # Look for lines with constitutional article or stats
                if re.search(r'(Article\s+[XIVL]+|Art\.\s+[XIVL]+|Constitution|home rule|Dillon)', cleaned, re.IGNORECASE):
                    # Truncate to reasonable length
                    result = first_sentences(cleaned, 1)
                    if len(result) > 120:
                        result = result[:117] + '...'
                    return result

    # Fallback: try the opening of section 1 itself
    lines = section1.split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('|'):
            continue
        cleaned = clean_md(line)
        if re.search(r'(home rule|Dillon|constitution|Article)', cleaned, re.IGNORECASE):
            result = first_sentences(cleaned, 1)
            if len(result) > 120:
                result = result[:117] + '...'
            return result

    return "See state guide for details"


def extract_key_advantage(opening_para, section1):
    """Extract the single strongest legal argument."""
    # Look for bold text in opening that sounds positive
    bold_phrases = re.findall(r'\*\*(.+?)\*\*', opening_para)
    positive_keywords = ['strong', 'favor', 'advantage', 'robust', 'no anti-sanctuary',
                         'repeal', 'protection', 'sanctuary', 'powerful', 'supports',
                         'ban', 'prohibit', 'first state', 'unique', 'already']

    # Try opening paragraph first - find sentences with positive signals
    sentences = re.split(r'(?<=[.!?])\s+', clean_md(opening_para))
    for sent in sentences:
        lower = sent.lower()
        if any(kw in lower for kw in positive_keywords) and len(sent) > 30:
            result = sent.strip()
            if len(result) > 180:
                result = result[:177] + '...'
            return result

    # Fallback: use first bold phrase from opening
    if bold_phrases:
        for phrase in bold_phrases:
            if len(phrase) > 20 and not re.search(r'(risk|barrier|hostile|weak|limit)', phrase, re.IGNORECASE):
                return phrase[:180]

    # Last resort: first substantial sentence from opening
    for sent in sentences:
        if len(sent) > 30:
            return first_sentences(sent, 1)[:180]

    return "See state guide for analysis"


def extract_key_risk(opening_para, section1):
    """Extract the single biggest legal obstacle."""
    risk_keywords = ['risk', 'challenge', 'barrier', 'preempt', 'hostile', 'weak',
                     'limit', 'restrict', 'obstacl', 'difficult',
                     'anti-sanctuary', 'dillon', 'block', 'criminal penalt',
                     'supermajor', 'conservative', 'turnaround', 'weaponiz',
                     'retaliatory', 'dangerous', 'aggressive']

    # Search opening paragraph for risk sentences
    sentences = re.split(r'(?<=[.!?])\s+', clean_md(opening_para))
    for sent in sentences:
        lower = sent.lower()
        if any(kw in lower for kw in risk_keywords) and len(sent) > 20:
            result = sent.strip()
            if len(result) > 180:
                result = result[:177] + '...'
            return result

    # Search the preemption subsection in Section 1
    subsections = extract_subsections(section1)
    for heading, body in subsections:
        if re.search(r'preemption|risk|challenge|barrier|landscape|weaponiz', heading, re.IGNORECASE):
            cleaned = clean_md(body)
            sents = re.split(r'(?<=[.!?])\s+', cleaned)
            # Look for risk-related sentences in this subsection
            for sent in sents:
                lower = sent.lower()
                if any(kw in lower for kw in risk_keywords) and len(sent) > 20:
                    result = sent.strip()
                    if len(result) > 180:
                        result = result[:177] + '...'
                    return result
            # Fallback: first sentence of the risk subsection
            if sents and len(sents[0]) > 30:
                first = sents[0]
                if len(first) > 180:
                    first = first[:177] + '...'
                return first

    # Search ALL subsections for any risk mention
    for heading, body in subsections:
        cleaned = clean_md(body)
        sents = re.split(r'(?<=[.!?])\s+', cleaned)
        for sent in sents:
            lower = sent.lower()
            if any(kw in lower for kw in risk_keywords) and len(sent) > 30:
                result = sent.strip()
                if len(result) > 180:
                    result = result[:177] + '...'
                return result

    return "See state guide for risk analysis"


def extract_recommended_framing(section1, section3):
    """Extract recommended ordinance framing strategy."""
    framing_keywords = ['fram', 'resource allocation', 'police power', 'draft',
                        'ordinance should', 'language must', 'recommended approach',
                        'should be framed', 'strategic recommendation', 'emphasis']

    # Check Section 3 for "Ordinance Drafting Principles" or "Recommended Approach"
    subsections = extract_subsections(section3)
    for heading, body in subsections:
        if re.search(r'(draft|fram|recommend|approach|principle)', heading, re.IGNORECASE):
            cleaned = clean_md(body)
            sents = re.split(r'(?<=[.!?])\s+', cleaned)
            for sent in sents:
                if any(kw in sent.lower() for kw in framing_keywords) and len(sent) > 20:
                    result = first_sentences(sent, 2)
                    if len(result) > 180:
                        result = result[:177] + '...'
                    return result
            # Fallback: first sentence of the subsection
            if sents and len(sents[0]) > 20:
                return first_sentences(sents[0], 2)[:180]

    # Check Section 1 for framing advice
    subsections = extract_subsections(section1)
    for heading, body in subsections:
        cleaned = clean_md(body)
        sents = re.split(r'(?<=[.!?])\s+', cleaned)
        for sent in sents:
            if any(kw in sent.lower() for kw in framing_keywords) and len(sent) > 30:
                result = first_sentences(sent, 1)
                if len(result) > 180:
                    result = result[:177] + '...'
                return result

    # Last resort: check the conclusion
    return "Police resource allocation under local authority"


def extract_anti_sanctuary(section1, opening_para, full_content):
    """Determine anti-sanctuary status and format note.

    Only searches Section 1 and opening paragraph to avoid false positives
    from references to other states' laws elsewhere in the document.
    """
    # Search Section 1, opening para, and sanctuary-related content from Sections 2 & 5
    # (Some states put anti-sanctuary info in statute tables or security sections)
    section2 = extract_section(full_content, 2)
    section5 = extract_section(full_content, 5)

    # Extract anti-sanctuary rows from tables in Section 2 and Section 5
    sanctuary_table_rows = ""
    for sec in [section2, section5]:
        for row in re.findall(r'\|[^|]*(?:sanctuary|anti-sanctuary)[^|]*\|[^\n]+', sec, re.IGNORECASE):
            sanctuary_table_rows += " " + row

    text = section1 + "\n" + opening_para + "\n" + sanctuary_table_rows

    # Find the sanctuary-specific subsection if it exists
    sanctuary_subsection = ""
    subsections = extract_subsections(section1)
    for heading, body in subsections:
        if re.search(r'sanctuary|anti-sanctuary|cooperation\s+mandate', heading, re.IGNORECASE):
            sanctuary_subsection = body

    # Explicit "no anti-sanctuary" patterns — clearly safe
    no_anti_sanctuary_patterns = [
        r'no anti-sanctuary\b',
        r'has no "?anti-sanctuary"? law',
        r'no anti-sanctuary preemption',
        r'does not have.*anti-sanctuary',
        r'has no.*anti-sanctuary',
    ]

    # Safe patterns — state PROTECTS sanctuary policies (not bans them)
    safe_patterns = [
        r'HB\s*19-1124',  # Colorado
        r'(?:SB|Senate Bill)\s*54.*(?:Values Act|sanctuary|protect)',  # California SB 54
        r'ORS\s*181A',  # Oregon
        r'(?:enacted|passed|adopted|maintains?|established|has)\s+(?:\w+\s+){0,3}sanctuary\s+(?:polic|ordinance|law|protect|status)',
        r'non-?cooperation\s+(?:polic|law|ordinance)',
        r'sanctuary\s+(?:state|city)\s+(?:protect|law|since)',
        r'limiting.*(?:local-?)?federal\s+(?:enforcement\s+)?cooperation',
    ]

    # Risk patterns — state HAS anti-sanctuary laws or mandates
    risk_patterns = [
        r'(?<!no\s)(?<!absence of\s)(?<!no )anti-sanctuary\s*(law|act|statute|legislation|preemption|city|provision|mandate|\||\*)',
        r'prohibit\w*\s+"?sanctuary\s*cit',
        r'ban\w*\s+(?:on\s+)?sanctuary',
        r'sanctuary\s*city\s*ban',
        r'(?:HB|SB)\s*\d+.*(?:anti-sanctuary|ban.*sanctuary|prohibit.*sanctuary)',
        r'Beason-Hammon',  # Alabama HB 56
        r'§\s*752\.053',  # Texas SB 4 cite
        r'cooperation\s*mandate.*(?:immigration|ICE|federal)',
        r'mandate.*cooperation.*(?:ICE|immigration)',
        r'penalt.*local\s*officials.*(?:sanctuary|non-?cooperat)',
        r'felony.*(?:officials?\s+voting\s+for\s+sanctuary|local\s*officials)',
        r'anti-sanctuary.*aggressive',
        r'Class\s+[A-E]\s+felony.*sanctuary',
    ]

    # Check the sanctuary subsection first if found (most reliable)
    if sanctuary_subsection:
        sub_text = sanctuary_subsection
        # Is the subsection about the state having protections or restrictions?
        for pat in no_anti_sanctuary_patterns:
            if re.search(pat, sub_text, re.IGNORECASE):
                detail = _find_sanctuary_detail(section1, opening_para, safe=True)
                return True, detail
        for pat in safe_patterns:
            if re.search(pat, sub_text, re.IGNORECASE):
                detail = _find_sanctuary_detail(section1, opening_para, safe=True)
                return True, detail
        for pat in risk_patterns:
            if re.search(pat, sub_text, re.IGNORECASE):
                detail = _find_sanctuary_detail(section1, opening_para, safe=False)
                return False, detail

    # Fall back to searching the broader section1 text
    # Check safe patterns first (since most green/yellow states are safe)
    for pat in no_anti_sanctuary_patterns:
        if re.search(pat, text, re.IGNORECASE):
            detail = _find_sanctuary_detail(section1, opening_para, safe=True)
            return True, detail

    for pat in safe_patterns:
        if re.search(pat, text, re.IGNORECASE):
            detail = _find_sanctuary_detail(section1, opening_para, safe=True)
            return True, detail

    # Check risk patterns
    for pat in risk_patterns:
        if re.search(pat, text, re.IGNORECASE):
            detail = _find_sanctuary_detail(section1, opening_para, safe=False)
            return False, detail

    # Default: if no sanctuary mentioned at all, consider safe
    lower_text = text.lower()
    if 'sanctuary' not in lower_text and 'anti-sanctuary' not in lower_text:
        return True, "✓ No specific anti-sanctuary law identified. See state guide."

    return True, "✓ See state guide for sanctuary law analysis."


def _find_sanctuary_detail(section1, opening_para, safe=True):
    """Build the anti-sanctuary note detail text."""
    # Strip subsection headings before splitting into sentences
    search_text = re.sub(r'###[^\n]+\n', '\n', section1) + "\n" + opening_para

    # Look for sentences about sanctuary/anti-sanctuary
    sentences = re.split(r'(?<=[.!?])\s+', clean_md(search_text))
    sanctuary_sents = []
    for sent in sentences:
        lower = sent.lower()
        if 'sanctuary' in lower or 'anti-sanctuary' in lower or 'cooperation' in lower:
            if len(sent) > 15:
                sanctuary_sents.append(sent)

    if safe:
        prefix = "✓"
        # Look for sentences explaining safety
        for sent in sanctuary_sents:
            lower = sent.lower()
            if any(w in lower for w in ['no anti', 'protect', 'no legal barrier', 'has no', 'none']):
                result = sent.strip()
                if len(result) > 150:
                    result = result[:147] + '...'
                return f"✓ {result}" if not result.startswith("✓") else result
        if sanctuary_sents:
            return f"✓ {sanctuary_sents[0][:150]}"
        return "✓ No anti-sanctuary law. No legal barrier."
    else:
        prefix = "⚠"
        for sent in sanctuary_sents:
            lower = sent.lower()
            if any(w in lower for w in ['anti-sanctuary', 'penalty', 'mandate', 'prohibit', 'require']):
                result = sent.strip()
                if len(result) > 150:
                    result = result[:147] + '...'
                return f"⚠ {result}" if not result.startswith("⚠") else result
        if sanctuary_sents:
            return f"⚠ {sanctuary_sents[0][:150]}"
        return "⚠ Anti-sanctuary provisions may apply. Requires careful framing."


def extract_cities(section3, state_name):
    """Extract up to 3 target cities from Section 3."""
    cities = []

    # Pattern 1: ### CityName (Primary Target) or ### CityName -- Population
    city_headings = re.finditer(
        r'###\s+(?:#?\d+\s+)?(.+?)(?:\s*\((?:Primary|Secondary|Scale|Additional|University|Tertiary)\s*Target\))?'
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

        # Skip non-city headings
        skip_words = ['deprioritize', 'non-starter', 'county-level', 'ordinance',
                      'cities to', 'recommended', 'additional target', 'strategic',
                      'drafting', 'general note', 'no city', 'tier 1', 'tier 2',
                      'tier 3', 'highest priority', 'strong secondary', 'recent campaign',
                      'model', 'overview']
        if any(w in raw_name.lower() for w in skip_words):
            continue

        # Clean city name - remove things like "offers the ideal" etc
        city_name = re.split(r'\s+(?:offer|provid|lead|creat|has\s|is\s|—|:)', raw_name)[0].strip()
        city_name = re.sub(r'\s*\([^)]*\)\s*$', '', city_name).strip()
        # Handle "CityName, KS" or "Kansas City, KS / Wyandotte County..."
        city_name = re.split(r'\s*/\s*', city_name)[0].strip()
        # Remove trailing possessives and descriptors
        city_name = re.sub(r"'s\s+.*$", '', city_name).strip()

        if len(city_name) > 30 or len(city_name) < 2:
            continue

        # Extract population
        pop = pop_from_heading
        if not pop:
            pop_match = re.search(r'\*\*Population:?\*\*\s*~?([\d,]+)', body)
            if not pop_match:
                pop_match = re.search(r'Pop(?:ulation)?\.?\s*~?([\d,]+)', body)
            if pop_match:
                pop = pop_match.group(1)

        # Format population
        pop_str = ""
        if pop:
            pop_num = int(pop.replace(',', ''))
            if pop_num >= 1_000_000:
                pop_str = f"Pop. {pop_num / 1_000_000:.1f}M"
            else:
                pop_str = f"Pop. {pop_num // 1000}K"

        # Extract government type
        gov_match = re.search(
            r'(Charter|Home Rule|Council-Manager|Mayor-Council|Strong Mayor|'
            r'Commission-Manager|Oldest Charter|Code City|Code Home Rule|'
            r'Commission|Unified Government|First-Class)',
            body, re.IGNORECASE
        )
        gov_type = gov_match.group(1).title() if gov_match else ""

        # Build city_meta
        meta_parts = [p for p in [pop_str, gov_type] if p]
        city_meta = " • ".join(meta_parts) if meta_parts else "See state guide"

        # Build city_why - look for a strong hook in the body
        why = _extract_city_why(body, city_name)

        cities.append({
            'name': city_name,
            'meta': city_meta,
            'why': why,
        })

        if len(cities) >= 3:
            break

    # Pattern 2: Narrative paragraph format with **CityName** as bold text
    # Used by Maryland, New York, Ohio, etc.
    if not cities:
        cities = _extract_cities_from_paragraphs(section3, state_name)

    # Pattern 3: Bullet list format: - **CityName** — description
    if not cities:
        cities = _extract_cities_from_bullets(section3)

    # Pattern 4: Table format (Wyoming, etc.)
    if not cities:
        cities = _extract_cities_from_table(section3, state_name)

    # Pattern 5: Default cities for states with no data
    if not cities:
        cities = _default_cities(state_name)

    return cities[:3]


def _extract_cities_from_bullets(section3):
    """Extract cities from bullet list format: - **CityName** — description."""
    cities = []
    bullet_matches = re.finditer(
        r'[-*]\s+\*\*([^*]+?)\*\*\s*(?:—|--|-)\s*(.+)',
        section3
    )
    for match in bullet_matches:
        name = match.group(1).strip()
        desc = match.group(2).strip()

        # Skip non-city entries
        if len(name) > 30 or len(name) < 2:
            continue

        why = f"<strong>{name}.</strong> {clean_md(desc)[:60]}"
        if len(why) > 100:
            why = why[:97] + '...'

        cities.append({
            'name': name,
            'meta': 'See state guide',
            'why': why,
        })

        if len(cities) >= 3:
            break

    return cities


def _default_cities(state_name):
    """Provide default cities for states with no specific target city data."""
    defaults = {
        'Georgia': [
            {'name': 'Atlanta', 'meta': 'Pop. 499K • Charter', 'why': '<strong>Largest city.</strong> Progressive council, existing civil rights infrastructure.'},
            {'name': 'Savannah', 'meta': 'Pop. 147K • Charter', 'why': '<strong>Historic city.</strong> Democratic mayor, strong community organizations.'},
            {'name': 'Athens', 'meta': 'Pop. 127K • Unified Gov.', 'why': '<strong>University city.</strong> Progressive unified government, activist base.'},
        ],
        'Mississippi': [
            {'name': 'Jackson', 'meta': 'Pop. 153K • Charter', 'why': '<strong>State capital.</strong> Democratic mayor, civil rights legacy.'},
            {'name': 'Hattiesburg', 'meta': 'Pop. 48K • Code Charter', 'why': '<strong>University city.</strong> Progressive leadership, Southern Miss campus.'},
        ],
    }
    return defaults.get(state_name, [])


def _extract_cities_from_paragraphs(section3, state_name):
    """Extract cities from narrative paragraph format where city names are bold."""
    cities = []

    # Find paragraphs that start with **CityName** at the beginning of a line
    # This handles formats like:
    #   **Baltimore City** emerges as the strongest...
    #   **New York City** represents the highest-impact...
    #   **Columbus** offers the strongest foundation...
    para_matches = re.finditer(
        r'(?:^|\n)\s*\*\*([A-Z][^*]{2,40}?)\*\*\s+((?:(?:emerges?|represents?|offers?|provides?|presents?|ranks?|combines?|has|is|the|operates?|leads?)\b)[^\n]*(?:\n(?!\s*\*\*[A-Z]|\s*###|\s*##|\s*\n\s*\*\*[A-Z]).*)*)',
        section3,
        re.MULTILINE
    )

    for match in para_matches:
        raw_name = match.group(1).strip()
        body = match.group(2).strip()

        # Skip non-city entries
        skip_words = ['population', 'key consideration', 'governing body',
                      'weakness', 'note', 'secondary target', 'the most',
                      'no city', 'target city']
        if any(w in raw_name.lower() for w in skip_words):
            continue

        # Remove trailing descriptors from name
        city_name = raw_name.strip()
        if len(city_name) > 30 or len(city_name) < 2:
            continue

        # Extract population from body
        pop_match = re.search(r'(?:~|approximately\s+)([\d,]+(?:,\d+)*)\s*(?:residents|population|people)?', body)
        if not pop_match:
            pop_match = re.search(r'([\d,]+(?:,\d+)*)-member', body)
        pop_str = ""
        if pop_match:
            try:
                pop_num = int(pop_match.group(1).replace(',', ''))
                if pop_num >= 100_000:  # Only use if it looks like population, not council size
                    if pop_num >= 1_000_000:
                        pop_str = f"Pop. {pop_num / 1_000_000:.1f}M"
                    else:
                        pop_str = f"Pop. {pop_num // 1000}K"
            except ValueError:
                pass

        # Extract government type
        gov_match = re.search(
            r'(Charter|Home Rule|Council-Manager|Mayor-Council|Strong Mayor|'
            r'Commission-Manager|Oldest Charter|Code City|Independent City|'
            r'Commission|Unified Government|First-Class|council-manager)',
            body, re.IGNORECASE
        )
        gov_type = gov_match.group(1).title() if gov_match else ""

        meta_parts = [p for p in [pop_str, gov_type] if p]
        city_meta = " • ".join(meta_parts) if meta_parts else "See state guide"

        # Build city_why
        cleaned = clean_md(body)
        why = _make_hook(first_sentences(cleaned, 1))

        cities.append({
            'name': city_name,
            'meta': city_meta,
            'why': why,
        })

        if len(cities) >= 3:
            break

    return cities


def _extract_city_why(body, city_name):
    """Extract a concise 'why this city' from body text."""
    cleaned = clean_md(body)
    sentences = re.split(r'(?<=[.!?])\s+', cleaned)

    # Look for a sentence with a strong hook
    hook_keywords = ['launch', 'optimal', 'strongest', 'best', 'most', 'highest',
                     'key', 'critical', 'unique', 'progressive', 'flip', 'largest',
                     'visibility', 'symbolic', 'first', 'only', 'proven']

    for sent in sentences:
        lower = sent.lower()
        if any(kw in lower for kw in hook_keywords) and 20 < len(sent) < 200:
            # Create a hook + reason format
            hook = _make_hook(sent)
            return hook

    # Fallback: use first substantial sentence
    for sent in sentences:
        if 20 < len(sent) < 200 and not sent.startswith('Population') and not sent.startswith('Governing'):
            return _make_hook(sent)

    return f"<strong>Target city.</strong> See state guide for details."


def _make_hook(sentence):
    """Format a sentence into <strong>Hook.</strong> + reason format, ≤80 chars."""
    # Try to extract a 2-3 word hook
    words = sentence.split()
    if len(words) >= 3:
        hook_words = words[:2]
        hook = ' '.join(hook_words)
        rest = ' '.join(words[2:])

        # Better hook: look for an adjective+noun at the start
        m = re.match(r'^([\w]+\s+[\w]+(?:\s+[\w]+)?)[.,]?\s*(.*)', sentence)
        if m and len(m.group(1)) < 25:
            hook = m.group(1).rstrip('.,')
            rest = m.group(2) if m.group(2) else ' '.join(words[3:])

        result = f"<strong>{hook}.</strong> {rest}"
        if len(result) > 100:
            result = result[:97] + '...'
        return result

    return f"<strong>Target.</strong> {sentence[:70]}"


def _extract_cities_from_table(section3, state_name):
    """Extract cities from markdown table format."""
    cities = []
    # Look for table rows with city data
    rows = re.findall(r'\|\s*\*?\*?([^|*]+?)\*?\*?\s*\|\s*~?([\d,]+)\s*\|([^|]+)\|', section3)

    for row in rows:
        name = row[0].strip()
        pop = row[1].strip()
        rest = row[2].strip()

        # Skip header rows
        if name.lower() in ('municipality', 'city', 'target', '-', '---', 'state'):
            continue
        if re.match(r'^-+$', name):
            continue

        pop_num = int(pop.replace(',', ''))
        if pop_num >= 1_000_000:
            pop_str = f"Pop. {pop_num / 1_000_000:.1f}M"
        elif pop_num >= 1000:
            pop_str = f"Pop. {pop_num // 1000}K"
        else:
            pop_str = f"Pop. {pop_num}"

        # Clean name
        name = re.sub(r'\[([^\]]+)\].*', r'\1', name).strip()

        cities.append({
            'name': name,
            'meta': pop_str,
            'why': f"<strong>Target city.</strong> {clean_md(rest)[:60]}",
        })

        if len(cities) >= 3:
            break

    return cities


def extract_orgs(section4, state_name, state_abbrev):
    """Extract 3-5 coalition partner organizations from Section 4."""
    orgs = []

    # Pattern 1: **Org Name** at start of line or after bullet
    org_matches = re.findall(r'(?:^|\n)\s*[-*]?\s*\*\*([^*]+?)\*\*', section4)

    # Pattern 2: Numbered list items
    if not org_matches:
        org_matches = re.findall(r'\d+\.\s*\*\*([^*]+?)\*\*', section4)

    seen = set()
    for org in org_matches:
        org = org.strip()
        # Skip non-org entries
        skip = ['key', 'contact', 'opposition', 'governor', 'ag ', 'attorney general',
                'legislature', 'secretary', 'republican', 'population', 'status',
                'anti-sanctuary', 'legislative', 'judicial', 'strategic', 'note',
                'weakness', 'key consideration', 'governing body', 'probability']
        if any(s in org.lower() for s in skip):
            continue
        if len(org) < 3 or len(org) > 60:
            continue

        # Abbreviate long names
        org = _abbreviate_org(org)

        if org.lower() not in seen:
            seen.add(org.lower())
            orgs.append(org)

        if len(orgs) >= 5:
            break

    # Defaults if nothing found
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


def _abbreviate_org(name):
    """Abbreviate long organization names."""
    replacements = [
        (r'League of Women Voters of\s+', 'LWV '),
        (r'League of Women Voters\s+', 'LWV '),
        (r'American Civil Liberties Union of\s+', 'ACLU of '),
        (r'Colorado Immigrant Rights Coalition', 'CIRC'),
        (r'National Association for the Advancement of Colored People', 'NAACP'),
    ]
    for pattern, repl in replacements:
        name = re.sub(pattern, repl, name)

    # Add member count if in parens
    # Already handled in source data

    if len(name) > 35:
        name = name[:32] + '...'

    return name


def extract_tagline(section1, opening_para, state_name, tier_class):
    """Compose a tagline: home rule type + distinctive legal feature (≤80 chars)."""
    text = section1 + "\n" + opening_para

    # Determine home rule type
    hr_type = "Home Rule"
    if re.search(r'constitutional\s+home\s*rule|constitution.*home\s*rule', text, re.IGNORECASE):
        hr_type = "Constitutional Home Rule"
    elif re.search(r"strict\s+dillon'?s?\s+rule", text, re.IGNORECASE):
        hr_type = "Dillon's Rule"
    elif re.search(r"dillon'?s?\s+rule\s+(?:state|with|but)", text, re.IGNORECASE):
        hr_type = "Dillon's Rule"
    elif re.search(r'statutory\s+home\s*rule', text, re.IGNORECASE):
        hr_type = "Statutory Home Rule"
    elif re.search(r'home\s*rule.*(?:strongest|strong|broad|robust|expansive)', text, re.IGNORECASE):
        hr_type = "Strong Home Rule"

    # Find distinctive legal feature from opening paragraph
    feature = ""
    feature_patterns = [
        r'first\s+state\s+to\s+(\w[\w\s]+?)(?:\.|,)',
        r'nation-leading\s+(\w[\w\s]+?)(?:\.|,)',
        r'strongest\s+(\w[\w\s]+?)(?:\.|,)',
        r'only\s+state\s+(?:to\s+|that\s+)(\w[\w\s]+?)(?:\.|,)',
        r'unique\s+(\w[\w\s]+?)(?:\.|,)',
    ]

    cleaned_opening = clean_md(opening_para)
    for pat in feature_patterns:
        m = re.search(pat, cleaned_opening, re.IGNORECASE)
        if m:
            feature = m.group(1).strip()
            feature = feature[:40]
            break

    if not feature:
        # Look for bold distinctive claims
        bold_phrases = re.findall(r'\*\*(.+?)\*\*', opening_para)
        for phrase in bold_phrases:
            if len(phrase) > 10 and not re.search(r'(section|overview|tier|18 u\.s\.c)', phrase, re.IGNORECASE):
                feature = phrase[:40]
                break

    if not feature:
        # Fallback features by tier
        if tier_class == 'green':
            feature = "Favorable Legal Environment"
        elif tier_class == 'yellow':
            feature = "Viable with Careful Strategy"
        else:
            feature = "Creative Strategy Needed"

    tagline = f"{hr_type} • {feature}"
    if len(tagline) > 80:
        # Trim the feature
        max_feat = 80 - len(hr_type) - 3  # " • "
        feature = feature[:max_feat]
        tagline = f"{hr_type} • {feature}"

    return tagline


# ---------------------------------------------------------------------------
# Colorado Reference Data (hardcoded for validation)
# ---------------------------------------------------------------------------

COLORADO_REFERENCE = {
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
    "anti_sanctuary_safe": True,
    "city1_name": "Boulder",
    "city1_meta": "Pop. 105K • Charter",
    "city1_why": "<strong>Launch city.</strong> Sanctuary ord., police oversight panel, progressive 9-member council.",
    "city2_name": "Denver",
    "city2_meta": "Pop. 715K • Oldest Charter",
    "city2_why": "<strong>Max visibility.</strong> Immigration ord. already limits fed cooperation. 13-member council.",
    "city3_name": "Aurora",
    "city3_meta": "Pop. 386K • Charter",
    "city3_why": "<strong>Time-sensitive.</strong> Nov '25 flipped council to 6-4 progressive. 3rd largest city.",
    "org_tags_html": '<span class="partner-tag">COVRA (45+ orgs)</span><span class="partner-tag">CO Common Cause</span><span class="partner-tag">ACLU of CO</span><span class="partner-tag">LWV Colorado</span><span class="partner-tag">CIRC (80+ orgs)</span>',
}


# ---------------------------------------------------------------------------
# Main extraction pipeline
# ---------------------------------------------------------------------------

def extract_state_data(abbrev, slug, name, md_path):
    """Extract all flyer fields from a state's markdown file."""
    content = md_path.read_text(encoding='utf-8')

    # Use hardcoded data for Colorado
    if abbrev == "CO":
        return COLORADO_REFERENCE.copy()

    # Extract sections
    tier_class = extract_tier(content)
    tier_label = TIER_MAP.get(tier_class, "Strong Viability")

    # Strip frontmatter for content parsing
    content_body = re.sub(r'^---\n.*?\n---\n', '', content, count=1, flags=re.DOTALL)

    opening_para = get_opening_paragraph(content_body)
    section1 = extract_section(content_body, 1)
    section3 = extract_section(content_body, 3)
    section4 = extract_section(content_body, 4)

    # Extract fields
    home_rule = extract_home_rule(section1)
    key_advantage = extract_key_advantage(opening_para, section1)
    key_risk = extract_key_risk(opening_para, section1)
    recommended_framing = extract_recommended_framing(section1, section3)
    anti_sanctuary_safe, anti_sanctuary_note = extract_anti_sanctuary(section1, opening_para, content_body)
    tagline = extract_tagline(section1, opening_para, name, tier_class)
    cities = extract_cities(section3, name)
    orgs = extract_orgs(section4, name, abbrev)

    # Build org tags HTML
    org_tags = ''.join(f'<span class="partner-tag">{html_escape(org)}</span>' for org in orgs)

    data = {
        "state_name": name,
        "state_abbrev": abbrev,
        "state_slug": slug,
        "tier_class": tier_class,
        "tier_label": tier_label,
        "state_tagline": tagline,
        "home_rule": html_escape(home_rule),
        "key_advantage": html_escape(key_advantage),
        "key_risk": html_escape(key_risk),
        "recommended_framing": html_escape(recommended_framing),
        "anti_sanctuary_note": anti_sanctuary_note,
        "anti_sanctuary_safe": anti_sanctuary_safe,
        "org_tags_html": org_tags,
    }

    # Add city data
    for i in range(3):
        idx = i + 1
        if i < len(cities):
            data[f"city{idx}_name"] = html_escape(cities[i]['name'])
            data[f"city{idx}_meta"] = html_escape(cities[i]['meta'])
            data[f"city{idx}_why"] = cities[i]['why']  # Already has HTML tags
        else:
            data[f"city{idx}_name"] = ""
            data[f"city{idx}_meta"] = ""
            data[f"city{idx}_why"] = ""

    return data


def render_flyer(template, data):
    """Render the template with extracted data, handling conditional styling."""
    html = template

    # Replace all {{ placeholder }} values
    html = html.replace('{{ state_name }}', data['state_name'])
    html = html.replace('{{ state_slug }}', data['state_slug'])
    html = html.replace('{{ tier_class }}', data['tier_class'])
    html = html.replace('{{ tier_label }}', data['tier_label'])
    html = html.replace('{{ state_tagline }}', data['state_tagline'])
    html = html.replace('{{ home_rule }}', data['home_rule'])
    html = html.replace('{{ key_advantage }}', data['key_advantage'])
    html = html.replace('{{ key_risk }}', data['key_risk'])
    html = html.replace('{{ recommended_framing }}', data['recommended_framing'])
    html = html.replace('{{ anti_sanctuary_note }}', data['anti_sanctuary_note'])
    html = html.replace('{{ city1_name }}', data.get('city1_name', ''))
    html = html.replace('{{ city1_meta }}', data.get('city1_meta', ''))
    html = html.replace('{{ city1_why }}', data.get('city1_why', ''))
    html = html.replace('{{ city2_name }}', data.get('city2_name', ''))
    html = html.replace('{{ city2_meta }}', data.get('city2_meta', ''))
    html = html.replace('{{ city2_why }}', data.get('city2_why', ''))
    html = html.replace('{{ city3_name }}', data.get('city3_name', ''))
    html = html.replace('{{ city3_meta }}', data.get('city3_meta', ''))
    html = html.replace('{{ city3_why }}', data.get('city3_why', ''))
    html = html.replace('{{ org_tags }}', data.get('org_tags_html', ''))

    # Handle anti-sanctuary styling swap (green -> amber when risky)
    if not data.get('anti_sanctuary_safe', True):
        html = html.replace(
            'style="border-left-color: var(--green-400); background: var(--green-50);"',
            'style="border-left-color: #F59E0B; background: #FEF9C3;"'
        )
        html = html.replace(
            'style="color: var(--green-700);"',
            'style="color: #92400E;"'
        )

    # Remove empty city cards
    for i in range(1, 4):
        if not data.get(f'city{i}_name'):
            # Remove the entire city-card div for this city
            pattern = (
                r'<div class="city-card">\s*'
                r'<div class="city-name"></div>\s*'
                r'<div class="city-meta"></div>\s*'
                r'<div class="city-why"></div>\s*'
                r'</div>'
            )
            html = re.sub(pattern, '', html, count=1)

    return html


def generate_index(generated_states):
    """Generate index.html listing all flyers."""
    rows = []
    for abbrev, slug, name, tier_class in sorted(generated_states, key=lambda x: x[2]):
        color_map = {'green': '#16A34A', 'yellow': '#EAB308', 'red': '#EF4444'}
        color = color_map.get(tier_class, '#888')
        tier_label = TIER_MAP.get(tier_class, '')
        rows.append(
            f'      <tr>'
            f'<td><span style="display:inline-block;width:10px;height:10px;'
            f'border-radius:50%;background:{color};margin-right:8px;"></span>'
            f'<a href="{abbrev}_flyer.html"><strong>{name}</strong></a></td>'
            f'<td>{abbrev}</td>'
            f'<td style="color:{color};font-weight:600;">{tier_label}</td>'
            f'</tr>'
        )

    table_rows = '\n'.join(rows)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>50-State Flyers — Protections for Elections</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'DM Sans', sans-serif; background: #F1F5F9; padding: 40px 20px; }}
  .container {{ max-width: 800px; margin: 0 auto; }}
  h1 {{ font-family: 'DM Serif Display', serif; color: #0D3B1E; font-size: 32px; margin-bottom: 8px; }}
  p.subtitle {{ color: #475569; font-size: 14px; margin-bottom: 24px; }}
  table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
  th {{ background: #0D3B1E; color: white; text-align: left; padding: 12px 16px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; }}
  td {{ padding: 10px 16px; border-bottom: 1px solid #E2E8F0; font-size: 14px; }}
  tr:hover {{ background: #F0FDF4; }}
  a {{ color: #166534; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<div class="container">
  <h1>50-State Election Protection Flyers</h1>
  <p class="subtitle">Printable 5.5&quot; &times; 8.5&quot; flyers with state-specific legal analysis, target cities, and coalition partners.</p>
  <table>
    <thead>
      <tr><th>State</th><th>Code</th><th>Viability Tier</th></tr>
    </thead>
    <tbody>
{table_rows}
    </tbody>
  </table>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Parse args
    filter_abbrev = sys.argv[1].upper() if len(sys.argv) > 1 else None

    # Load template
    template = TEMPLATE_PATH.read_text(encoding='utf-8')

    # Create output dir
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    gaps = []
    generated = []

    states_to_process = STATES
    if filter_abbrev:
        states_to_process = [(a, s, n) for a, s, n in STATES if a == filter_abbrev]
        if not states_to_process:
            print(f"ERROR: State abbreviation '{filter_abbrev}' not found.")
            sys.exit(1)

    for abbrev, slug, name in states_to_process:
        md_path = STATE_GUIDES_DIR / f"{slug}.md"
        if not md_path.exists():
            gaps.append(f"- **{name} ({abbrev})**: Markdown file not found at {md_path}")
            print(f"  SKIP {abbrev} — no markdown file")
            continue

        print(f"  Processing {abbrev} ({name})...", end=" ")

        try:
            data = extract_state_data(abbrev, slug, name, md_path)

            # Check for gaps in extracted data
            state_gaps = []
            for field in ['home_rule', 'key_advantage', 'key_risk', 'recommended_framing']:
                val = data.get(field, '')
                if 'See state guide' in val or not val:
                    state_gaps.append(field)

            if not data.get('city1_name'):
                state_gaps.append('target_cities')

            if state_gaps:
                gaps.append(f"- **{name} ({abbrev})**: Incomplete fields: {', '.join(state_gaps)}")

            # Render flyer
            html = render_flyer(template, data)

            # Verify no remaining placeholders
            remaining = re.findall(r'\{\{.*?\}\}', html)
            if remaining:
                gaps.append(f"- **{name} ({abbrev})**: Unresolved placeholders: {remaining}")
                print(f"WARNING — {len(remaining)} unresolved placeholders")
            else:
                print("OK")

            # Write output
            out_path = OUTPUT_DIR / f"{abbrev}_flyer.html"
            out_path.write_text(html, encoding='utf-8')
            generated.append((abbrev, slug, name, data['tier_class']))

        except Exception as e:
            gaps.append(f"- **{name} ({abbrev})**: Error during processing: {e}")
            print(f"ERROR — {e}")

    # Generate index
    if not filter_abbrev:
        index_html = generate_index(generated)
        index_path = OUTPUT_DIR / "index.html"
        index_path.write_text(index_html, encoding='utf-8')
        print(f"\n  Index: {index_path}")

    # Write gaps file
    if gaps:
        gaps_content = "# Flyer Generation Gaps\n\n"
        gaps_content += "The following states had missing or incomplete data:\n\n"
        gaps_content += '\n'.join(gaps) + '\n'
        GAPS_PATH.write_text(gaps_content, encoding='utf-8')
        print(f"\n  Gaps logged: {GAPS_PATH}")
    else:
        # Write empty gaps file
        GAPS_PATH.write_text("# Flyer Generation Gaps\n\nNo gaps detected. All 50 states generated successfully.\n", encoding='utf-8')

    print(f"\n  Generated {len(generated)} flyers in {OUTPUT_DIR}")


if __name__ == '__main__':
    main()

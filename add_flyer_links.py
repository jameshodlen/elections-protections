#!/usr/bin/env python3
"""Add flyer download links to state guide pages and comparison tables.

Modifies:
  - docs/state-guides/*.md (50 files) — appends Printable Flyer section
  - docs/state-guides/index.md — adds Flyer column to 3 tier tables
  - docs/legal-foundation/50-state-overview.md — adds Flyer column to 50-state table
"""

import re
from pathlib import Path

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

SLUG_TO_ABBREV = {slug: abbrev for abbrev, slug, _ in STATES}
SLUG_TO_NAME = {slug: name for _, slug, name in STATES}

DOCS = Path("docs")
STATE_GUIDES = DOCS / "state-guides"
OVERVIEW_FILE = DOCS / "legal-foundation" / "50-state-overview.md"
INDEX_FILE = STATE_GUIDES / "index.md"


def flyer_section(name: str, abbrev: str) -> str:
    """Build the markdown block to append to a state guide page."""
    return (
        "\n---\n\n"
        "## Printable Flyer\n\n"
        f'!!! tip "Download the {name} Election Protection Flyer"\n\n'
        f"    A printable 5.5\" × 8.5\" flyer with {name}-specific legal analysis,\n"
        "    target cities, and coalition partners.\n\n"
        f'    [:material-file-download: **View & Download Flyer**](../flyers/{abbrev}_flyer.html){{:target="_blank" .md-button .md-button--primary}}\n\n'
        "    *Open the flyer in your browser, then use **File → Print** or **Ctrl+P** to\n"
        '    print or save as PDF. The flyer is optimized for half-letter (5.5" × 8.5") printing.*\n'
    )


def append_flyer_sections() -> int:
    """Append flyer section to each state guide markdown file. Returns count."""
    count = 0
    for abbrev, slug, name in STATES:
        path = STATE_GUIDES / f"{slug}.md"
        if not path.exists():
            print(f"  SKIP (not found): {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if "## Printable Flyer" in text:
            print(f"  SKIP (already has flyer section): {slug}")
            continue
        # Ensure file ends with newline before appending
        if not text.endswith("\n"):
            text += "\n"
        text += flyer_section(name, abbrev)
        path.write_text(text, encoding="utf-8")
        count += 1
        print(f"  Added flyer section: {slug}")
    return count


def extract_slug_from_link(cell: str) -> str | None:
    """Extract the state slug from a markdown link in a table cell.

    Handles patterns like:
      [Colorado](colorado.md)
      **[Alabama](../state-guides/alabama.md)**
    """
    m = re.search(r'\((?:\.\./state-guides/)?([a-z-]+)\.md\)', cell)
    if m:
        return m.group(1)
    return None


def add_flyer_column_to_index() -> bool:
    """Add Flyer column to the 3 tier tables in state-guides/index.md."""
    text = INDEX_FILE.read_text(encoding="utf-8")

    if "| Flyer |" in text:
        print("  SKIP (index.md already has Flyer column)")
        return False

    lines = text.split("\n")
    new_lines = []
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Detect table header rows (they contain "| Guide |")
        if stripped.startswith("|") and "| Guide |" in stripped:
            line = line.rstrip().rstrip("|").rstrip() + " | Flyer |"
            new_lines.append(line)
            in_table = True
            continue

        # Detect separator rows right after header
        if in_table and stripped.startswith("|") and re.match(r'^\|[\s\-|]+\|$', stripped):
            line = line.rstrip().rstrip("|").rstrip() + "|---|"
            new_lines.append(line)
            continue

        # Data rows in a table
        if in_table and stripped.startswith("|") and not stripped.startswith("|---"):
            slug = extract_slug_from_link(stripped)
            if slug and slug in SLUG_TO_ABBREV:
                abbrev = SLUG_TO_ABBREV[slug]
                flyer_link = f'[:material-printer: Flyer](../flyers/{abbrev}_flyer.html){{:target="_blank"}}'
                line = line.rstrip().rstrip("|").rstrip() + f" | {flyer_link} |"
            new_lines.append(line)
            continue

        # Non-table line — reset table state
        if in_table and not stripped.startswith("|"):
            in_table = False

        new_lines.append(line)

    INDEX_FILE.write_text("\n".join(new_lines), encoding="utf-8")
    print("  Added Flyer column to index.md tables")
    return True


def add_flyer_column_to_overview() -> bool:
    """Add Flyer column to the 50-state table in 50-state-overview.md."""
    text = OVERVIEW_FILE.read_text(encoding="utf-8")

    if "Flyer |" in text:
        print("  SKIP (50-state-overview.md already has Flyer column)")
        return False

    lines = text.split("\n")
    new_lines = []
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Detect the 50-state table header (contains "Target Cities")
        if (stripped.startswith("|") and "Target Cities" in stripped
                and "Home Rule" in stripped):
            line = line.rstrip().rstrip("|").rstrip() + " | Flyer |"
            new_lines.append(line)
            in_table = True
            continue

        # Separator row
        if in_table and stripped.startswith("|") and re.match(r'^\|[\s\-|]+\|$', stripped):
            line = line.rstrip().rstrip("|").rstrip() + "|---|"
            new_lines.append(line)
            continue

        # Data rows
        if in_table and stripped.startswith("|") and "**[" in stripped:
            slug = extract_slug_from_link(stripped)
            if slug and slug in SLUG_TO_ABBREV:
                abbrev = SLUG_TO_ABBREV[slug]
                name = SLUG_TO_NAME[slug]
                flyer_link = f'[:material-printer:](../flyers/{abbrev}_flyer.html){{:target="_blank" title="{name} flyer"}}'
                line = line.rstrip().rstrip("|").rstrip() + f" | {flyer_link} |"
            new_lines.append(line)
            continue

        # End of table
        if in_table and not stripped.startswith("|"):
            in_table = False

        new_lines.append(line)

    OVERVIEW_FILE.write_text("\n".join(new_lines), encoding="utf-8")
    print("  Added Flyer column to 50-state-overview.md table")
    return True


def main():
    print("Step 1: Appending flyer sections to state guide pages...")
    n = append_flyer_sections()
    print(f"  → {n} state guides updated\n")

    print("Step 2: Adding Flyer column to state-guides/index.md...")
    add_flyer_column_to_index()
    print()

    print("Step 3: Adding Flyer column to 50-state-overview.md...")
    add_flyer_column_to_overview()
    print()

    print("Done.")


if __name__ == "__main__":
    main()

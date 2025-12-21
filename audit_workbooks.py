#!/usr/bin/env python3
"""
PFL Workbook Data Audit
Scan all Student Activity Packet HTML files for local/state data requirements
"""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

# Paths
CONTENT_BASE = Path("/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/content-complete/English")
SLIDE_DIR = Path("slide-content")

# Localization triggers
STATE_VARIABLES = [
    "{{STATE", "{{LOCAL", "{{CITY", "{{REGION"
]

KEY_PHRASES = [
    "in your state",
    "research local",
    "current minimum wage",
    "average rent",
    "median rent",
    "tuition cost",
    "auto insurance",
    "property tax",
    "vehicle registration",
    "state tax",
    "local law",
    "in your area",
    "your community",
    "your city",
    "state requirement",
    "local college",
    "nearby university",
    "housing cost",
    "cost of living",
    "state minimum wage",
    "local housing",
    "your region"
]

def find_workbook_files():
    """Find all Student Activity Packet HTML files."""
    pattern = "L-*/assets/L-*_Student_Activity_Packet.html"
    files = list(CONTENT_BASE.glob(pattern))
    return sorted(files, key=lambda x: int(re.search(r'L-(\d+)', x.name).group(1)))

def extract_chapter_info(filepath):
    """Extract chapter number and title from workbook file."""
    filename = filepath.name
    match = re.search(r'L-(\d+)', filename)
    if not match:
        return None, None

    chapter_num = match.group(1)

    # Try to get title from parent directory name
    parent_name = filepath.parent.parent.name
    # Remove "L-XX-" prefix to get title
    title_match = re.search(r'L-\d+-(.*)', parent_name)
    if title_match:
        title = title_match.group(1).replace('-', ' ').title()
    else:
        title = "Unknown"

    return chapter_num, title

def scan_workbook(filepath):
    """Scan workbook for localization triggers."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return []

    soup = BeautifulSoup(content, 'html.parser')
    text_content = soup.get_text().lower()

    findings = []

    # Check for explicit state variables
    for var in STATE_VARIABLES:
        if var in content:  # Case-sensitive check for variables
            findings.append(f"Uses {var} variable")

    # Check for key phrases
    for phrase in KEY_PHRASES:
        if phrase.lower() in text_content:
            # Get context snippet
            pattern = re.compile(r'.{0,50}' + re.escape(phrase) + r'.{0,50}', re.IGNORECASE)
            match = pattern.search(text_content)
            if match:
                findings.append(f'"{phrase}"')

    # Remove duplicates while preserving order
    seen = set()
    unique_findings = []
    for item in findings:
        if item not in seen:
            seen.add(item)
            unique_findings.append(item)

    return unique_findings

def check_slide_deck_status(chapter_num):
    """Check if slide deck has state variables enabled."""
    json_path = SLIDE_DIR / f"L-{chapter_num}.json"

    if not json_path.exists():
        return "No slide deck", []

    try:
        with open(json_path, 'r', encoding='utf-8', errors='surrogatepass') as f:
            data = json.load(f)

        metadata = data.get('metadata', {})
        has_vars = metadata.get('hasStateVariables', False)
        state_vars = metadata.get('stateVariablesUsed', [])

        if has_vars and state_vars:
            return f"✅ Has {len(state_vars)} vars", state_vars
        elif has_vars:
            return "⚠️ Enabled, no vars", []
        else:
            return "❌ Not enabled", []
    except Exception as e:
        return f"Error: {e}", []

def generate_report(workbook_data):
    """Generate markdown report."""

    report = []
    report.append("# PFL Workbook Data Audit Report\n")
    report.append(f"**Generated:** {Path.cwd().name}\n")
    report.append(f"**Total Workbooks Scanned:** {len(workbook_data)}\n")
    report.append("\n---\n")

    # Main table
    report.append("## Workbook Local Data Requirements\n")
    report.append("| Chapter | Title | Data Points Detected | Slide Deck Status |")
    report.append("|---------|-------|---------------------|-------------------|")

    workbooks_with_data = []

    for entry in workbook_data:
        chapter = entry['chapter']
        title = entry['title']
        findings = entry['findings']
        status = entry['slide_status']
        state_vars = entry['state_vars']

        if findings:
            # Truncate findings for table
            findings_str = "; ".join(findings[:3])
            if len(findings) > 3:
                findings_str += f" (+{len(findings)-3} more)"

            report.append(f"| L-{chapter} | {title} | {findings_str} | {status} |")

            workbooks_with_data.append(entry)

    report.append("\n---\n")

    # Summary statistics
    report.append("## Summary Statistics\n")
    total_scanned = len(workbook_data)
    total_with_local_data = len(workbooks_with_data)

    # Count slide decks with state vars
    slides_with_vars = sum(1 for e in workbook_data if e['slide_status'].startswith("✅"))

    report.append(f"- **Total Workbooks Scanned:** {total_scanned}")
    report.append(f"- **Workbooks Requiring Local Data:** {total_with_local_data}")
    report.append(f"- **Slide Decks with State Variables:** {slides_with_vars}")
    report.append(f"- **Gap (Workbook needs data, Slide doesn't have it):** {total_with_local_data - slides_with_vars}\n")

    # Top 5 Opportunities
    report.append("\n---\n")
    report.append("## Top 5 Opportunities for Alignment\n")
    report.append("*Workbooks that request local data but slide decks don't provide it yet*\n")

    opportunities = [
        e for e in workbooks_with_data
        if not e['slide_status'].startswith("✅")
    ]

    # Sort by number of findings (most data points first)
    opportunities.sort(key=lambda x: len(x['findings']), reverse=True)

    for i, entry in enumerate(opportunities[:5], 1):
        chapter = entry['chapter']
        title = entry['title']
        findings = entry['findings']
        status = entry['slide_status']

        report.append(f"\n### {i}. L-{chapter}: {title}")
        report.append(f"**Slide Deck Status:** {status}")
        report.append(f"**Local Data Points Requested ({len(findings)}):**")
        for finding in findings:
            report.append(f"  - {finding}")

    # Detailed breakdown
    report.append("\n\n---\n")
    report.append("## Detailed Breakdown by Chapter\n")

    for entry in workbooks_with_data:
        chapter = entry['chapter']
        title = entry['title']
        findings = entry['findings']
        status = entry['slide_status']
        state_vars = entry['state_vars']

        report.append(f"\n### L-{chapter}: {title}")
        report.append(f"**Slide Deck Status:** {status}")
        if state_vars:
            report.append(f"**Current Slide Variables:** {', '.join(state_vars)}")
        report.append(f"**Workbook Local Data Points ({len(findings)}):**")
        for finding in findings:
            report.append(f"  - {finding}")

    return "\n".join(report)

def main():
    print("=" * 70)
    print("PFL WORKBOOK DATA AUDIT")
    print("=" * 70)
    print("\nScanning Student Activity Packet files...\n")

    workbook_files = find_workbook_files()
    print(f"Found {len(workbook_files)} workbook files\n")

    workbook_data = []

    for filepath in workbook_files:
        chapter_num, title = extract_chapter_info(filepath)
        if not chapter_num:
            continue

        print(f"Scanning L-{chapter_num}: {title}...")

        findings = scan_workbook(filepath)
        slide_status, state_vars = check_slide_deck_status(chapter_num)

        workbook_data.append({
            'chapter': chapter_num,
            'title': title,
            'findings': findings,
            'slide_status': slide_status,
            'state_vars': state_vars
        })

        if findings:
            print(f"  ✓ Found {len(findings)} local data point(s)")

    print("\n" + "=" * 70)
    print("Generating report...\n")

    report = generate_report(workbook_data)

    # Write report
    output_path = Path("WORKBOOK_DATA_AUDIT.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Report generated: {output_path}")
    print(f"   Total workbooks scanned: {len(workbook_data)}")
    print(f"   Workbooks with local data: {sum(1 for e in workbook_data if e['findings'])}")
    print("=" * 70)

if __name__ == "__main__":
    main()

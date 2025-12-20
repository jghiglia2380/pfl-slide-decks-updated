#!/usr/bin/env python3
"""
Enrich slide JSON files (L-59 through L-69) with content from teacher guides.
"""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Base paths
SLIDE_DIR = Path("slide-content")
TEACHER_GUIDE_BASE = Path("/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/content-complete/English")

# Chapters to process
CHAPTERS = ["L-59", "L-61", "L-62", "L-63", "L-64", "L-65", "L-66", "L-67", "L-68", "L-69"]

def find_teacher_guide(chapter):
    """Find the teacher guide HTML file for a given chapter."""
    pattern = f"{chapter}-*"
    matches = list(TEACHER_GUIDE_BASE.glob(pattern))
    if matches:
        guide_path = matches[0] / "assets" / f"{chapter}_Teacher_Guide.html"
        if guide_path.exists():
            return guide_path
    return None

def extract_challenge_discussion(html_content):
    """Extract THE CHALLENGE discussion prompts from teacher guide."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find THE CHALLENGE section
    challenge_title = soup.find('div', class_='flow-title', string='THE CHALLENGE')
    if not challenge_title:
        return None

    # Get the parent flow-content
    flow_content = challenge_title.find_parent('div', class_='flow-content')
    if not flow_content:
        return None

    # Extract bullet points
    bullets = flow_content.find('ul')
    if not bullets:
        return None

    items = []
    for li in bullets.find_all('li'):
        text = li.get_text().strip()
        items.append(text)

    # Format as HTML
    formatted = "<strong>Discussion Prompts:</strong><br>"
    formatted += "<br>".join([f"• {item}" for item in items])

    return formatted

def extract_misconceptions(html_content):
    """Extract Common Misconceptions table from teacher guide."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find misconception table
    table = soup.find('table', class_='misconception-table')
    if not table:
        return None

    rows = []
    for tr in table.find_all('tr')[1:]:  # Skip header row
        cells = tr.find_all('td')
        if len(cells) == 2:
            misconception = cells[0].get_text().strip()
            clarification = cells[1].get_text().strip()
            rows.append((misconception, clarification))

    # Format as HTML table
    formatted = "<strong>Common Misconceptions:</strong><br>"
    formatted += "<table style='width:100%; border-collapse: collapse; margin-top: 8px;'>"
    formatted += "<tr><th style='background: #fee2e2; color: #991b1b; padding: 6px; border: 1px solid #fca5a5; text-align: left;'>Misconception</th>"
    formatted += "<th style='background: #dcfce7; color: #166534; padding: 6px; border: 1px solid #86efac; text-align: left;'>Clarification</th></tr>"

    for misconception, clarification in rows:
        formatted += f"<tr><td style='padding: 6px; border: 1px solid #e2e8f0;'>{misconception}</td>"
        formatted += f"<td style='padding: 6px; border: 1px solid #e2e8f0;'>{clarification}</td></tr>"

    formatted += "</table>"

    return formatted

def extract_answer_key(html_content):
    """Extract Check Your Understanding answer key from teacher guide."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find Check Your Understanding section
    answer_title = soup.find('div', class_='answer-title', string='Check Your Understanding')
    if not answer_title:
        return None

    # Get the parent answer-block
    answer_block = answer_title.find_parent('div', class_='answer-block')
    if not answer_block:
        return None

    # Extract answer items
    answer_items = answer_block.find_all('div', class_='answer-item')

    answers = []
    for item in answer_items:
        html = str(item)
        # Extract question number and answer
        match = re.search(r'<strong>(\d+\.)</strong>\s*(.*?)</div>', html, re.DOTALL)
        if match:
            q_num = match.group(1)
            answer = match.group(2).strip()
            answers.append((q_num, answer))

    # Format as HTML
    formatted = "<strong>Assessment Answer Key (Check Your Understanding):</strong><br><br>"
    for q_num, answer in answers:
        formatted += f"<strong>Q{q_num}</strong> <em>Answer:</em> {answer}<br><br>"

    return formatted.rstrip("<br>")

def enrich_chapter(chapter):
    """Enrich a single chapter's JSON file."""
    print(f"\nProcessing {chapter}...")

    # Load JSON
    json_path = SLIDE_DIR / f"{chapter}.json"
    if not json_path.exists():
        print(f"  ❌ JSON file not found: {json_path}")
        return False

    with open(json_path, 'r', encoding='utf-8', errors='surrogatepass') as f:
        data = json.load(f)

    # Find teacher guide
    guide_path = find_teacher_guide(chapter)
    if not guide_path:
        print(f"  ❌ Teacher guide not found for {chapter}")
        return False

    print(f"  ✓ Found teacher guide: {guide_path.name}")

    # Read teacher guide
    with open(guide_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract content
    discussion = extract_challenge_discussion(html_content)
    misconceptions = extract_misconceptions(html_content)
    answer_key = extract_answer_key(html_content)

    # Update slides
    modified = False

    for slide in data['slides']:
        slide_num = slide.get('number')

        # Slide 2: Add discussion notes (only if not already present)
        if slide_num == 2 and discussion and 'notes' not in slide:
            slide['notes'] = discussion
            print(f"  ✓ Added discussion prompts to slide 2")
            modified = True

        # Slide 11: Add misconceptions (only if not already present)
        if slide_num == 11 and misconceptions and 'notes' not in slide:
            slide['notes'] = misconceptions
            print(f"  ✓ Added misconceptions to slide 11")
            modified = True

        # Slide 17: Add answer key (only if not already present)
        if slide_num == 17 and answer_key and 'notes' not in slide:
            slide['notes'] = answer_key
            print(f"  ✓ Added answer key to slide 17")
            modified = True

    # Save JSON if modified
    if modified:
        # Read original file to preserve formatting and encoding
        with open(json_path, 'r', encoding='utf-8', errors='surrogatepass') as f:
            original_content = f.read()

        # Write JSON with surrogatepass to handle emoji characters
        with open(json_path, 'w', encoding='utf-8', errors='surrogatepass') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  ✅ Saved changes to {chapter}.json")
        return True
    else:
        print(f"  ⚠️  No changes needed for {chapter}")
        return False

def main():
    print("=" * 60)
    print("Slide Enrichment - Batch 5 (L-59 through L-69)")
    print("=" * 60)

    success_count = 0

    for chapter in CHAPTERS:
        if enrich_chapter(chapter):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"✅ Successfully enriched {success_count}/{len(CHAPTERS)} chapters")
    print("=" * 60)

if __name__ == "__main__":
    main()

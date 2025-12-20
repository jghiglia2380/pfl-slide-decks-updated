#!/usr/bin/env python3
"""
Enrich slide deck JSON files with content from teacher guide HTML files.
Updates slides 2, 11, and 17 with speaker notes.
"""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_story_and_question(html_content):
    """Extract the story summary and framing question from THE CHALLENGE section."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find THE CHALLENGE section in lesson flow
    flow_items = soup.find_all('div', class_='flow-item')
    challenge_prompts = []

    for item in flow_items:
        title = item.find('div', class_='flow-title')
        if title and 'CHALLENGE' in title.text:
            # Extract discussion prompts from the list
            ul = item.find('ul')
            if ul:
                for li in ul.find_all('li'):
                    text = li.get_text(strip=True)
                    challenge_prompts.append(text)

    return challenge_prompts

def extract_common_misconceptions(html_content):
    """Extract common misconceptions table."""
    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table', class_='misconception-table')
    if not table:
        return []

    misconceptions = []
    rows = table.find_all('tr')[1:]  # Skip header row

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            misconception = cells[0].get_text(strip=True)
            clarification = cells[1].get_text(strip=True)
            misconceptions.append(f'• "{misconception}" → {clarification}')

    return misconceptions

def extract_assessment_answers(html_content):
    """Extract assessment answer key from Check Your Understanding section."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find Check Your Understanding answer block
    answer_blocks = soup.find_all('div', class_='answer-block')

    for block in answer_blocks:
        title = block.find('div', class_='answer-title')
        if title and 'Check Your Understanding' in title.text:
            answers = []
            answer_items = block.find_all('div', class_='answer-item')

            for i, item in enumerate(answer_items, 1):
                text = item.get_text(strip=True)
                # Remove the question number if it's at the start
                text = re.sub(r'^\d+\.\s*', f'{i}. ', text)
                answers.append(text)

            return answers

    return []

def create_speaker_notes_challenge(prompts):
    """Create speaker notes for slide 2 from challenge prompts."""
    if not prompts:
        return ""

    # Format the prompts into a coherent speaker note
    notes_parts = []

    for prompt in prompts:
        if 'read' in prompt.lower() or 'scenario' in prompt.lower():
            notes_parts.insert(0, prompt)  # Put reading instruction first
        else:
            notes_parts.append(prompt)

    return ' '.join(notes_parts)

def create_speaker_notes_misconceptions(misconceptions):
    """Create speaker notes for slide 11 from misconceptions."""
    if not misconceptions:
        return ""

    return "COMMON MISCONCEPTIONS:\n" + '\n'.join(misconceptions)

def create_speaker_notes_assessment(answers):
    """Create speaker notes for slide 17 from assessment answers."""
    if not answers:
        return ""

    return "ASSESSMENT ANSWER KEY:\n" + '\n'.join(answers)

def extract_story_from_slide(slide_content):
    """Extract a 2-sentence summary from existing slide 2 question."""
    question = slide_content.get('question', '')

    # Remove HTML tags for analysis
    clean_text = re.sub(r'<[^>]+>', ' ', question)

    # Split by <br><br> or double line breaks
    parts = re.split(r'<br\s*/?>\s*<br\s*/?>', question)

    if len(parts) >= 2:
        # First part is usually the story
        story_part = parts[0]

        # Split into sentences
        sentences = re.split(r'[.!?]+\s+', re.sub(r'<[^>]+>', ' ', story_part))
        sentences = [s.strip() for s in sentences if s.strip()]

        # Take first 2 sentences and reconstruct
        if len(sentences) >= 2:
            summary = sentences[0] + '. ' + sentences[1] + '.'
        elif len(sentences) == 1:
            summary = sentences[0] + '.'
        else:
            summary = story_part

        # Find the framing question (usually in <strong> or ends with ?)
        question_match = re.search(r'<strong>([^<]+\?)</strong>', question)
        if question_match:
            framing_q = question_match.group(1)
        else:
            # Try to find question in last part
            if parts[-1].strip().endswith('?'):
                framing_q = re.sub(r'<[^>]+>', '', parts[-1]).strip()
            else:
                framing_q = "What should be done in this situation?"

        return f"{summary}<br><br><strong>{framing_q}</strong>"

    return question  # Return original if parsing fails

def update_slide_json(json_path, teacher_guide_path):
    """Update a single slide JSON file with content from teacher guide."""

    print(f"Processing {json_path.name}...")

    # Read teacher guide HTML
    with open(teacher_guide_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract content
    challenge_prompts = extract_story_and_question(html_content)
    misconceptions = extract_common_misconceptions(html_content)
    assessment_answers = extract_assessment_answers(html_content)

    # Read JSON - handle emojis properly
    with open(json_path, 'r', encoding='utf-8', errors='surrogatepass') as f:
        content = f.read()
        data = json.loads(content)

    # Update slides
    for slide in data['slides']:
        if slide['number'] == 2:
            # Update question with summary
            if 'content' in slide and 'question' in slide['content']:
                slide['content']['question'] = extract_story_from_slide(slide['content'])

            # Add speaker notes
            if challenge_prompts:
                slide['speakerNotes'] = create_speaker_notes_challenge(challenge_prompts)

        elif slide['number'] == 11:
            # Add misconceptions to speaker notes
            if misconceptions:
                slide['speakerNotes'] = create_speaker_notes_misconceptions(misconceptions)

        elif slide['number'] == 17:
            # Add assessment answer key
            if assessment_answers:
                slide['speakerNotes'] = create_speaker_notes_assessment(assessment_answers)

    # Write updated JSON - handle emoji/surrogate pairs
    json_str = json.dumps(data, indent=2, ensure_ascii=False)

    with open(json_path, 'w', encoding='utf-8', errors='surrogatepass') as f:
        f.write(json_str)

    print(f"  ✓ Updated slide 2 (challenge)")
    print(f"  ✓ Updated slide 11 (misconceptions: {len(misconceptions)} items)")
    print(f"  ✓ Updated slide 17 (assessment: {len(assessment_answers)} questions)")

def main():
    """Process Batch 4B: L-51 through L-56."""

    base_path = Path("/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy")
    slide_dir = base_path / "slide-deck-templates" / "slide-content"
    content_dir = base_path / "content-complete" / "English"

    # Process Batch 4B chapters: 51-56 (L-50.json doesn't exist)
    batch_4b_chapters = [51, 52, 53, 54, 55, 56]
    for chapter_num in batch_4b_chapters:
        chapter_id = f"L-{chapter_num}"

        # Find JSON file
        json_file = slide_dir / f"{chapter_id}.json"
        if not json_file.exists():
            print(f"⚠ Skipping {chapter_id}: JSON not found")
            continue

        # Find teacher guide HTML
        teacher_guide_pattern = list(content_dir.glob(f"{chapter_id}-*/assets/{chapter_id}_Teacher_Guide.html"))

        if not teacher_guide_pattern:
            print(f"⚠ Skipping {chapter_id}: Teacher guide not found")
            continue

        teacher_guide = teacher_guide_pattern[0]

        # Update the JSON file
        try:
            update_slide_json(json_file, teacher_guide)
            print(f"✅ {chapter_id} complete\n")
        except Exception as e:
            print(f"❌ Error processing {chapter_id}: {e}\n")

if __name__ == "__main__":
    main()

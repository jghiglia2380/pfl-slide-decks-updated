#!/usr/bin/env python3
import json
import os
import glob
from bs4 import BeautifulSoup

def find_teacher_guide(chapter_num):
    """Find the teacher guide HTML file for a given chapter number"""
    base_path = "/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/content-complete/English"
    pattern = f"{base_path}/L-{chapter_num}-*/assets/L-{chapter_num}_Teacher_Guide.html"
    files = glob.glob(pattern)
    return files[0] if files else None

def extract_discussion_prompts(soup):
    """Extract discussion prompts from Lesson Flow"""
    discussion_text = "DISCUSSION PROMPTS:\n"
    flow_items = soup.find_all('div', class_='flow-item')
    for item in flow_items:
        flow_title = item.find('div', class_='flow-title')
        if flow_title and 'CHALLENGE' in flow_title.get_text().upper():
            flow_content = item.find('div', class_='flow-content')
            if flow_content:
                time_elem = item.find('div', class_='flow-time')
                time = time_elem.get_text().strip() if time_elem else ''
                title = flow_title.get_text().strip()
                discussion_text += f"{title} ({time}):\n"
                ul = flow_content.find('ul')
                if ul:
                    for li in ul.find_all('li'):
                        discussion_text += f"• {li.get_text().strip()}\n"
    return discussion_text

def extract_misconceptions(soup):
    """Extract common misconceptions table"""
    misconceptions_text = "COMMON MISCONCEPTIONS:\n\n"
    table = soup.find('table', class_='misconception-table')
    if table:
        rows = table.find_all('tr')[1:]  # Skip header row
        for idx, row in enumerate(rows, 1):
            cells = row.find_all('td')
            if len(cells) == 2:
                misconception = cells[0].get_text().strip()
                clarification = cells[1].get_text().strip()
                misconceptions_text += f"{idx}. {misconception}\n   → {clarification}\n\n"
    return misconceptions_text

def extract_answer_key(soup):
    """Extract assessment answer key"""
    answer_key_text = "ANSWER KEY:\n\n"

    # Find the "Check Your Understanding" section in the answer key
    answer_blocks = soup.find_all('div', class_='answer-block')
    for block in answer_blocks:
        title_elem = block.find('div', class_='answer-title')
        if title_elem and 'Check Your Understanding' in title_elem.get_text():
            answer_items = block.find_all('div', class_='answer-item')
            for item in answer_items:
                answer_key_text += f"{item.get_text().strip()}\n\n"

    return answer_key_text

def get_json_path(chapter_num):
    """Get the correct JSON file path, handling special cases like L-60-UPDATED"""
    if chapter_num == 60:
        return 'slide-content/L-60-UPDATED.json'
    else:
        return f'slide-content/L-{chapter_num}.json'

def update_chapter(chapter_num):
    """Update a single chapter's JSON file"""
    print(f"\nProcessing L-{chapter_num}...")

    # Find teacher guide
    guide_path = find_teacher_guide(chapter_num)
    if not guide_path:
        print(f"  ⚠️  Teacher guide not found for L-{chapter_num}")
        return False

    print(f"  ✓ Found teacher guide: {os.path.basename(os.path.dirname(guide_path))}")

    # Read and parse HTML
    with open(guide_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Extract content
    discussion_prompts = extract_discussion_prompts(soup)
    misconceptions = extract_misconceptions(soup)
    answer_key = extract_answer_key(soup)

    # Read JSON file - handle surrogates
    json_path = get_json_path(chapter_num)
    if not os.path.exists(json_path):
        print(f"  ⚠️  JSON file not found: {json_path}")
        return False

    with open(json_path, 'r', encoding='utf-8', errors='surrogatepass') as f:
        data = json.load(f)

    # Get the story from slide 2 to create summary
    slide_2 = next((s for s in data['slides'] if s['number'] == 2), None)
    if slide_2 and 'content' in slide_2 and 'question' in slide_2['content']:
        original_question = slide_2['content']['question']
        # Create a summarized version (first 2 sentences + framing question)
        parts = original_question.split('<br><br>')
        if len(parts) >= 2:
            # Take first 2 narrative parts and last framing question
            story_summary = ' '.join(parts[:2])
            framing_question = parts[-1] if '?' in parts[-1] else parts[-2] if len(parts) > 2 else parts[-1]
            new_question = f"{story_summary} <br><br> {framing_question}"
            slide_2['content']['question'] = new_question

    # Update slides with notes
    for slide in data['slides']:
        if slide['number'] == 2:
            slide['notes'] = discussion_prompts
        elif slide['number'] == 11:
            slide['notes'] = misconceptions
        elif slide['number'] == 17:
            slide['notes'] = answer_key

    # Write back to JSON with proper emoji handling
    with open(json_path, 'w', encoding='utf-8', errors='surrogatepass') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  ✓ Updated {os.path.basename(json_path)}")
    return True

def main():
    """Process all chapters from L-60 to L-69"""
    print("=" * 60)
    print("BATCH 5B SLIDE ENRICHMENT: L-60 through L-69")
    print("=" * 60)

    success_count = 0
    fail_count = 0

    for chapter_num in range(60, 70):  # 60 through 69
        try:
            if update_chapter(chapter_num):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"  ✗ Error processing L-{chapter_num}: {str(e)}")
            fail_count += 1

    print("\n" + "=" * 60)
    print(f"COMPLETE: {success_count} chapters updated, {fail_count} failed")
    print("=" * 60)

if __name__ == '__main__':
    main()

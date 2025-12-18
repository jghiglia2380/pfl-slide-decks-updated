# JSON File Fix Instructions for Claude Code

## Overview
The HTML-to-JSON converter failed to properly extract content from several slide deck HTML files. You need to manually read each HTML file and generate accurate, complete JSON files following the established schema.

## Reference Files

**Schema Example (use this as your template):**
```
/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-deck-templates/slide-content/L-01.json
```

**HTML Source Directory:**
```
/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/
```

**JSON Output Directory:**
```
/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-deck-templates/slide-content/
```

---

## PRIORITY 1: Completely Empty Files (No slides extracted)

These files have empty `slides: []` arrays. The HTML files use Reveal.js format which the converter couldn't parse.

| JSON File | HTML Source |
|-----------|-------------|
| L-51.json | L-51-market-structures-slides.html |
| L-52.json | L-52-government-economy-slides.html |
| L-53.json | L-53-fiscal-monetary-policy-slides.html |
| L-54.json | L-54-inflation-unemployment-slides.html |
| L-55.json | L-55-international-trade-slides.html |
| L-56.json | L-56-financial-record-keeping-slides.html |

**Task:** Read each HTML file, extract ALL content, and generate complete JSON files.

---

## PRIORITY 2: Empty layoutData (Structure exists but content missing)

These files have slide structures but `layoutData: {}` is empty or fields are blank.

| JSON File | HTML Source |
|-----------|-------------|
| L-57.json | L-57-loan-applications-and-creditworthiness-slides.html |
| L-61.json | L-61-contract-evaluation-and-consumer-protection-slides.html |
| L-62.json | L-62-investment-portfolio-strategies-slides.html |
| L-63.json | L-63-advanced-investment-concepts-slides.html |
| L-64.json | L-64-risk-and-return-in-investing-slides.html |
| L-69.json | L-69-alternative-investments-and-wealth-strategies-slides.html |

**Task:** Read the HTML, fill in all missing content in layoutData, objectives, terms, paragraphs, stats, questions, etc.

---

## PRIORITY 3: Partial Content / Incorrect Metadata

These files have some content but are incomplete or have errors like `"lChapter": "L-XX"`.

| JSON File | HTML Source | Known Issues |
|-----------|-------------|--------------|
| L-04.json | L-04-financial-goal-setting-slides.html | lChapter says "L-XX", many empty fields |
| L-06.json | L-06-understanding-federal-state-taxes-slides.html | Incomplete data, empty arrays |

**Task:** Fix metadata, fill in all missing content.

---

## JSON Schema Reference

Every JSON file must follow this structure:

```json
{
  "metadata": {
    "lChapter": "L-XX",           // Must match actual chapter number
    "title": "Chapter Title",
    "subtitle": "Chapter Subtitle",
    "totalSlides": 20,            // Actual count of slides
    "hasStateVariables": false,   // true if {{STATE_NAME}} etc. appear
    "stateVariablesUsed": []      // List any: ["STATE_NAME", "STATE_CODE", etc.]
  },
  "slides": [
    // Array of slide objects
  ]
}
```

## Slide Types

### 1. Title Slide (type: "title")
```json
{
  "number": 1,
  "type": "title",
  "content": {
    "title": "Main Title",
    "titleSize": "large",
    "subtitle": "Subtitle text"
  }
}
```

### 2. Hook Slide (type: "hook")
```json
{
  "number": 2,
  "type": "hook",
  "content": {
    "label": "Essential Question",
    "question": "The hook question with <em>emphasis</em> tags"
  }
}
```

### 3. Content Slide (type: "content")
```json
{
  "number": 3,
  "type": "content",
  "headerColor": "teal",  // Options: teal, purple, blue, rose, green
  "content": {
    "headerTitle": "Slide Title",
    "layout": "layout-name",
    "layoutData": {
      // Layout-specific data
    }
  }
}
```

### 4. Discussion Slide (type: "discussion")
```json
{
  "number": 15,
  "type": "discussion",
  "variant": "teal",  // or "purple"
  "content": {
    "badge": "Discussion",  // or "Personal Reflection"
    "question": "The discussion question text"
  }
}
```

### 5. Closing Slide (type: "closing")
```json
{
  "number": 20,
  "type": "closing",
  "content": {
    "tagline": "Tagline text",
    "website": "www.pflacademy.co",
    "copyright": "© 2025 PFL Academy. All rights reserved."
  }
}
```

## Common Layout Types

### objectives-expanded
```json
{
  "layout": "objectives-expanded",
  "layoutData": {
    "objectives": [
      {
        "number": 1,
        "verb": "Identify",
        "description": "Full description of the objective"
      }
    ]
  }
}
```

### vocab-container
```json
{
  "layout": "vocab-container",
  "layoutData": {
    "terms": [
      {
        "term": "Term Name",
        "definition": "Full definition",
        "example": "Example usage"
      }
    ]
  }
}
```

### balanced-layout
```json
{
  "layout": "balanced-layout",
  "layoutData": {
    "leftPanel": {
      "title": "Panel Title",
      "paragraphs": ["Paragraph 1", "Paragraph 2"],
      "highlightBox": {
        "icon": "💡",
        "text": "Highlight text"
      }
    },
    "rightPanel": {
      "stats": [
        {"value": "85%", "label": "Stat label", "color": "teal"}
      ],
      "infoCard": {
        "title": "Card Title",
        "color": "amber",
        "items": ["Item 1", "Item 2"]
      }
    }
  }
}
```

### comparison-grid
```json
{
  "layout": "comparison-grid",
  "layoutData": {
    "leftColumn": {
      "icon": "✓",
      "title": "Left Title",
      "items": ["Item 1", "Item 2"]
    },
    "rightColumn": {
      "icon": "⚠",
      "title": "Right Title", 
      "items": ["Item 1", "Item 2"]
    }
  }
}
```

### concept-full
```json
{
  "layout": "concept-full",
  "layoutData": {
    "title": "Concept Title",
    "paragraphs": ["Paragraph text"],
    "bulletPoints": ["Point 1", "Point 2"],
    "keyPoint": "Key point text"
  }
}
```

### scenario-layout
```json
{
  "layout": "scenario-layout",
  "layoutData": {
    "scenario": {
      "icon": "👤",
      "name": "Person Name: Description",
      "paragraphs": ["Scenario paragraph 1", "Scenario paragraph 2"]
    },
    "outcomes": [
      {"type": "before", "label": "Before", "value": "$500", "detail": "Detail text"},
      {"type": "after", "label": "After", "value": "$1,200", "detail": "Detail text"}
    ]
  }
}
```

### check-grid
```json
{
  "layout": "check-grid",
  "layoutData": {
    "questions": [
      {"number": 1, "question": "Question text"},
      {"number": 2, "question": "Question text"}
    ]
  }
}
```

### takeaway-grid
```json
{
  "layout": "takeaway-grid",
  "layoutData": {
    "takeaways": [
      {"number": 1, "title": "Takeaway Title", "description": "Description text"}
    ]
  }
}
```

### activity-layout
```json
{
  "layout": "activity-layout",
  "layoutData": {
    "main": {
      "icon": "📋",
      "title": "Activity Title",
      "description": "Activity description"
    },
    "steps": ["Step 1", "Step 2", "Step 3"]
  }
}
```

---

## State Variables

If the HTML contains any of these placeholders, set `hasStateVariables: true` and list them:

- `{{STATE_NAME}}` - Full state name
- `{{STATE_CODE}}` - Two-letter state code
- `{{STATE_INCOME_TAX_RATE}}` - Income tax rate
- `{{STATE_SALES_TAX_RATE}}` - Sales tax rate
- `{{STATE_MINIMUM_WAGE}}` - Minimum wage
- `{{STATE_CAPITAL_GAINS_TAX}}` - Capital gains tax
- And others as found in the HTML

---

## Execution Steps

For each file in Priority 1, 2, and 3:

1. **Read the HTML file** from the slide-decks directory
2. **Read L-01.json** as schema reference
3. **Parse all slide content** from the HTML:
   - Extract titles, subtitles, paragraphs
   - Extract all bullet points and list items
   - Extract statistics and numbers
   - Extract discussion questions
   - Extract key terms and definitions
   - Identify state variables
4. **Generate complete JSON** following the schema
5. **Save to slide-content directory** overwriting the incomplete file
6. **Verify** the JSON is valid and complete

---

## Quality Checklist

Before saving each JSON file, verify:

- [ ] `lChapter` matches the actual chapter number (e.g., "L-51")
- [ ] `title` and `subtitle` are populated
- [ ] `totalSlides` matches actual slide count
- [ ] `hasStateVariables` is correct
- [ ] `stateVariablesUsed` lists all variables found
- [ ] Every slide has a `number`, `type`, and `content`
- [ ] No empty strings in required fields
- [ ] No empty arrays where content should exist
- [ ] All `layoutData` objects have complete content
- [ ] Discussion questions are fully populated
- [ ] All vocabulary terms have definitions and examples

---

## Files to Process (Complete List)

### Priority 1 - Full Generation Needed:
1. L-51.json
2. L-52.json
3. L-53.json
4. L-54.json
5. L-55.json
6. L-56.json

### Priority 2 - Content Fill Needed:
7. L-57.json
8. L-61.json
9. L-62.json
10. L-63.json
11. L-64.json
12. L-69.json

### Priority 3 - Fixes Needed:
13. L-04.json
14. L-06.json

---

## After Completion

Once all 14 files are fixed:

1. Copy updated JSON files to the GitHub repo:
```bash
cp "/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-deck-templates/slide-content/"*.json ~/temp-slide-repo/slide-content/
```

2. Commit and push:
```bash
cd ~/temp-slide-repo
git add .
git commit -m "Fix incomplete JSON files - manual content extraction"
git push origin main
```

---

## Notes

- Preserve HTML formatting tags like `<strong>`, `<em>`, `<br>` in text content
- Some HTML files use Reveal.js format (L-51 through L-56) - parse the `<section>` tags
- Other HTML files use custom PFL format - parse the `.slide` divs
- When in doubt, extract MORE content rather than less
- Double-check numbers and statistics for accuracy

# STRICT JSON Fix Instructions - 7 Files

## CRITICAL: READ THIS FIRST

The previous attempt FAILED. You must follow these instructions EXACTLY.

### FAILURES TO AVOID:
1. ❌ L-61 was left completely empty - UNACCEPTABLE
2. ❌ Files had 15-18 slides instead of required 20
3. ❌ Custom layoutData structures were invented instead of following schema
4. ❌ Hook slides had extra fields not in schema

---

## FILES TO FIX (7 total)

| File | Current Issue |
|------|---------------|
| L-51.json | Only 15 slides, needs 20 |
| L-52.json | Only 17 slides, needs 20 |
| L-53.json | Only 18 slides, needs 20 |
| L-54.json | Only 16 slides, needs 20 |
| L-55.json | Only 15 slides, needs 20 |
| L-56.json | Only 16 slides, needs 20 |
| L-61.json | COMPLETELY EMPTY - 20 placeholder slides with no content |

---

## MANDATORY REQUIREMENTS

### 1. EXACTLY 20 SLIDES PER FILE

Every JSON file MUST have exactly 20 slides. Not 15, not 18, not 19. **EXACTLY 20.**

### 2. REQUIRED SLIDE STRUCTURE

Follow this exact sequence:

| Slide # | Type | Purpose |
|---------|------|---------|
| 1 | title | Chapter title and subtitle |
| 2 | hook | Essential question to engage students |
| 3 | content | Learning objectives (objectives-expanded layout) |
| 4 | content | Key vocabulary part 1 (vocab-container layout) |
| 5 | content | Key vocabulary part 2 (vocab-container layout) |
| 6-11 | content | Core instructional content (6 slides) |
| 12 | discussion | Class discussion question |
| 13-14 | content | Real-world examples/scenarios (2 slides) |
| 15 | discussion | Personal reflection |
| 16 | content | Additional content or common mistakes |
| 17 | content | Check for understanding (check-grid layout) |
| 18 | content | Key takeaways (takeaway-grid layout) |
| 19 | content | Skill builder activity preview (activity-layout) |
| 20 | closing | Tagline, website, copyright |

### 3. USE ONLY THESE LAYOUTS

DO NOT INVENT NEW LAYOUTS. Use ONLY these:

- `objectives-expanded`
- `vocab-container`
- `balanced-layout`
- `comparison-grid`
- `concept-full`
- `scenario-layout`
- `check-grid`
- `takeaway-grid`
- `activity-layout`

---

## EXACT SCHEMA FOR EACH SLIDE TYPE

### Slide 1: Title
```json
{
  "number": 1,
  "type": "title",
  "content": {
    "title": "Chapter Title Here",
    "titleSize": "large",
    "subtitle": "Subtitle text here"
  }
}
```

### Slide 2: Hook
```json
{
  "number": 2,
  "type": "hook",
  "content": {
    "label": "Essential Question",
    "question": "The hook question with <em>emphasis</em> if needed"
  }
}
```
**DO NOT ADD:** `context`, `keyQuestion`, `proArguments`, `conArguments`, `whatHappened`, `table`, or any other fields.

### Slide 3: Learning Objectives
```json
{
  "number": 3,
  "type": "content",
  "headerColor": "purple",
  "content": {
    "headerTitle": "Learning Objectives",
    "layout": "objectives-expanded",
    "layoutData": {
      "objectives": [
        {
          "number": 1,
          "verb": "Identify",
          "description": "Full description of the objective"
        },
        {
          "number": 2,
          "verb": "Explain",
          "description": "Full description of the objective"
        },
        {
          "number": 3,
          "verb": "Analyze",
          "description": "Full description of the objective"
        },
        {
          "number": 4,
          "verb": "Apply",
          "description": "Full description of the objective"
        }
      ]
    }
  }
}
```

### Slides 4-5: Vocabulary
```json
{
  "number": 4,
  "type": "content",
  "headerColor": "teal",
  "content": {
    "headerTitle": "Key Terms",
    "layout": "vocab-container",
    "layoutData": {
      "terms": [
        {
          "term": "Term Name",
          "definition": "Full definition of the term",
          "example": "Example of the term in use"
        },
        {
          "term": "Second Term",
          "definition": "Full definition",
          "example": "Example"
        }
      ]
    }
  }
}
```

### Content Slides: balanced-layout
```json
{
  "number": 6,
  "type": "content",
  "headerColor": "purple",
  "content": {
    "headerTitle": "Slide Title",
    "layout": "balanced-layout",
    "layoutData": {
      "leftPanel": {
        "title": "Left Panel Title",
        "paragraphs": [
          "First paragraph of content.",
          "Second paragraph of content."
        ],
        "highlightBox": {
          "icon": "💡",
          "text": "Key insight or tip"
        }
      },
      "rightPanel": {
        "stats": [
          {
            "value": "85%",
            "label": "Description of statistic",
            "color": "teal"
          },
          {
            "value": "$500",
            "label": "Another statistic",
            "color": "purple"
          }
        ],
        "infoCard": {
          "title": "Info Card Title",
          "color": "amber",
          "items": [
            "First item",
            "Second item"
          ]
        }
      }
    }
  }
}
```

**IMPORTANT:** `rightPanel` can have EITHER `stats` OR `infoCard`, not custom fields.

### Content Slides: comparison-grid
```json
{
  "number": 7,
  "type": "content",
  "headerColor": "teal",
  "content": {
    "headerTitle": "Comparison Title",
    "layout": "comparison-grid",
    "layoutData": {
      "leftColumn": {
        "icon": "✓",
        "title": "Left Column Title",
        "items": [
          "First item",
          "Second item",
          "Third item"
        ]
      },
      "rightColumn": {
        "icon": "✗",
        "title": "Right Column Title",
        "items": [
          "First item",
          "Second item",
          "Third item"
        ]
      }
    }
  }
}
```

**DO NOT USE:** `centerColumn`, `table`, `causes`, `roles`, `impacts`, `strategies`, `structures`, or any other custom fields.

### Content Slides: concept-full
```json
{
  "number": 8,
  "type": "content",
  "headerColor": "blue",
  "content": {
    "headerTitle": "Concept Title",
    "layout": "concept-full",
    "layoutData": {
      "title": "Main concept title or statement",
      "paragraphs": [
        "First paragraph explaining the concept.",
        "Second paragraph with more details."
      ],
      "bulletPoints": [
        "Key point one",
        "Key point two",
        "Key point three"
      ],
      "keyPoint": "The most important takeaway from this slide"
    }
  }
}
```

### Content Slides: scenario-layout
```json
{
  "number": 13,
  "type": "content",
  "headerColor": "teal",
  "content": {
    "headerTitle": "Real-World Example",
    "layout": "scenario-layout",
    "layoutData": {
      "scenario": {
        "icon": "👤",
        "name": "Person Name: Brief Description",
        "paragraphs": [
          "First paragraph describing the scenario.",
          "Second paragraph with more context."
        ]
      },
      "outcomes": [
        {
          "type": "before",
          "label": "Before",
          "value": "$500",
          "detail": "Description of before state"
        },
        {
          "type": "after",
          "label": "After",
          "value": "$1,200",
          "detail": "Description of after state"
        }
      ]
    }
  }
}
```

### Discussion Slides
```json
{
  "number": 12,
  "type": "discussion",
  "variant": "teal",
  "content": {
    "badge": "Discussion",
    "question": "The discussion question goes here. Can include <br> for line breaks."
  }
}
```

For reflection slides, use `"badge": "Personal Reflection"` and `"variant": "purple"`.

### Slide 17: Check for Understanding
```json
{
  "number": 17,
  "type": "content",
  "headerColor": "purple",
  "content": {
    "headerTitle": "Check for Understanding",
    "layout": "check-grid",
    "layoutData": {
      "questions": [
        {
          "number": 1,
          "question": "First comprehension question?"
        },
        {
          "number": 2,
          "question": "Second comprehension question?"
        },
        {
          "number": 3,
          "question": "Third comprehension question?"
        },
        {
          "number": 4,
          "question": "Fourth comprehension question?"
        }
      ]
    }
  }
}
```

### Slide 18: Key Takeaways
```json
{
  "number": 18,
  "type": "content",
  "headerColor": "teal",
  "content": {
    "headerTitle": "Key Takeaways",
    "layout": "takeaway-grid",
    "layoutData": {
      "takeaways": [
        {
          "number": 1,
          "title": "First Takeaway",
          "description": "Explanation of the first key point"
        },
        {
          "number": 2,
          "title": "Second Takeaway",
          "description": "Explanation of the second key point"
        },
        {
          "number": 3,
          "title": "Third Takeaway",
          "description": "Explanation of the third key point"
        },
        {
          "number": 4,
          "title": "Fourth Takeaway",
          "description": "Explanation of the fourth key point"
        }
      ]
    }
  }
}
```

### Slide 19: Activity Preview
```json
{
  "number": 19,
  "type": "content",
  "headerColor": "blue",
  "content": {
    "headerTitle": "Skill Builder: Activity Name",
    "layout": "activity-layout",
    "layoutData": {
      "main": {
        "icon": "📋",
        "title": "Activity Title",
        "description": "Brief description of what students will do"
      },
      "steps": [
        "Step 1 instruction",
        "Step 2 instruction",
        "Step 3 instruction",
        "Step 4 instruction",
        "Step 5 instruction"
      ]
    }
  }
}
```

### Slide 20: Closing
```json
{
  "number": 20,
  "type": "closing",
  "content": {
    "tagline": "\"Memorable tagline related to chapter topic\"",
    "website": "www.pflacademy.co",
    "copyright": "© 2025 PFL Academy. All rights reserved."
  }
}
```

---

## HTML SOURCE FILES

Read content from these HTML files:

| JSON to Create | HTML Source |
|----------------|-------------|
| L-51.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-51-market-structures-slides.html |
| L-52.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-52-government-economy-slides.html |
| L-53.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-53-fiscal-monetary-policy-slides.html |
| L-54.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-54-inflation-unemployment-slides.html |
| L-55.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-55-international-trade-slides.html |
| L-56.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-56-financial-record-keeping-slides.html |
| L-61.json | /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-decks/L-61-contract-evaluation-and-consumer-protection-slides.html |

---

## OUTPUT LOCATION

Save completed JSON files to:
```
/Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/slide-deck-templates/slide-content/
```

---

## VALIDATION CHECKLIST

Before saving each file, verify:

- [ ] File has EXACTLY 20 slides
- [ ] Slide 1 is type "title"
- [ ] Slide 2 is type "hook" with ONLY `label` and `question` fields
- [ ] Slide 3 has layout "objectives-expanded" with 4 objectives
- [ ] Slides 4-5 have layout "vocab-container"
- [ ] Slide 12 is type "discussion"
- [ ] Slide 15 is type "discussion" with badge "Personal Reflection"
- [ ] Slide 17 has layout "check-grid" with 4 questions
- [ ] Slide 18 has layout "takeaway-grid" with 4+ takeaways
- [ ] Slide 19 has layout "activity-layout"
- [ ] Slide 20 is type "closing"
- [ ] NO custom layoutData fields invented
- [ ] All layoutData follows exact schema above
- [ ] `lChapter` in metadata matches file name (e.g., "L-51")
- [ ] `totalSlides` in metadata equals 20

---

## EXECUTION ORDER

1. Read L-51 HTML → Generate L-51.json → Verify 20 slides → Save
2. Read L-52 HTML → Generate L-52.json → Verify 20 slides → Save
3. Read L-53 HTML → Generate L-53.json → Verify 20 slides → Save
4. Read L-54 HTML → Generate L-54.json → Verify 20 slides → Save
5. Read L-55 HTML → Generate L-55.json → Verify 20 slides → Save
6. Read L-56 HTML → Generate L-56.json → Verify 20 slides → Save
7. Read L-61 HTML → Generate L-61.json → Verify 20 slides → Save

---

## FINAL REMINDER

**DO NOT:**
- Leave any file empty
- Create fewer than 20 slides
- Invent custom layoutData structures
- Add extra fields to hook slides
- Use layouts not listed in this document
- Skip the validation checklist

**DO:**
- Follow the exact schema provided
- Extract ALL content from HTML source
- Create exactly 20 well-structured slides
- Use only the approved layouts
- Verify each file before saving

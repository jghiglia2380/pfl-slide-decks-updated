# PFL Academy Slide Deck Golden Template Specification

**Version:** 2.0  
**Last Updated:** December 18, 2025  
**Reference Files:** L-60.json (structure), L-50.json (state variable integration)

---

## Design Philosophy

The slide deck is **Day 1's instructional spine** - not a standalone artifact. It must:

1. **Mirror the Student Activity Packet** in terminology and visual signaling
2. **Complement the Teacher Guide** without duplicating its facilitation depth
3. **Create narrative tension** that makes Day 2's Learning Lab feel essential
4. **Remain structurally disciplined** - 20 slides, fixed sections, flexible content

### Artifact Role Contract

| Artifact | Primary Function | Must NOT Do |
|----------|------------------|-------------|
| **Slide Deck** | Pace instruction, anchor discussion, signal transitions | Contain dense explanations or replace the Teacher Guide |
| **Student Activity Packet** | Capture thinking, apply concepts, provide evidence | Introduce concepts independently |
| **Teacher Guide** | Explain how/why to teach, provide differentiation | Be projected or student-facing |

---

## Color System (Aligned to Student Activity Packet)

The slide deck inherits the **semantic color system** from the Student Activity Packet. Colors signal cognitive modes, not decoration.

| Role | Hex Code | CSS Variable | Slide Usage |
|------|----------|--------------|-------------|
| **Instruction/Concepts** | #6366f1 | `--primary` (indigo) | Objectives, Core Concepts, Takeaways, most content |
| **Challenge/Scenarios** | #f59e0b | `--accent` (amber) | The Challenge, Scenarios, Discussion prompts |
| **Assessment/Synthesis** | #059669 | `--success` (emerald) | Check Your Understanding |
| **Text Primary** | #1e293b | `--text-dark` | Body text, titles |
| **Text Secondary** | #475569 | `--text-medium` | Descriptions, examples |

### headerColor Mapping

| Slide Type | headerColor Value |
|------------|-------------------|
| Learning Objectives | `"indigo"` |
| Core Concepts (Key Terms) | `"indigo"` |
| Core Content slides | `"indigo"` |
| Scenario slides | `"amber"` |
| Discussion slides | `"amber"` |
| Check Your Understanding | `"emerald"` |
| Key Takeaways | `"indigo"` |
| Activity Preview / Tomorrow's Challenge | `"amber"` |

---

## Terminology Alignment

Section headers must match the Student Activity Packet exactly.

| Slide Section | Correct Label | Incorrect Labels |
|---------------|---------------|------------------|
| Slide 2 (Hook) | **"The Challenge"** | "Essential Question", "Hook" |
| Slides 4-5 | **"Core Concepts"** | "Key Terms", "Vocabulary" |
| Slides 13-14 | **"Apply It"** (scenarios) | "Real-World Example" |
| Slide 17 | **"Check Your Understanding"** | "Check for Understanding" |
| Slide 19 | **"Tomorrow's Challenge"** | "Day 2 Preview", "Activity" |

---

## 20-Slide Structure

### Overview

```
SETUP (Slides 1-5)           → 7-10 minutes
├── Title, Challenge, Objectives, Core Concepts

CORE CONTENT (Slides 6-12)   → 15-20 minutes  
├── Concept explanation, examples, data

APPLICATION (Slides 13-16)   → 10-15 minutes
├── Scenarios, discussion, reflection

TRANSFER (Slides 17-20)      → 5-10 minutes
├── Assessment, takeaways, Day 2 bridge, closing
```

---

### Slide-by-Slide Specification

#### SLIDE 1: Title
```json
{
  "number": 1,
  "type": "title",
  "content": {
    "title": "[Chapter Title]",
    "titleSize": "large",
    "subtitle": "[Engaging subtitle that hints at relevance]"
  }
}
```

---

#### SLIDE 2: The Challenge
```json
{
  "number": 2,
  "type": "hook",
  "content": {
    "label": "The Challenge",
    "question": "[Narrative scenario OR striking statistic with <em> emphasis]<br><br>[Framing question that creates tension]"
  }
}
```

**Requirements:**
- Must mirror the Challenge box from the Student Activity Packet
- Use `<em>` for emphasis on key data points
- End with an open question that the lesson will resolve

---

#### SLIDE 3: Learning Objectives
```json
{
  "number": 3,
  "type": "content",
  "headerColor": "indigo",
  "content": {
    "headerTitle": "Learning Objectives",
    "layout": "objectives-expanded",
    "layoutData": {
      "objectives": [
        {
          "number": 1,
          "verb": "[Action verb]",
          "description": "[Observable, measurable outcome]"
        }
      ]
    }
  }
}
```

**Requirements:**
- Exactly 4 objectives
- Each begins with an action verb (Analyze, Evaluate, Compare, Apply, etc.)
- Objectives must align with Student Activity Packet learning objectives

---

#### SLIDES 4-5: Core Concepts
```json
{
  "number": 4,
  "type": "content",
  "headerColor": "indigo",
  "content": {
    "headerTitle": "Core Concepts",
    "layout": "vocab-container",
    "layoutData": {
      "terms": [
        {
          "term": "[Term]",
          "definition": "[Clear, concise definition]",
          "example": "[Concrete, relatable example]"
        },
        {
          "term": "[Term]",
          "definition": "[Clear, concise definition]",
          "example": "[Concrete, relatable example]"
        }
      ]
    }
  }
}
```

**Requirements:**
- 2 terms per slide (4 total across slides 4-5)
- Terms must match the Student Activity Packet terms table exactly
- Examples should be student-relatable

---

#### SLIDES 6-12: Core Content

Flexible layout selection based on content needs:

**Layout Options:**

| Layout | Use Case |
|--------|----------|
| `balanced-layout` | Two-panel content with stats, info cards |
| `concept-full` | Full-width explanation with bullet points |
| `comparison-grid` | Side-by-side comparison (Do/Don't, Before/After) |
| `scenario-layout` | Narrative scenario with outcomes |

**balanced-layout structure:**
```json
{
  "layout": "balanced-layout",
  "layoutData": {
    "leftPanel": {
      "title": "[Section title]",
      "paragraphs": ["[Content]"],
      "highlightBox": {
        "icon": "💡",
        "text": "[Key insight]"
      }
    },
    "rightPanel": {
      "stats": [
        {
          "value": "[Number or $amount]",
          "label": "[What it measures]",
          "color": "indigo|amber|emerald"
        }
      ],
      "infoCard": {
        "title": "[Card title]",
        "color": "indigo|amber|emerald",
        "items": ["[Bullet points]"]
      }
    }
  }
}
```

**concept-full structure:**
```json
{
  "layout": "concept-full",
  "layoutData": {
    "title": "[Main concept]",
    "paragraphs": ["[Introductory text]"],
    "bulletPoints": [
      "<strong>[Category]:</strong> [Explanation]"
    ],
    "keyPoint": {
      "text": "[Summary or key takeaway with emoji]"
    }
  }
}
```

---

#### SLIDES 13-14: Scenarios (Apply It)
```json
{
  "number": 13,
  "type": "content",
  "headerColor": "amber",
  "content": {
    "headerTitle": "Apply It",
    "layout": "scenario-layout",
    "layoutData": {
      "scenario": {
        "icon": "[Relevant emoji]",
        "name": "[Scenario title - person's name + situation]",
        "paragraphs": [
          "[Narrative setup]",
          "[Key decision point or tension]"
        ]
      },
      "outcomes": [
        {
          "type": "before|after|positive|negative",
          "label": "[Outcome label]",
          "value": "[Key metric]",
          "detail": "[Brief explanation]"
        }
      ]
    }
  }
}
```

**Requirements:**
- Scenarios should connect to or preview the Student Activity Packet scenarios
- Include concrete numbers/outcomes
- Create decision-making context

---

#### SLIDES 15-16: Discussion
```json
{
  "number": 15,
  "type": "discussion",
  "variant": "amber",
  "content": {
    "badge": "Discussion",
    "question": "[Open-ended question that requires application of concepts]"
  }
}
```

```json
{
  "number": 16,
  "type": "discussion",
  "variant": "indigo",
  "content": {
    "badge": "Reflection",
    "question": "[Personal application question]<br><br>[Follow-up that deepens thinking]"
  }
}
```

**Requirements:**
- Slide 15: Conceptual discussion (amber)
- Slide 16: Personal reflection (indigo)
- Questions should not have single "right" answers

---

#### SLIDE 17: Check Your Understanding
```json
{
  "number": 17,
  "type": "content",
  "headerColor": "emerald",
  "content": {
    "headerTitle": "Check Your Understanding",
    "layout": "check-grid",
    "layoutData": {
      "questions": [
        {
          "number": 1,
          "question": "[Recall or comprehension question]"
        },
        {
          "number": 2,
          "question": "[Application question]"
        },
        {
          "number": 3,
          "question": "[Analysis question]"
        },
        {
          "number": 4,
          "question": "[Synthesis or evaluation question]"
        }
      ]
    }
  }
}
```

**Requirements:**
- Exactly 4 questions
- Progress through Bloom's taxonomy levels
- Should preview (not duplicate) the Student Activity Packet assessment

---

#### SLIDE 18: Key Takeaways
```json
{
  "number": 18,
  "type": "content",
  "headerColor": "indigo",
  "content": {
    "headerTitle": "Key Takeaways",
    "layout": "takeaway-grid",
    "layoutData": {
      "takeaways": [
        {
          "number": 1,
          "title": "[Concept name]",
          "description": "[One-sentence synthesis]"
        }
      ]
    }
  }
}
```

**Requirements:**
- Exactly 4 takeaways
- Each should map to a learning objective
- Descriptions are synthesis, not repetition

---

#### SLIDE 19: Tomorrow's Challenge (Cliffhanger)
```json
{
  "number": 19,
  "type": "content",
  "headerColor": "amber",
  "content": {
    "headerTitle": "Tomorrow's Challenge",
    "layout": "activity-layout",
    "layoutData": {
      "main": {
        "icon": "[Relevant emoji]",
        "title": "[Learning Lab activity title]",
        "description": "[What unresolved tension carries forward? What will they solve?]"
      },
      "steps": [
        "[Step 1 - preview of Day 2 activity]",
        "[Step 2]",
        "[Step 3]",
        "[Step 4]",
        "[Step 5]"
      ]
    }
  }
}
```

**Requirements:**
- Frame as unresolved tension, not just a list of activities
- Connect explicitly to a scenario or problem from Day 1
- Make Day 2 feel necessary, not optional

---

#### SLIDE 20: Closing
```json
{
  "number": 20,
  "type": "closing",
  "content": {
    "tagline": "Building Financial Futures, One Lesson at a Time",
    "website": "www.pflacademy.co",
    "copyright": "© 2025 PFL Academy. All rights reserved."
  }
}
```

---

## State Variable Integration

When chapters include state-specific data, variables should be woven naturally into content.

### Available Variables (Common)
- `{{STATE_NAME}}`
- `{{STATE_MEDIAN_RENT}}`
- `{{STATE_MEDIAN_HOME_PRICE}}`
- `{{STATE_UNEMPLOYMENT_RATE}}`
- `{{STATE_MEDIAN_INCOME}}`
- `{{STATE_INCOME_TAX_RATE}}`
- `{{STATE_MINIMUM_WAGE}}`

### Correct Integration Pattern
```json
"question": "Why does rent cost <em>${{STATE_MEDIAN_RENT}}/month</em> in {{STATE_NAME}}?"
```

```json
"description": "At ${{STATE_MEDIAN_RENT}}/month, the number of renters equals available apartments in {{STATE_NAME}}."
```

### Anti-Pattern (DO NOT USE)
```json
"description": "Understanding your finances. in {{STATE_NAME}}"
```

Variables should appear in context where local data adds meaning - hooks, examples, stats, scenarios, discussion questions. Never append awkwardly.

---

## Metadata Requirements

```json
{
  "metadata": {
    "lChapter": "L-XX",
    "title": "[Full chapter title]",
    "subtitle": "[Engaging subtitle]",
    "totalSlides": 20,
    "hasStateVariables": true|false,
    "stateVariablesUsed": ["STATE_NAME", "..."]
  }
}
```

---

## Quality Checklist

Before marking a slide deck complete:

- [ ] `lChapter` matches the file name (not "L-XX")
- [ ] Exactly 20 slides (or 22 for combined chapters)
- [ ] Slide 2 label is "The Challenge" (not "Essential Question")
- [ ] Slides 4-5 headerTitle is "Core Concepts" (not "Key Terms")
- [ ] Slide 17 headerTitle is "Check Your Understanding"
- [ ] Slide 19 creates narrative tension for Day 2
- [ ] headerColor values use indigo/amber/emerald (not teal/purple/blue)
- [ ] State variables (if used) are woven naturally, not appended
- [ ] 4 learning objectives with action verbs
- [ ] 4 key terms (2 per slide)
- [ ] 4 check questions progressing through Bloom's
- [ ] 4 takeaways mapping to objectives
- [ ] Closing slide has correct tagline/website/copyright

---

## Remediation Patterns

### Find/Replace for Existing Files

| Find | Replace |
|------|---------|
| `"headerColor": "teal"` | `"headerColor": "indigo"` |
| `"headerColor": "purple"` | Context-dependent: `"indigo"` for content, `"emerald"` for assessment |
| `"headerColor": "blue"` | Context-dependent: `"indigo"` for content, `"amber"` for scenarios |
| `"label": "Essential Question"` | `"label": "The Challenge"` |
| `"headerTitle": "Key Terms"` | `"headerTitle": "Core Concepts"` |
| `"headerTitle": "Check for Understanding"` | `"headerTitle": "Check Your Understanding"` |
| `". in {{STATE_NAME}}"` | Rewrite to integrate naturally |
| `"lChapter": "L-XX"` | Correct chapter number |

### Structural Fixes

Files with non-standard slide counts need manual review:
- L-39: 18 slides → add 2 slides
- L-40: 14 slides → add 6 slides
- L-41: 18 slides → add 2 slides
- L-42: 18 slides → add 2 slides
- L-43: 18 slides → add 2 slides
- L-69: Missing closing → add proper slide 20

---

## Combined Chapter Format (LC-XX-XX)

For chapters that combine two related topics:

- **22 slides** (instead of 20)
- Extended core content section
- May have 6 key terms instead of 4
- Same opening/closing structure

Reference: `LC-36-37-combined-gambling.json`, `LC-39-40-combined-charitable.json`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Original | Initial template based on L-01 |
| 2.0 | 2025-12-18 | Color system aligned to Student Activity Packet; Terminology aligned; Cliffhanger enhancement; Comprehensive quality checklist |

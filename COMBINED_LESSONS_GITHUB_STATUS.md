# Combined Lessons GitHub Repository Status Report
**Date:** December 21, 2025
**Repository:** PFL-Academy-Frontend
**Location:** `/Users/justin/Library/CloudStorage/GoogleDrive-jghiglia@gmail.com/My Drive/PFL-Academy-Frontend`

---

## Executive Summary

✅ **Combined lessons ARE defined** in the GitHub repository but **content is placeholder only**.

The frontend codebase has the **structure** for Combined Lessons (Gambling & Philanthropy) but the actual curriculum **content fields are empty**.

---

## What EXISTS in GitHub

### 📍 Location: `src/data/standards.ts`

### 🎲 Standard 12: Gambling (Lines 397-420)

```typescript
{
  id: 'gambling',
  title: 'Standard 12: Gambling',
  overview: 'Understanding gambling risks and responsibilities.',
  chapters: [
    {
      id: 'gambling-risks',
      standardId: 'gambling',
      title: '12.1: Understanding the Risks of Gambling',
      description: 'Gambling risks and consequences.',
      content: 'Content for gambling risks',  // ❌ PLACEHOLDER ONLY
      learningObjectives: ['Understand gambling risks'],
      readingTime: '20 minutes'
    },
    {
      id: 'gambling-costs',
      standardId: 'gambling',
      title: '12.2: The Costs and Benefits of Gambling',
      description: 'Analyzing gambling costs and benefits.',
      content: 'Content for gambling costs',  // ❌ PLACEHOLDER ONLY
      learningObjectives: ['Analyze gambling impact'],
      readingTime: '25 minutes'
    }
  ]
}
```

### ❤️ Standard 14: Charitable Contributions (Lines 438-461)

```typescript
{
  id: 'charitable-giving',
  title: 'Standard 14: Charitable Contributions',
  overview: 'Planning and managing charitable giving.',
  chapters: [
    {
      id: 'charitable-planning',
      standardId: 'charitable-giving',
      title: '14.1: Charitable Giving and Financial Planning',
      description: 'Incorporating giving into financial plans.',
      content: 'Content for charitable planning',  // ❌ PLACEHOLDER ONLY
      learningObjectives: ['Plan charitable giving'],
      readingTime: '25 minutes'
    },
    {
      id: 'charitable-groups',
      standardId: 'charitable-giving',
      title: '14.2: Checking Out Charitable Groups',
      description: 'Evaluating charitable organizations.',
      content: 'Content for charitable groups',  // ❌ PLACEHOLDER ONLY
      learningObjectives: ['Evaluate charities'],
      readingTime: '20 minutes'
    }
  ]
}
```

---

## Mapping: HTML Slides → GitHub Repository

| HTML Slide Deck | GitHub Standard | GitHub Chapters | Content Status |
|----------------|-----------------|-----------------|----------------|
| `L-36-37-combined-gambling-slides.html` | Standard 12: Gambling | 12.1: Understanding Risks<br>12.2: Costs & Benefits | ❌ Placeholder only |
| `L-39-40-combined-philanthropy-slides.html` | Standard 14: Charitable Contributions | 14.1: Charitable Planning<br>14.2: Checking Out Groups | ❌ Placeholder only |

---

## Discrepancy Analysis

### 🔴 Naming Convention Mismatch

| File System | GitHub Repository |
|-------------|-------------------|
| L-36: Understanding Gambling Risks | 12.1: Understanding Risks of Gambling |
| L-37: Gambling Costs & Benefits | 12.2: Costs and Benefits of Gambling |
| L-39: Charitable Giving & Financial Planning | 14.1: Charitable Giving and Financial Planning |
| L-40: Researching Charitable Groups | 14.2: Checking Out Charitable Groups |

**Issue:** The GitHub repo uses "Standard 12" and "Standard 14" numbering, but file system uses "L-36", "L-37", "L-39", "L-40".

---

## What's MISSING in GitHub

### ❌ Actual Curriculum Content
- No markdown content loaded
- No learning objectives details
- No quiz/assessment data
- No skill builder definitions
- No teacher guide content

### ❌ Content Files
The repository structure shows content is rendered through:
- `ChapterContent.tsx` - Renders markdown content from `chapter.content`
- `SkillBuilder.tsx` - Renders skill builder activities
- `Quiz.tsx` - Renders quizzes
- `TeacherGuide.tsx` - Renders teacher-specific materials

**BUT:** All these components expect content from `standards.ts`, which only has placeholder strings.

---

## How Content Should Be Integrated

### Current Architecture
```
src/
├── data/
│   └── standards.ts          ← Defines structure (EXISTS)
├── components/
│   ├── ChapterContent.tsx    ← Renders content (EXISTS)
│   ├── SkillBuilder.tsx      ← Renders activities (EXISTS)
│   ├── Quiz.tsx              ← Renders assessments (EXISTS)
│   └── TeacherGuide.tsx      ← Renders teacher materials (EXISTS)
```

### What Needs to Happen

**Option 1: Direct Integration in standards.ts**
```typescript
{
  id: 'gambling-risks',
  content: `
    # Understanding the Risks of Gambling

    ## Introduction
    [Full markdown content from L-36_Student_Activity_Packet.html]

    ## Key Concepts
    ...
  `,
  skillBuilder: {
    // Skill builder data
  },
  quiz: {
    // Quiz questions
  }
}
```

**Option 2: External Content Files**
```
src/
├── content/
│   ├── gambling/
│   │   ├── 12.1-risks.md
│   │   └── 12.2-costs.md
│   └── charitable/
│       ├── 14.1-planning.md
│       └── 14.2-groups.md
```

Then import in `standards.ts`:
```typescript
import gambling121 from '../content/gambling/12.1-risks.md';
```

---

## Recommendations for Seb

### Immediate Actions

1. **Extract Content from HTML Slides**
   - Convert `L-36-37-combined-gambling-slides.html` to markdown/JSON
   - Convert `L-39-40-combined-philanthropy-slides.html` to markdown/JSON

2. **Extract from Activity Packets**
   - Source: `content-complete/English/L-36-*/assets/L-36_Student_Activity_Packet.html`
   - Source: `content-complete/English/L-37-*/assets/L-37_Student_Activity_Packet.html`
   - Source: `content-complete/English/L-39-*/assets/L-39_Student_Activity_Packet.html`
   - Source: `content-complete/English/L-40-*/assets/L-40_Student_Activity_Packet.html`

3. **Choose Integration Method**
   - **Recommended:** Create `src/content/` directory with markdown files
   - **Alternative:** Embed directly in `standards.ts` (less maintainable)

4. **Add Skill Builders**
   - Define interactive components for each chapter
   - Create JSON schemas for skill builder activities

5. **Add Assessments**
   - Create quiz questions for each chapter
   - Define knowledge checks with answer keys

### Content Extraction Strategy

```bash
# For each combined lesson:
1. Read HTML slide deck
2. Extract content sections
3. Convert to markdown format
4. Separate into:
   - Main content
   - Skill builder activities
   - Discussion prompts
   - Quiz questions
   - Teacher guidance
```

---

## Files Available for Content Extraction

### Gambling
- **HTML Slides:** `slide-decks/L-36-37-combined-gambling-slides.html`
- **Activity Packets:**
  - `content-complete/English/L-36-understanding-gambling-risks/assets/L-36_Student_Activity_Packet.html`
  - `content-complete/English/L-37-gambling-costs-benefits/assets/L-37_Student_Activity_Packet.html`
- **Teacher Guides:**
  - `content-complete/English/L-36-understanding-gambling-risks/assets/L-36_Teacher_Guide.html`
  - `content-complete/English/L-37-gambling-costs-benefits/assets/L-37_Teacher_Guide.html`

### Philanthropy
- **HTML Slides:** `slide-decks/L-39-40-combined-philanthropy-slides.html`
- **Activity Packets:**
  - `content-complete/English/L-39-charitable-giving-financial-planning/assets/L-39_Student_Activity_Packet.html`
  - `content-complete/English/L-40-researching-charitable-groups/assets/L-40_Student_Activity_Packet.html`
- **Teacher Guides:**
  - `content-complete/English/L-39-charitable-giving-financial-planning/assets/L-39_Teacher_Guide.html`
  - `content-complete/English/L-40-researching-charitable-groups/assets/L-40_Teacher_Guide.html`

---

## Next Steps

1. ✅ **Repository structure EXISTS** - Standards 12 & 14 defined
2. ❌ **Content is MISSING** - Only placeholder text
3. 🔧 **Action Required:** Extract content from HTML files and populate GitHub repo
4. 📝 **Suggested Tool:** Create content extraction script to convert HTML → Markdown
5. 🧪 **Testing:** Verify content renders correctly in `ChapterContent.tsx`

---

**Report Location:** `/slide-deck-templates/COMBINED_LESSONS_GITHUB_STATUS.md`
**Last Updated:** December 21, 2025

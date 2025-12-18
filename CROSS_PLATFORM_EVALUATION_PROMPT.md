# PFL Academy Slide Deck Design Evaluation

## Context

I'm building PFL Academy, a comprehensive K-12 financial literacy education platform. We have three interconnected content deliverables that must work together as a cohesive system:

1. **Slide Decks** (JSON-based, rendered as interactive presentations) - Day 1 content delivery
2. **Teacher Guides** (HTML) - Instructor support materials with pacing, differentiation, and assessment
3. **Student Workbooks** (HTML) - Day 2 "Learning Lab" activities with interactive exercises

I need you to evaluate whether our **Slide Deck structure** maintains consistency in style, pedagogical quality, and design philosophy with the Teacher Guides and Student Workbooks.

---

## Our Pedagogical Framework: COST

We use the **COST Framework** adapted for 55-minute class periods:

- **C**onceptual (Hook + Essential Question) - 5 min
- **O**perational (Key Terms + Core Content) - 25 min  
- **S**ituational (Scenarios + Discussion) - 15 min
- **T**ransfer (Assessment + Activity Preview) - 10 min

Our guiding principle: Move from "2D calculator" experiences to "3D simulator" experiences that engage students through scenario-based learning. Content must be both **FUN** (engaging enough to capture attention) and **STICK** (memorable experiences that promote retention).

---

## The Golden Template: Slide Deck Structure (L-60)

This is our established "golden template" - a complete 20-slide lesson structure:

```
SLIDES 1-5: SETUP (CONCEPTUAL)
├── Slide 1: Title
│   ├── type: "title"
│   ├── content: {title, titleSize: "large", subtitle}
│
├── Slide 2: Hook (Essential Question)
│   ├── type: "hook"
│   ├── content: {label: "Essential Question", question: [engaging hook with <em> emphasis]}
│
├── Slide 3: Learning Objectives
│   ├── type: "content"
│   ├── headerColor: "teal"
│   ├── layout: "objectives-expanded"
│   ├── layoutData: {objectives: [4 objectives with number, verb, description]}
│
├── Slide 4: Key Terms (2 terms)
│   ├── type: "content"
│   ├── headerColor: "purple"
│   ├── layout: "vocab-container"
│   ├── layoutData: {terms: [{term, definition, example}, {term, definition, example}]}
│
└── Slide 5: Key Terms (2 more terms)
    └── Same structure as Slide 4

SLIDES 6-14: CORE CONTENT (OPERATIONAL + SITUATIONAL)
├── Flexible mix of layouts based on topic needs:
│   ├── "balanced-layout" - Two-panel with leftPanel (paragraphs, highlightBox) + rightPanel (stats, infoCard)
│   ├── "concept-full" - Full-width with title, paragraphs, bulletPoints, keyPoint
│   ├── "scenario-layout" - Scenario with icon, name, paragraphs + outcomes array
│   ├── "comparison-grid" - Two columns with leftColumn/rightColumn items
│
├── Typically includes 1-2 complete scenarios with outcome formatting:
│   └── outcomes: [{type: "before/after", label, value, detail}]
│
└── Core content builds understanding through:
    ├── Explanation of concepts
    ├── Real-world examples
    ├── Visual data (stats with color coding)
    └── Application scenarios

SLIDES 15-16: DISCUSSION (SITUATIONAL)
├── Slide 15: Discussion Question
│   ├── type: "discussion"
│   ├── variant: "teal"
│   ├── content: {badge: "Discussion", question: [open-ended question]}
│
└── Slide 16: Personal Reflection
    ├── type: "discussion"
    ├── variant: "purple"
    └── content: {badge: "Personal Reflection", question: [reflective prompt]}

SLIDES 17-18: ASSESSMENT (TRANSFER)
├── Slide 17: Check for Understanding
│   ├── type: "content"
│   ├── headerColor: "purple"
│   ├── layout: "check-grid"
│   └── layoutData: {questions: [4 questions with number and question]}
│
└── Slide 18: Key Takeaways
    ├── type: "content"
    ├── headerColor: "teal"
    ├── layout: "takeaway-grid"
    └── layoutData: {takeaways: [4 takeaways with number, title, description]}

SLIDES 19-20: WRAP-UP (TRANSFER)
├── Slide 19: Activity Preview
│   ├── type: "content"
│   ├── headerColor: "blue"
│   ├── layout: "activity-layout"
│   └── layoutData: {main: {icon, title, description}, steps: [5 steps]}
│
└── Slide 20: Closing
    ├── type: "closing"
    └── content: {tagline, website, copyright}
```

---

## Teacher Guide Structure (HTML)

The Teacher Guide provides instructors with comprehensive support:

**Key Components:**
- Fixed purple header with PFL Academy branding
- Sticky sidebar with chapter navigation and resource links
- Content Guide tab / Learning Lab tab toggle
- Color-coded sections:
  - Purple (diff-section): Differentiation Strategies - Supporting All Learners
  - Green (assess-section): Assessment Opportunities
  - Blue (support-section): Instructor Support

**Content Approach:**
- Pacing guidance tied to slide progression
- Discussion facilitation prompts
- Common misconceptions and how to address them
- Extension activities for advanced learners
- Scaffolding strategies for struggling learners

---

## Student Workbook Structure (HTML - Day 2 Learning Lab)

The Learning Lab is the hands-on Day 2 experience:

**Key Components:**
- Learning Objectives (light blue background)
- Podcast/Video Review section (10 min)
- Learning Stations (interactive, numbered, with progress tracking)
- Discussion Prompts (blue with left border)
- Activity Timers (yellow with orange border)
- Important Notes (amber with warning styling)
- Progress bar with station completion tracking

**Format Options:**
1. Multi-Activity Format - Multiple independent stations
2. Project-Based Format - Single extended project with stages
3. Case Study Format - Deep analysis with analytical framework

**Design Philosophy:**
- Interactive elements with hover effects
- Toast notifications for user feedback
- Station indicators for navigation
- Input persistence via localStorage
- Professional polish with gradients and shadows

---

## UI Standardization (Brand Consistency)

**Color System:**
- Primary: #5849da (Brand purple)
- Secondary: #374151 (Dark gray)
- Sidebar: #f5f5f7 (Light gray)
- Section accents: Purple (differentiation), Green (assessment), Blue (support)

**Component Standards:**
- .learning-objectives: Light blue background
- .discussion-prompt: Blue background with left border
- .case-study: Light blue background with left border
- .skill-builder: Light purple background
- .activity-timer: Yellow background with orange left border

---

## State Variable Integration (When Used)

Some chapters include state-specific data (e.g., {{STATE_NAME}}, {{STATE_MEDIAN_RENT}}, {{STATE_UNEMPLOYMENT_RATE}}).

**Proper Integration:**
- Variables woven naturally into content, not appended
- Used in hooks, examples, stats, scenarios, and discussion questions
- Makes content locally relevant without feeling forced

**Anti-pattern to avoid:**
- "Some content here. in {{STATE_NAME}}" - awkward appending

---

## Evaluation Questions

Please analyze the slide deck structure against the Teacher Guide and Student Workbook patterns and answer:

### 1. Pedagogical Alignment
- Does the 20-slide structure support the COST framework effectively?
- Are the slide types appropriately sequenced for cognitive load management?
- Does the structure create natural handoff points to Day 2 Learning Labs?

### 2. Design Consistency
- Are the color-coding conventions (teal, purple, blue) used consistently across all three deliverables?
- Do the layout types in slide decks mirror the visual hierarchy of Teacher Guides and Student Workbooks?
- Is there stylistic coherence in how content is chunked and presented?

### 3. Content Quality Markers
- Do the slide deck structures support the same depth of scenarios that Teacher Guides suggest facilitating?
- Are Check for Understanding questions appropriately rigorous?
- Do takeaways synthesize at the right level of abstraction?

### 4. Structural Gaps or Redundancies
- Are there any components in Teacher Guides or Student Workbooks that should be reflected in slides but aren't?
- Are there slide elements that seem disconnected from the broader curriculum system?
- Is the slide count (20) appropriate, or would flexibility help certain topic types?

### 5. Improvement Recommendations
- What specific enhancements would strengthen the slide deck structure?
- Are there layout types missing that would better serve certain content?
- How could state variable integration be improved?
- Are there interaction patterns from Student Workbooks that should inform slide design?

### 6. Overall Assessment
- Rate the current alignment (1-10) between slide decks and the Teacher Guide/Student Workbook system
- What is the single highest-impact improvement you'd recommend?
- Does this structure scale well across 69 chapters with varying topics?

---

## Additional Context

- Platform serves school districts across 36 states with financial literacy mandates
- Target audience: High school students (primarily 11th grade)
- Delivery models: 90-hour teacher-led, 30-hour blended, 45-hour independent study
- Content must work for both synchronous classroom and self-paced contexts

Please provide specific, actionable feedback. If you see structural patterns that could be improved, suggest concrete alternatives with rationale.

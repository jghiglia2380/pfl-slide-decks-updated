# SLIDE DECK REMEDIATION INSTRUCTIONS
## For Claude Code Execution
## Date: December 20, 2025

---

## OVERVIEW

This document provides EXPLICIT instructions for remediating issues in slide deck JSON files. 

**FILES TO REMEDIATE:**
1. **SEVERE State Variable Corruption (4 files):** L-10, L-20, L-21, L-23
2. **Metadata Issues (3 files):** L-07, L-08, L-22
3. **Title Spacing Issues (3 files):** L-16, L-18, L-19

**GOLDEN TEMPLATES (DO NOT MODIFY):** L-45.json, L-46.json, L-50.json

---

## ISSUE TYPE 1: METADATA ISSUES (L-07, L-08, L-22)

### Problem
Files claim `hasStateVariables: true` but NO state variables appear anywhere in the content.

### Files Affected
- L-07.json
- L-08.json  
- L-22.json

### Fix Required
Change metadata from:
```json
"hasStateVariables": true,
"stateVariablesUsed": [
  "STATE_NAME",
  "STATE_INCOME_TAX_RATE"
]
```

To:
```json
"hasStateVariables": false,
"stateVariablesUsed": []
```

### Verification
After fix, search file for `{{` - should return 0 matches if metadata says `hasStateVariables: false`.

---

## ISSUE TYPE 2: TITLE SPACING ISSUES (L-16, L-18, L-19)

### Problem
Missing spaces in title fields.

### Files and Fixes

**L-16.json:**
- WRONG: `"Evaluating Saving &Investment Strategies"`
- RIGHT: `"Evaluating Saving & Investment Strategies"`

**L-18.json:**
- WRONG: `"UnderstandingMoney Risks"`
- RIGHT: `"Understanding Money Risks"`

**L-19.json:**
- WRONG: `"Planning forRetirement"`
- RIGHT: `"Planning for Retirement"`

### Fix Locations
Fix in BOTH places:
1. `metadata.title`
2. `slides[0].content.title` (slide number 1, type "title")

---

## ISSUE TYPE 3: SEVERE STATE VARIABLE CORRUPTION (L-10, L-20, L-21, L-23)

### Problem Pattern
`in {{STATE_NAME}}` has been APPENDED incorrectly to nearly every field instead of being NATURALLY INTEGRATED into sentence structures.

### Files Affected
- L-10.json
- L-20.json
- L-21.json
- L-23.json

### CRITICAL RULES - READ CAREFULLY

**NEVER append `in {{STATE_NAME}}` to:**
- Labels (e.g., `"Essential Question"` NOT `"Essential Question in {{STATE_NAME}}"`)
- Stats values (e.g., `"75%"` NOT `"75% in {{STATE_NAME}}"`)
- Stats labels (e.g., `"Maximum Fraud Penalty"` NOT `"Maximum Fraud Penalty in {{STATE_NAME}}"`)
- Term names in vocab sections (e.g., `"Tax Planning"` NOT `"Tax Planning in {{STATE_NAME}}"`)
- Icons/emojis (e.g., `"👩‍💼"` NOT `"👩‍💼 in {{STATE_NAME}}"`)
- Outcome labels, values, or details in scenarios
- Badge text (e.g., `"Discussion"` NOT `"Discussion in {{STATE_NAME}}"`)
- Closing slide tagline, website, or copyright

**State variables SHOULD appear in:**
- Subtitle (OK: `"Strategic Approaches to Legal Tax Management in {{STATE_NAME}}"`)
- Natural sentence flow in paragraphs
- Natural sentence flow in questions (OK: `"How do taxes work in {{STATE_NAME}}?"`)
- Natural integration in bullet points

---

## GOLDEN TEMPLATE EXCERPTS - CORRECT PATTERNS

### CORRECT: Hook Slide (from L-45.json - no state vars)
```json
{
  "number": 2,
  "type": "hook",
  "content": {
    "label": "Essential Question",
    "question": "What if you could turn <em>your skills and passions</em><br>into income—while keeping your day job<br>or building something <em>entirely your own</em>?"
  }
}
```

### CORRECT: Hook Slide WITH State Variable (from L-46.json)
```json
{
  "number": 2,
  "type": "hook",
  "content": {
    "label": "Essential Question",
    "question": "In <em>{{STATE_NAME}}</em>, why do some people pay<br><em>$100,000 more</em> for vehicles over their lifetime—<br>even if they drive <em>similar cars</em>?"
  }
}
```
**NOTE:** Label is PLAIN, state variable is INSIDE the question text naturally.

### WRONG: Hook Slide (from corrupted files)
```json
{
  "number": 2,
  "type": "hook",
  "content": {
    "label": "Essential Question in {{STATE_NAME}}",
    "question": "What's the difference between <em>legal tax planning</em><br>and <em>illegal tax evasion</em>? in {{STATE_NAME}}"
  }
}
```
**PROBLEMS:** Label has appended text, question ends with awkward append.

---

### CORRECT: Vocab Terms (from L-45.json)
```json
{
  "term": "Entrepreneurship",
  "definition": "The activity of setting up and running a business, taking on financial risks in the hope of profit.",
  "example": "Starting a web design agency, opening a bakery, launching an app company"
}
```

### CORRECT: Vocab Terms WITH State Variable (from L-46.json)
```json
{
  "term": "Total Cost of Ownership",
  "definition": "Complete cost: purchase, financing, insurance, fuel, maintenance, repairs, and depreciation.",
  "example": "In {{STATE_NAME}}, monthly payment is only part—add {{STATE_SALES_TAX}}% sales tax, registration, insurance."
}
```
**NOTE:** Term name is PLAIN, state variable appears naturally in example sentence.

### WRONG: Vocab Terms (from corrupted files)
```json
{
  "term": "Tax Planning in {{STATE_NAME}}",
  "definition": "Legal strategies to reduce tax liability...",
  "example": "Contributing to a 401(k)..."
}
```
**PROBLEM:** Term name has appended text.

---

### CORRECT: Stats (from L-45.json)
```json
{
  "value": "44%",
  "label": "of Americans Have Side Hustles",
  "color": "teal"
}
```

### CORRECT: Stats WITH State Variable (from L-46.json)
```json
{
  "value": "{{STATE_SALES_TAX}}%",
  "label": "{{STATE_NAME}} Sales Tax",
  "color": "rose"
}
```
**NOTE:** Variable IS the value or part of label - not appended.

### WRONG: Stats (from corrupted files)
```json
{
  "value": "75% in {{STATE_NAME}}",
  "label": "Maximum Fraud Penalty in {{STATE_NAME}}",
  "color": "rose"
}
```
**PROBLEMS:** Both value AND label have awkward appends.

---

### CORRECT: Scenario Layout (from L-45.json)
```json
{
  "scenario": {
    "icon": "👨‍💻",
    "name": "Jordan's Tutoring Side Hustle",
    "paragraphs": [...]
  },
  "outcomes": [
    {
      "type": "before",
      "label": "Time Investment",
      "value": "10 hrs/wk",
      "detail": "Fits around classes"
    }
  ]
}
```

### CORRECT: Scenario WITH State Variable (from L-46.json)
```json
{
  "scenario": {
    "icon": "👩",
    "name": "Mia's Buy-and-Keep Strategy in {{STATE_NAME}}",
    "paragraphs": [
      "Mia considered leasing a new SUV... instead purchased a <span class=\"highlight-text\">certified pre-owned sedan for $18,000</span> in {{STATE_NAME}}.",
      "..."
    ]
  },
  "outcomes": [
    {
      "type": "before",
      "label": "Total Paid",
      "value": "~$20K",
      "detail": "+ $3K down payment"
    }
  ]
}
```
**NOTE:** State variable in NAME and PARAGRAPHS is fine. Outcomes are PLAIN.

### WRONG: Scenario (from corrupted files)
```json
{
  "scenario": {
    "icon": "👩‍💼 in {{STATE_NAME}}",
    "name": "Kate's Proactive Tax Planning Approach in {{STATE_NAME}}",
    "paragraphs": [...]
  },
  "outcomes": [
    {
      "type": "after",
      "label": "Tax Reduction in {{STATE_NAME}}",
      "value": "$3,400+ in {{STATE_NAME}}",
      "detail": "Annual savings through planning in {{STATE_NAME}}"
    }
  ]
}
```
**PROBLEMS:** Icon has append, ALL outcome fields have appends.

---

### CORRECT: Discussion Slide (from L-45.json)
```json
{
  "number": 15,
  "type": "discussion",
  "variant": "teal",
  "content": {
    "badge": "Discussion",
    "question": "What made Jordan's and Maya's side hustles successful?<br><br>What strategies did they use to minimize risk while growing their businesses?"
  }
}
```

### CORRECT: Discussion WITH State Variable (from L-46.json)
```json
{
  "number": 15,
  "type": "discussion",
  "variant": "teal",
  "content": {
    "badge": "Discussion",
    "question": "In {{STATE_NAME}}, with {{STATE_SALES_TAX}}% sales tax and ${{STATE_INSURANCE_AVG_TEEN}}/mo teen insurance, what financial trade-offs did Mia and James make?<br><br>When might James's approach make sense for someone?"
  }
}
```
**NOTE:** Badge is PLAIN, state variables are INSIDE the question naturally.

### WRONG: Discussion (from corrupted files)
```json
{
  "badge": "Discussion in {{STATE_NAME}}",
  "question": "What factors would be most important to you when choosing a financial service provider? in {{STATE_NAME}}"
}
```
**PROBLEMS:** Badge has append, question ends with awkward append.

---

### CORRECT: Closing Slide (from L-45.json and L-46.json - BOTH identical)
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

### WRONG: Closing Slide (from corrupted files)
```json
{
  "tagline": "Building Financial Futures, One Lesson at a Time in {{STATE_NAME}}",
  "website": "www.pflacademy.co in {{STATE_NAME}}",
  "copyright": "© 2025 PFL Academy. All rights reserved. in {{STATE_NAME}}"
}
```
**PROBLEMS:** ALL three fields have appends. Closing slides should NEVER have state variables.

---

## REGEX PATTERNS FOR FINDING ISSUES

### Find awkward appends at end of strings:
```regex
" in \{\{STATE_NAME\}\}"$
```

### Find `in {{STATE_NAME}}` in places it shouldn't be:
```regex
"(label|badge|value|detail|icon|tagline|website|copyright)":\s*"[^"]*in \{\{STATE_NAME\}\}"
```

### Find term names with appends:
```regex
"term":\s*"[^"]*in \{\{STATE_NAME\}\}"
```

### Find missing spaces before common words:
```regex
[a-z](for|and|the|to|in|of|vs|&)[A-Z]
```

---

## FILE-BY-FILE REMEDIATION CHECKLIST

### L-07.json
- [ ] Change `hasStateVariables` to `false`
- [ ] Change `stateVariablesUsed` to `[]`
- [ ] Verify: Search for `{{` returns 0 matches

### L-08.json
- [ ] Change `hasStateVariables` to `false`
- [ ] Change `stateVariablesUsed` to `[]`
- [ ] Verify: Search for `{{` returns 0 matches

### L-22.json
- [ ] Change `hasStateVariables` to `false`
- [ ] Change `stateVariablesUsed` to `[]`
- [ ] Verify: Search for `{{` returns 0 matches

### L-16.json
- [ ] Fix metadata.title: "Evaluating Saving & Investment Strategies"
- [ ] Fix slides[0].content.title: "Evaluating Saving & Investment Strategies"

### L-18.json
- [ ] Fix metadata.title: "Understanding Money Risks"
- [ ] Fix slides[0].content.title: "Understanding Money Risks"

### L-19.json
- [ ] Fix metadata.title: "Planning for Retirement"
- [ ] Fix slides[0].content.title: "Planning for Retirement"

### L-10.json (SEVERE - Full remediation)
- [ ] Slide 2: Remove " in {{STATE_NAME}}" from label, fix question ending
- [ ] Slide 4-5: Remove " in {{STATE_NAME}}" from ALL term names
- [ ] Slide 5: ALSO fix missing spaces: "Tax-Advantaged Accounts", "Tax Compliance"
- [ ] Slide 6: Remove " in {{STATE_NAME}}" from ALL stats values and labels
- [ ] Slide 8: Remove " in {{STATE_NAME}}" from ALL stats values and labels
- [ ] Slide 10: Remove " in {{STATE_NAME}}" from ALL stats values and labels
- [ ] Slide 12: Remove " in {{STATE_NAME}}" from ALL stats values and labels
- [ ] Slide 13: Remove " in {{STATE_NAME}}" from icon, ALL outcome fields
- [ ] Slide 14: Remove " in {{STATE_NAME}}" from icon, ALL outcome fields
- [ ] Slide 15: Remove " in {{STATE_NAME}}" from badge, fix question ending
- [ ] Slide 16: Remove " in {{STATE_NAME}}" from badge, fix question ending
- [ ] Slide 20: Remove " in {{STATE_NAME}}" from tagline, website, copyright
- [ ] Review: Ensure state variables ONLY appear naturally in sentences/paragraphs
- [ ] Update metadata.stateVariablesUsed to reflect actual variables used (may need to be empty)

### L-20.json (SEVERE - Full remediation)
- [ ] Same checklist as L-10 - audit each slide type for corruption
- [ ] Remove ALL awkward " in {{STATE_NAME}}" appends
- [ ] Keep ONLY natural integrations in sentences/paragraphs
- [ ] Fix closing slide

### L-21.json (SEVERE - Full remediation)
- [ ] Same checklist as L-10 - audit each slide type for corruption
- [ ] Remove ALL awkward " in {{STATE_NAME}}" appends
- [ ] Keep ONLY natural integrations in sentences/paragraphs
- [ ] Fix closing slide

### L-23.json (SEVERE - Full remediation)
- [ ] Same checklist as L-10 - audit each slide type for corruption
- [ ] Remove ALL awkward " in {{STATE_NAME}}" appends
- [ ] Keep ONLY natural integrations in sentences/paragraphs
- [ ] Fix closing slide

---

## VALIDATION STEPS AFTER REMEDIATION

1. **JSON Validity:** Ensure file is valid JSON (no syntax errors)
2. **Slide Count:** Confirm exactly 20 slides
3. **Metadata Accuracy:** `hasStateVariables` matches actual content
4. **No Awkward Appends:** Search for `" in {{STATE_NAME}}"` at string endings
5. **Natural Integration:** State variables only appear mid-sentence where grammatically correct
6. **Closing Slide Clean:** tagline, website, copyright have NO state variables

---

## SUMMARY OF WHAT TO FIX

| File | Issue Type | Priority |
|------|------------|----------|
| L-10 | SEVERE state variable corruption | HIGH |
| L-20 | SEVERE state variable corruption | HIGH |
| L-21 | SEVERE state variable corruption | HIGH |
| L-23 | SEVERE state variable corruption | HIGH |
| L-07 | Metadata claims vars not used | MEDIUM |
| L-08 | Metadata claims vars not used | MEDIUM |
| L-22 | Metadata claims vars not used | MEDIUM |
| L-16 | Title spacing | LOW |
| L-18 | Title spacing | LOW |
| L-19 | Title spacing | LOW |

---

## END OF REMEDIATION INSTRUCTIONS

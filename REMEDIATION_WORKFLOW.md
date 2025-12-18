# PFL Academy Slide Deck Remediation Workflow

**Created:** December 18, 2025  
**Purpose:** Complete instructions for applying the Golden Template Specification to all 71 slide deck files  
**Reference:** `GOLDEN_TEMPLATE_SPECIFICATION.md`

---

## Overview

This document provides a systematic workflow to bring all slide deck JSON files into compliance with the Golden Template Specification v2.0. Work can be done file-by-file with Claude Code.

### Summary of Work

| Category | Count | Effort Level |
|----------|-------|--------------|
| 100% Complete (need color/terminology fixes only) | 30 | Low - find/replace |
| 70-95% Complete (fixable issues) | 21 | Medium - targeted fixes |
| Skeleton Files (need full content) | 20 | High - full content creation |
| **Total** | **71** | |

---

## Phase 1: Global Find/Replace (All 71 Files)

These changes apply to ALL files, including complete ones. Run these first.

### 1.1 Color System Alignment

| Find | Replace With |
|------|--------------|
| `"headerColor": "teal"` | `"headerColor": "indigo"` |
| `"headerColor": "purple"` | See context rules below |
| `"headerColor": "blue"` | See context rules below |

**Context rules for purple/blue:**
- If slide is "Check Your Understanding" → `"headerColor": "emerald"`
- If slide is scenario/challenge → `"headerColor": "amber"`
- Otherwise → `"headerColor": "indigo"`

### 1.2 Terminology Alignment

| Find | Replace With |
|------|--------------|
| `"label": "Essential Question"` | `"label": "The Challenge"` |
| `"headerTitle": "Key Terms"` | `"headerTitle": "Core Concepts"` |
| `"headerTitle": "Check for Understanding"` | `"headerTitle": "Check Your Understanding"` |

### 1.3 State Variable Anti-Pattern Fix

**Find pattern:** `". in {{STATE_NAME}}"` or `"content. in {{STATE_NAME}}"`

**Fix:** Rewrite to integrate naturally. Example:
- Bad: `"Understanding your finances. in {{STATE_NAME}}"`
- Good: `"Understanding your finances as a {{STATE_NAME}} resident"`

Files with this issue: L-10, L-11, L-12, L-16, L-17, L-18, L-19, L-20, L-21, L-23, L-31, L-37, L-38, L-39, L-40, L-41, L-42, L-43, L-44

---

## Phase 2: Fix Specific Issues by File

### 2.1 Files with Title/Term Spacing Issues (18 files)

These have concatenated words that need spaces added:

| File | Issue | Fix |
|------|-------|-----|
| L-09 | "Deductions& Credits" | "Deductions & Credits" |
| L-12 | "AccountFees" | "Account Fees" |
| L-16 | "Saving &Investment" | "Saving & Investment" |
| L-18 | "UnderstandingMoney" | "Understanding Money" |
| L-19 | "Planning forRetirement" | "Planning for Retirement" |
| L-25 | "UnderstandingStudent Loans" | "Understanding Student Loans" |
| L-26 | "Credit Card Useand Management" | "Credit Card Use and Management" |
| L-28 | "Consumer FraudProtection" | "Consumer Fraud Protection" |
| L-29 | "Identity TheftPrevention & Recovery" | "Identity Theft Prevention & Recovery" |
| L-37 | "Costs and Benefitsof Gambling" | "Costs and Benefits of Gambling" |
| L-38 | "Managing HighLevels of Debt" | "Managing High Levels of Debt" |
| L-39 | "Charitable Giving &Financial Planning" | "Charitable Giving & Financial Planning" |
| L-40 | "Checking OutCharitable Groups" | "Checking Out Charitable Groups" |
| L-41 | "Career Explorationand Goal Setting" | "Career Exploration and Goal Setting" |
| L-42 | "Resume Building &Personal Branding" | "Resume Building & Personal Branding" |
| L-43 | "Job ApplicationProcess" | "Job Application Process" |
| L-44 | "Interview Skills &Workplace" | "Interview Skills & Workplace Readiness" |
| L-45 | "Entrepreneurship &Side Hustles" | "Entrepreneurship & Side Hustles" |

### 2.2 Files with Non-Standard Slide Count

| File | Current | Target | Action |
|------|---------|--------|--------|
| L-39 | 18 slides | 20 slides | Add 2 slides to core content |
| L-40 | 14 slides | 20 slides | Add 6 slides (likely missing scenarios + discussion) |
| L-41 | 18 slides | 20 slides | Add 2 slides |
| L-42 | 18 slides | 20 slides | Add 2 slides |
| L-43 | 18 slides | 20 slides | Add 2 slides |
| L-69 | 20 slides but wrong structure | 20 slides | Replace slide 20 (activity) with proper closing, shift activity to slide 19 |

### 2.3 Files with Wrong lChapter Metadata (11 files)

These skeleton files have `"lChapter": "L-XX"` instead of correct chapter number:

| File | Current | Correct |
|------|---------|---------|
| L-05.json | "L-XX" | "L-05" |
| L-07.json | "L-XX" | "L-07" |
| L-08.json | "L-XX" | "L-08" |
| L-13.json | "L-XX" | "L-13" |
| L-14.json | "L-XX" | "L-14" |
| L-15.json | "L-XX" | "L-15" |
| L-22.json | "L-XX" | "L-22" |
| L-33.json | "L-XX" | "L-33" |
| L-34.json | "L-XX" | "L-34" |
| L-35.json | "L-XX" | "L-35" |
| L-36.json | "L-XX" | "L-36" |

---

## Phase 3: Skeleton File Content Creation (20 Files)

These files have the structure but empty/placeholder content. Each requires full content population.

### Priority Order (based on curriculum flow)

**Tier 1 - Core Early Chapters (do first):**
1. L-05 - Financial Goals
2. L-07 - Tax Brackets
3. L-08 - Tax Filing Requirements

**Tier 2 - Banking & Saving:**
4. L-13 - Banking Tools
5. L-14 - Saving Basics
6. L-15 - Investment Basics

**Tier 3 - Credit:**
7. L-22 - Credit Sources
8. L-24 - Credit Legislation
9. L-25 - Student Loans
10. L-26 - Credit Card Management
11. L-27 - Shopping Strategies
12. L-28 - Consumer Fraud Protection
13. L-29 - Identity Theft Prevention

**Tier 4 - Risk Management:**
14. L-33 - Risk Management Basics
15. L-34 - Insurance Fundamentals
16. L-35 - Insurance Types
17. L-36 - Insurance Selection

**Tier 5 - Investment:**
18. L-47 - Investment Types
19. L-48 - Economic Systems
20. L-49 - Scarcity & Choice

### Content Creation Workflow

For each skeleton file:

1. **Reference the Student Activity Packet** at:
   ```
   /Users/justin/Library/Mobile Documents/com~apple~CloudDocs/Documents/pfl-academy/content-complete/English/L-XX-[chapter-name]/assets/L-XX_Student_Activity_Packet.html
   ```

2. **Extract from Student Packet:**
   - The Challenge scenario and framing question
   - Learning objectives
   - Key terms (4 terms with definitions and examples)
   - Scenario content for slides 13-14
   - Check Your Understanding questions

3. **Build core content slides (6-12)** based on:
   - Background section from Student Packet
   - Teacher Guide pacing notes
   - Topic-appropriate layouts (balanced-layout, concept-full, comparison-grid)

4. **Ensure slide 19 creates Day 2 cliffhanger:**
   - Reference the Learning Lab activity
   - Frame unresolved tension from Day 1

---

## Phase 4: Quality Verification

After fixing each file, verify against this checklist:

### Structural Checklist
- [ ] `lChapter` matches filename (e.g., "L-05" for L-05.json)
- [ ] `totalSlides` is 20 (or 22 for combined chapters)
- [ ] Exactly 20 slides in the slides array
- [ ] Slides numbered 1-20 sequentially

### Terminology Checklist
- [ ] Slide 2 label is "The Challenge"
- [ ] Slides 4-5 headerTitle is "Core Concepts"
- [ ] Slide 17 headerTitle is "Check Your Understanding"
- [ ] Slide 19 headerTitle is "Tomorrow's Challenge"

### Color Checklist
- [ ] No instances of `"headerColor": "teal"`
- [ ] No instances of `"headerColor": "purple"` (except properly converted)
- [ ] No instances of `"headerColor": "blue"` (except properly converted)
- [ ] Check Your Understanding uses `"headerColor": "emerald"`
- [ ] Scenarios use `"headerColor": "amber"`

### Content Checklist
- [ ] 4 learning objectives with action verbs
- [ ] 4 key terms (2 per slide on slides 4-5)
- [ ] 4 check questions
- [ ] 4 takeaways
- [ ] No spacing errors in titles/terms
- [ ] State variables (if used) integrated naturally, not appended

### Closing Checklist
- [ ] Slide 20 is type "closing"
- [ ] Tagline: "Building Financial Futures, One Lesson at a Time"
- [ ] Website: "www.pflacademy.co"
- [ ] Copyright: "© 2025 PFL Academy. All rights reserved."

---

## Claude Code Workflow

When working on a file, use this workflow:

### Step 1: Read the file
```
Read slide-content/L-XX.json
```

### Step 2: Identify issues
Compare against Golden Template Specification and this checklist.

### Step 3: Apply fixes
For simple fixes (color, terminology), use find/replace.
For content creation, reference the Student Activity Packet.

### Step 4: Validate
Run through the Quality Verification checklist.

### Step 5: Commit
```bash
git add slide-content/L-XX.json
git commit -m "Fix L-XX: [brief description of fixes]"
```

### Step 6: Move to next file

---

## File Status Reference

### ✅ Complete Files (30) - Need Phase 1 fixes only

L-01, L-02, L-03, L-04, L-06, L-30, L-32, L-45, L-46, L-50, L-51, L-52, L-53, L-54, L-55, L-56, L-57, L-58, L-59, L-60, L-61, L-62, L-63, L-64, L-65, L-66, L-67, L-68, LC-36-37, LC-39-40

### ⚠️ Fixable Files (21) - Need Phase 1 + Phase 2 fixes

L-09, L-10, L-11, L-12, L-16, L-17, L-18, L-19, L-20, L-21, L-23, L-31, L-37, L-38, L-39, L-40, L-41, L-42, L-43, L-44, L-69

### ❌ Skeleton Files (20) - Need Phase 1 + Phase 2 + Phase 3

L-05, L-07, L-08, L-13, L-14, L-15, L-22, L-24, L-25, L-26, L-27, L-28, L-29, L-33, L-34, L-35, L-36, L-47, L-48, L-49

---

## Commit Strategy

Use meaningful commit messages:

- `"Apply color/terminology fixes to L-XX"` - for Phase 1 changes
- `"Fix spacing issues in L-XX"` - for Phase 2.1
- `"Add missing slides to L-XX (18→20)"` - for Phase 2.2
- `"Populate skeleton content for L-XX"` - for Phase 3
- `"Complete L-XX remediation"` - for files needing multiple fix types

Push regularly:
```bash
git push
```

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/jghiglia2380/pfl-slide-decks-updated.git
   cd pfl-slide-decks-updated
   ```

2. Start Claude Code:
   ```bash
   claude
   ```

3. Tell Claude:
   ```
   Read GOLDEN_TEMPLATE_SPECIFICATION.md and REMEDIATION_WORKFLOW.md, then start with the Phase 1 global fixes on the complete files (L-01, L-02, etc.)
   ```

4. Work through files systematically.

---

## Notes

- The `content-complete` directory with Student Activity Packets is NOT in this repo (it's in the main pfl-academy folder on your local machine)
- For skeleton files, you'll need access to those reference materials
- Combined chapters (LC-36-37, LC-39-40) use 22 slides - don't try to reduce to 20

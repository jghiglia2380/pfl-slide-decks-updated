Markdown# PFL Academy Slide Deck Generator

## Overview
**Status:** ✅ Production Ready (All 71 Chapters Complete)

This system generates state-customized HTML slide decks for the PFL Academy curriculum. It combines a master template, chapter content JSON files, and state-specific variables to produce ready-to-use presentation materials for all 36 states.

This repository contains the finalized content for **all** PFL Academy chapters (L-01 through L-71), including the specialized Combined Lessons (CL-Gambling, CL-Philanthropy).

## Quick Start

### Prerequisites
* Node.js v16+ installed
* Access to the following directories:
    * `/state-data/states/` - State variable JSON files
    * `/Simple-Data-Files-Updated/` - Chapter mapping files

### Installation
```bash
cd slide-deck-templates
npm install
Basic UsageGenerate slides for a specific state and chapter:Bashnode generate-slide-decks.js --state=oklahoma --chapter=L-03
System ArchitectureFile Structureslide-deck-templates/
├── slide-template.html          # Master HTML template
├── generate-slide-decks.js      # Generator script
├── slide-content/               # Chapter content JSON files (L-01 to L-71)
│   ├── L-01.json                # Jobs vs. Careers
│   ├── L-03.json                # Income and Taxes
│   ├── L-50.json                # Supply & Demand (Localized)
│   ├── CL-Gambling.json         # Combined Gambling Chapter
│   └── ... (All 71 chapters)
├── output/                      # Generated slide decks
└── DATA_DICTIONARY.md           # Engineering Spec for State Variables
State Variables & LocalizationVariable Documentation:Please refer to DATA_DICTIONARY.md in the root directory for the technical specification of all state variables, including update frequencies (Monthly/Quarterly/Annually) and fallback logic.Localization Status:Standard Chapters: L-01 through L-71 are complete.Combined Chapters: CL-Gambling and CL-Philanthropy are complete and located in the slide-content directory.Localization: 26 chapters have active state variables enabled. See LOCALIZATION_MASTER_MAP.md for the full inventory.Variable InterpolationState variables use the {{VARIABLE_NAME}} syntax and are automatically replaced during generation.Example:"text": "In {{STATE_NAME}}, the median rent is ${{STATE_MEDIAN_RENT}}"Becomes:"In Oklahoma, the median rent is $1,200"Layout TypesThe system supports 11 distinct layout patterns used across the curriculum:objectives-expanded - Learning objectivesvocab-container - Terms and definitionscomparison-grid - Side-by-side comparisons (Used heavily in L-50, L-52)scenario-layout - Case studiestakeaway-grid - Key points with iconspaycheck-breakdown - Line-by-line deductions (L-06)balanced-layout - Equal-width columnsactivity-layout - Student exercisescheck-grid - Checkliststhree-column - Information setsbullet-list-full - Simple listsCLI ReferenceOptionDescriptionExample--state=<name>State name (lowercase)--state=oklahoma--chapter=<id>L-chapter ID--chapter=L-03--list-statesList all available states--list-chaptersList all available chapters--validate <file>Validate content JSON file--validate slide-content/L-03.jsonProject Roadmap & StatusCompleted ✓[x] Master HTML template with CSS design system[x] Generator script with CLI interface[x] All 71 Chapters (L-01 to L-71) content generated[x] Combined Chapters (Gambling/Philanthropy) standardized and migrated[x] State Data Layer documented (DATA_DICTIONARY.md)[x] Localization Inventory completed (LOCALIZATION_MASTER_MAP.md)LicenseCopyright 2025 PFL Academy. All rights reserved.Status: Production Ready

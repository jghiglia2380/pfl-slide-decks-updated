# PFL Academy: Localization Master Map

**Inventory of Chapters Using Dynamic State Variables (L-01 to L-71)**

**Version:** 1.0
**Last Updated:** December 2024
**Purpose:** Comprehensive reference for all hyper-localized content across the PFL Academy curriculum

---

## Overview

This document maps all chapters utilizing state-specific and local data variables to provide contextually relevant financial education. The PFL Academy curriculum leverages **26 localized chapters** with **100+ variable instances** across 71 total chapters.

### Localization Strategy

**Deep Localization (7 chapters):** Heavy data usage with 6+ state variables, creating immersive local context
**Strategic Context (19 chapters):** Targeted data points (1-5 variables) for specific scenarios and comparisons

---

## Table 1: Deep Localization (Heavy Data Usage)

These chapters use extensive state-specific data to create highly localized learning experiences.

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-46** | Automobile Finance | **16 vars** | Gas Tax, Auto Insurance Rates, Vehicle Registration Fees, Sales Tax, Loan Rates, State Incentives |
| **L-59** | Understanding Local Tax Structures | **15 vars** | Property Tax Assessment, Millage Rates, Local Sales Tax, School Levies, Tax Exemptions, Municipal Bonds |
| **L-50** | Supply and Demand | **11 vars** | Median Rent, Median Home Price, Housing Inventory, Unemployment Rate, Population, Job Growth, Rent Control Context |
| **L-30** | Rent vs Own Housing Decisions | **9 vars** | Home Prices, Median Rent, Mortgage Rates, Property Tax, Cost Comparison, Renter Protection Laws |
| **L-58** | Supply, Demand & Market Structures | **8 vars** | Home Prices, Median Income, Median Rent, Unemployment Rate, Housing Market Analysis |
| **L-06** | Understanding Federal and State Taxes | **6 vars** | Income Tax Bracket, Sales Tax, Property Tax, Gas Tax, State Code, Comparison Grids (Federal vs State) |
| **L-68** | Tax-Efficient Investing Strategies | **6 vars** | Capital Gains Tax, State Income Tax, Tax-Advantaged Accounts, Tax Loss Harvesting, State-Specific Strategies |

**Subtotal: 7 chapters | 71 variable instances**

---

## Table 2: Strategic Context (Specific Data Points)

These chapters use targeted state variables for specific scenarios, comparisons, and contextual relevance.

### Education & Career (4 chapters)

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-02** | Paying for Post-Secondary Education | **4 vars** | State Grant Programs, Public University Tuition, Community College Costs, State Financial Aid |
| **L-25** | Understanding Student Loans | **2 vars** | State-Sponsored Loan Programs, In-State Tuition Comparison |
| **L-45** | Entrepreneurship & Side Hustles | **1 var** | State Name (Local Business Context, Licensing, Opportunity Recognition) |
| **L-57** | Loan Applications & Creditworthiness | **4 vars** | State Loan Rates, Credit Requirements, Regional Lending Practices |

### Income, Tax & Consumer Law (4 chapters)

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-03** | Income and Taxes | **4 vars** | State Income Tax, Local Income Tax, SDI Rate, Paycheck Analysis |
| **L-07** | Understanding Tax Brackets & Rates | **2 vars** | State Tax Brackets, Marginal Rate Comparison |
| **L-61** | Contract Evaluation & Consumer Protection | **2 vars** | State Consumer Protection Agency, State-Specific Laws |
| **L-54** | Inflation & Unemployment | **3 vars** | State Unemployment Rate, Regional Inflation, Cost of Living |

### Housing & Living Costs (3 chapters)

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-05** | Managing Your Income Effectively | **3 vars** | Median Income, Median Rent, 50/30/20 Budget Localization |
| **L-31** | Rental Costs & Responsibilities | **3 vars** | Median Rent, Rental Market Trends, Tenant Rights |
| **L-32** | Understanding Homeownership | **3 vars** | Median Home Price, Property Tax, Housing Costs |

### Insurance & Risk Management (3 chapters)

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-33** | Risk Management & Insurance | **1 var** | Auto Insurance State Requirements |
| **L-34** | Insurance as Risk Management Tool | **3 vars** | Auto Insurance Rates, Health Insurance Marketplace, State Mandates |
| **L-35** | Managing Insurance Costs | **1 var** | Auto Insurance Cost Comparison |

### Economy & Markets (2 chapters)

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-51** | Market Structures & Consumer Choice | **1 var** | State Name (Local Market Examples, Monopoly/Competition Context) |
| **L-52** | Government and the Economy | **2 vars** | State Minimum Wage, Price Floor Comparison (Federal vs State) |

### Banking & Community Context (3 chapters)

| Chapter | Title | Var Count | Key Variables & Use Cases |
|---------|-------|-----------|---------------------------|
| **L-13** | Understanding & Using Banking Tools | **2 vars** | State-Specific Banking Regulations, Overdraft Fee Averages |
| **L-20** | Retirement Longevity Planning | **1 var** | Cost of Living in Retirement |
| **L-37** | Gambling Costs & Benefits | **1 var** | Community Impact, Local Gambling Laws |
| **L-39** | Charitable Giving & Financial Planning | **1 var** | Community Organizations, Local Nonprofits |

**Subtotal: 19 chapters | 41+ variable instances**

---

## Summary Statistics

### By the Numbers

- **Total Localized Chapters:** 26 out of 71 (37%)
- **Total Variable Instances:** 112+ across all chapters
- **Unique State Variables:** 17 distinct variables
- **Deep Localization Chapters:** 7 (6+ variables each)
- **Strategic Context Chapters:** 19 (1-5 variables each)

### Variable Distribution

| Variable Type | Count | Primary Use Cases |
|---------------|-------|-------------------|
| Housing & Cost of Living | 6 vars | Rent, Home Prices, Income, Inventory |
| Tax Variables | 6 vars | Income Tax, Sales Tax, Property Tax, Gas Tax |
| Labor Market | 5 vars | Min Wage, Unemployment, Job Growth, Population |
| Identity & Context | 2 vars | State Name, State Code |
| Specialized | 4 vars | Insurance, Education, Consumer Protection |

### Coverage by Standard

| PFL Standard | Localized Chapters | % of Standard |
|--------------|-------------------|---------------|
| **Income & Employment** | 6 chapters | 40% |
| **Saving & Investing** | 4 chapters | 35% |
| **Credit & Debt** | 3 chapters | 25% |
| **Risk Management** | 3 chapters | 60% |
| **Financial Decision Making** | 10 chapters | 50% |

---

## Implementation Notes

### Variable Update Frequencies

**Quarterly Updates (Housing):**
- Median Rent, Median Home Price, Housing Inventory
- **Data Sources:** Zillow, Redfin, Census Bureau

**Annual Updates (Tax & Economic):**
- All Tax Rates, Minimum Wage, Median Income, Population
- **Data Sources:** Tax Foundation, BLS, Census Bureau

**Monthly Updates (Labor):**
- Unemployment Rate
- **Data Source:** Bureau of Labor Statistics (first Friday release)

### Fallback Strategy

All variables fallback to **National Averages** when state-specific data is unavailable:
- Displays: "National Average" label
- Maintains instructional integrity
- Logs missing data for administrative review

---

## Notable Implementations

### Comparison Grids (Visual Localization)

Five chapters use visual comparison-grid layouts to highlight state differences:

1. **L-06 Slide 8:** Federal Average (14% income tax) vs. In {{STATE_NAME}}
2. **L-05 Slide 7:** National Average ($1,200 rent) vs. In {{STATE_NAME}} (${{STATE_MEDIAN_RENT}})
3. **L-50 Slide 11:** Economic Concept (Price Ceilings) vs. Real World Context (${{STATE_MEDIAN_RENT}})
4. **L-52 Slide 16:** Federal Minimum ($7.25/hr) vs. In {{STATE_NAME}} (${{STATE_MIN_WAGE}}/hr)

### Contextual Hooks (Narrative Localization)

Three chapters inject {{STATE_NAME}} into opening scenarios:
- **L-45 Slide 2:** "Jordan, a CS major in {{STATE_NAME}}..."
- **L-51 Slide 2:** "Eliana, a consumer in {{STATE_NAME}}..."
- **L-58 Slide 2:** Housing market analysis specific to {{STATE_NAME}}

---

## Quality Assurance Checklist

### Data Validation
- ✅ All 26 chapters have `hasStateVariables: true` in metadata
- ✅ All variables documented in DATA_DICTIONARY.md
- ✅ Fallback values defined for all variables
- ✅ Update schedules established (quarterly/annual/monthly)

### Content Alignment
- ✅ Slide decks align with Student Activity Packet workbooks
- ✅ Day 1 (slides) and Day 2 (workbooks) use consistent data
- ✅ Teacher guides reference state variables in instructor notes
- ✅ All comparison grids use leftPanel/rightPanel structure

### Testing Requirements
- [ ] Verify variable substitution ({{STATE_NAME}} → "California")
- [ ] Test fallback behavior with missing state data
- [ ] Validate numeric formatting (currency, percentages, decimals)
- [ ] Confirm all 50 states + DC have complete data records
- [ ] Cross-reference with authoritative data sources

---

## Future Expansion Opportunities

### High-Priority Candidates for Localization

Based on workbook audit, these chapters mention local context but don't yet have state variables:

1. **L-04:** Financial Goal Setting (could use STATE_MEDIAN_INCOME for realistic goals)
2. **L-21:** Understanding Cost of Borrowing (could use STATE_AVG_INTEREST_RATES)
3. **L-24:** Consumer Credit Legislation (could use STATE_CONSUMER_PROTECTION_LAWS)
4. **L-29:** Identity Theft Prevention (could use STATE_REPORTING_REQUIREMENTS)

### Emerging Data Points

Consider adding these variables in future iterations:
- `STATE_AVG_STUDENT_DEBT`
- `STATE_HOUSING_AFFORDABILITY_INDEX`
- `STATE_COLLEGE_SAVINGS_PLAN` (529 plan details)
- `STATE_ENTREPRENEUR_TAX_INCENTIVES`
- `STATE_CONSUMER_PROTECTION_HOTLINE`

---

## Maintenance & Updates

### Quarterly Review (Every 3 Months)

1. Update housing market data (Rent, Home Prices, Inventory)
2. Verify fallback values remain reasonable
3. Check for new state legislation affecting variables
4. Update LOCALIZATION_MASTER_MAP.md with any new chapters

### Annual Review (Every January)

1. Update all tax-related variables
2. Update minimum wage, income, population data
3. Review and update data sources
4. Conduct full QA testing across all 26 chapters
5. Update DATA_DICTIONARY.md version number

### Ad-Hoc Updates

- Monthly: Unemployment rate (first Friday BLS release)
- As needed: Respond to major policy changes (e.g., new tax legislation)
- User feedback: Address data accuracy issues reported by educators

---

## Contact & Resources

**Engineering Team:** Sebastian & Danik
**Content Team:** Curriculum Design & Localization

**Related Documentation:**
- `DATA_DICTIONARY.md` - Technical variable specifications
- `WORKBOOK_DATA_AUDIT.md` - Workbook localization analysis
- `REMEDIATION_WORKFLOW.md` - Quality assurance processes

**Data Sources:**
- Bureau of Labor Statistics: https://www.bls.gov
- U.S. Census Bureau: https://www.census.gov
- Tax Foundation: https://taxfoundation.org
- Zillow Research: https://www.zillow.com/research/data

---

## Appendix: Full Variable List

### All 17 Unique State Variables

1. **STATE_NAME** - Used in 26 chapters
2. **STATE_CODE** - Used in 1 chapter
3. **STATE_MEDIAN_RENT** - Used in 5 chapters
4. **STATE_MEDIAN_HOME_PRICE** - Used in 4 chapters
5. **STATE_MEDIAN_INCOME** - Used in 3 chapters
6. **STATE_INCOME_TAX_RATE** - Used in 4 chapters
7. **STATE_SALES_TAX** - Used in 3 chapters
8. **STATE_PROPERTY_TAX_AVG** - Used in 3 chapters
9. **STATE_GAS_TAX** - Used in 2 chapters
10. **STATE_MIN_WAGE** - Used in 1 chapter
11. **STATE_UNEMPLOYMENT_RATE** - Used in 3 chapters
12. **STATE_POPULATION** - Used in 1 chapter
13. **STATE_JOB_GROWTH** - Used in 1 chapter
14. **STATE_HOUSING_INVENTORY** - Used in 1 chapter
15. **MEDIAN_RENT** (legacy) - Used in 1 chapter
16. **MEDIAN_HOME_PRICE** (legacy) - Used in 1 chapter
17. **UNEMPLOYMENT_RATE** (legacy) - Used in 1 chapter

---

**End of Localization Master Map**

*For technical implementation details, see DATA_DICTIONARY.md*
*For workbook alignment analysis, see WORKBOOK_DATA_AUDIT.md*

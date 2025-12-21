# PFL Academy - Data Dictionary
## Dynamic State Variables for Hyper-Localized Content

**Version:** 1.0
**Last Updated:** December 2024
**For:** Engineering Team (Sebastian & Danik)

---

## Overview

This document defines all dynamic state/local variables used across PFL Academy slide decks to provide hyper-localized, contextually relevant financial education. These variables replace static national averages with real-time state-specific data.

### Chapters Using State Variables
- **L-05:** Managing Your Income Effectively
- **L-06:** Understanding Federal and State Taxes
- **L-45:** Entrepreneurship & Side Hustles
- **L-50:** Supply and Demand
- **L-51:** Market Structures and Consumer Choice
- **L-52:** Government and the Economy

---

## Variable Definitions

### Core Identity Variables

| Variable | Description | Example | Update Frequency | Fallback |
|----------|-------------|---------|------------------|----------|
| `STATE_NAME` | Full state name | "California" | Static | "your state" |
| `STATE_CODE` | Two-letter postal code | "CA" | Static | "XX" |

### Housing & Cost of Living

| Variable | Description | Example | Update Frequency | Fallback |
|----------|-------------|---------|------------------|----------|
| `STATE_MEDIAN_RENT` | Median monthly rent (1BR) | 1850 | **Quarterly** | 1200 (national avg) |
| `MEDIAN_RENT` | Alias for STATE_MEDIAN_RENT | 1850 | **Quarterly** | 1200 (national avg) |
| `STATE_MEDIAN_HOME_PRICE` | Median home sale price | 450000 | **Quarterly** | 350000 (national avg) |
| `MEDIAN_HOME_PRICE` | Alias for STATE_MEDIAN_HOME_PRICE | 450000 | **Quarterly** | 350000 (national avg) |
| `STATE_MEDIAN_INCOME` | Median household income (annual) | 75000 | **Annually** | 70000 (national avg) |
| `STATE_HOUSING_INVENTORY` | Available housing units | 125000 | **Quarterly** | "varies by region" |

### Tax Variables

| Variable | Description | Example | Update Frequency | Fallback |
|----------|-------------|---------|------------------|----------|
| `STATE_INCOME_TAX_RATE` | Top marginal income tax rate (%) | 9.3 | **Annually** (Jan 1) | 5.0 (national avg) |
| `STATE_SALES_TAX` | Combined state sales tax rate (%) | 7.25 | **Annually** (Jan 1) | 6.5 (national avg) |
| `STATE_PROPERTY_TAX_AVG` | Effective property tax rate (%) | 0.74 | **Annually** (Jan 1) | 1.07 (national avg) |
| `STATE_GAS_TAX` | State gasoline excise tax ($/gallon) | 0.539 | **Annually** (Jul 1) | 0.30 (national avg) |

### Labor Market

| Variable | Description | Example | Update Frequency | Fallback |
|----------|-------------|---------|------------------|----------|
| `STATE_MIN_WAGE` | State minimum wage ($/hour) | 15.50 | **Annually** (Jan 1) | 7.25 (federal min) |
| `STATE_UNEMPLOYMENT_RATE` | Current unemployment rate (%) | 4.2 | **Monthly** | 3.8 (national avg) |
| `UNEMPLOYMENT_RATE` | Alias for STATE_UNEMPLOYMENT_RATE | 4.2 | **Monthly** | 3.8 (national avg) |
| `STATE_JOB_GROWTH` | YoY job growth rate (%) | 2.1 | **Annually** | 1.5 (national avg) |
| `STATE_POPULATION` | Current population estimate | 39500000 | **Annually** (Jul 1) | "varies by state" |

---

## Data Sources

### Recommended Sources (Priority Order)

1. **U.S. Bureau of Labor Statistics (BLS)**
   - Unemployment rates (monthly updates)
   - Job growth statistics (annual)
   - Minimum wage tracking

2. **U.S. Census Bureau**
   - Median household income (annual - American Community Survey)
   - Population estimates (annual - July 1 release)

3. **Zillow Research / Redfin Data Center**
   - Median home prices (monthly/quarterly)
   - Median rent (monthly/quarterly)
   - Housing inventory data

4. **Tax Foundation**
   - State income tax rates (annual)
   - State sales tax rates (annual)
   - Property tax effective rates (annual)

5. **State Department of Revenue / Taxation Agencies**
   - Gas tax rates (varies by state, often July 1)
   - Local tax adjustments

---

## Update Schedule

### Quarterly Updates (Housing Market)
**Timeline:** January 15, April 15, July 15, October 15

- `STATE_MEDIAN_RENT` / `MEDIAN_RENT`
- `STATE_MEDIAN_HOME_PRICE` / `MEDIAN_HOME_PRICE`
- `STATE_HOUSING_INVENTORY`

**Data Lag:** Use prior quarter data (e.g., Q4 2024 data released Jan 15, 2025)

### Annual Updates (Tax & Income)
**Timeline:** January 1 (for tax year)

- `STATE_INCOME_TAX_RATE`
- `STATE_SALES_TAX`
- `STATE_PROPERTY_TAX_AVG`
- `STATE_MIN_WAGE`
- `STATE_MEDIAN_INCOME`
- `STATE_JOB_GROWTH`
- `STATE_POPULATION`

**Note:** Gas tax (`STATE_GAS_TAX`) typically updates July 1

### Monthly Updates (Labor Market)
**Timeline:** First Friday of each month (BLS release)

- `STATE_UNEMPLOYMENT_RATE` / `UNEMPLOYMENT_RATE`

---

## Fallback Strategy

### Missing Data Protocol

When state-specific data is unavailable or fails to load:

```javascript
// Pseudocode example
const getStateVariable = (varName, stateCode) => {
  const value = fetchFromDatabase(varName, stateCode);

  if (!value || value === null) {
    // Fallback to national average
    return FALLBACK_VALUES[varName];
  }

  return value;
};

const FALLBACK_VALUES = {
  STATE_MEDIAN_RENT: 1200,
  STATE_MEDIAN_HOME_PRICE: 350000,
  STATE_MEDIAN_INCOME: 70000,
  STATE_INCOME_TAX_RATE: 5.0,
  STATE_SALES_TAX: 6.5,
  STATE_PROPERTY_TAX_AVG: 1.07,
  STATE_GAS_TAX: 0.30,
  STATE_MIN_WAGE: 7.25,
  STATE_UNEMPLOYMENT_RATE: 3.8,
  // ... etc
};
```

### Display Strategy

- **Always show the variable name** in instructor notes for transparency
- **Display "National Average" label** when fallback is used
- **Log missing data** for administrative review

Example:
```
Slide displays: "Median Rent: $1,200/mo (National Average)"
Instead of: "Median Rent: ${{STATE_MEDIAN_RENT}}/mo"
```

---

## Implementation Notes

### Database Schema Suggestion

```sql
CREATE TABLE state_data (
  state_code VARCHAR(2) PRIMARY KEY,
  state_name VARCHAR(50) NOT NULL,
  median_rent DECIMAL(10,2),
  median_home_price DECIMAL(10,2),
  median_income DECIMAL(10,2),
  income_tax_rate DECIMAL(5,2),
  sales_tax DECIMAL(5,2),
  property_tax_avg DECIMAL(5,3),
  gas_tax DECIMAL(5,3),
  min_wage DECIMAL(5,2),
  unemployment_rate DECIMAL(4,2),
  job_growth DECIMAL(4,2),
  population BIGINT,
  housing_inventory INT,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  data_source VARCHAR(100)
);
```

### Variable Naming Convention

- **Prefix:** `STATE_` for state-specific variables
- **Format:** SCREAMING_SNAKE_CASE
- **Consistency:** Some legacy variables (e.g., `MEDIAN_RENT`) exist without `STATE_` prefix—maintain both for backward compatibility

### Precision & Formatting

| Variable Type | Decimal Places | Display Format |
|---------------|----------------|----------------|
| Currency (rent, income, home price) | 0 | $1,850 (no cents) |
| Percentages (tax rates, unemployment) | 1-2 | 9.3% or 4.25% |
| Counts (population, inventory) | 0 | 39,500,000 (with commas) |

---

## Quality Assurance

### Data Validation Rules

1. **Range Checks:**
   - Rent: $400 - $5,000
   - Home Price: $50,000 - $2,000,000
   - Tax Rates: 0% - 15%
   - Min Wage: $7.25 - $20.00

2. **Logical Consistency:**
   - `STATE_MIN_WAGE` ≥ 7.25 (federal minimum)
   - `STATE_MEDIAN_RENT` < `STATE_MEDIAN_INCOME` / 2 (sanity check)

3. **Freshness Checks:**
   - Flag data older than update frequency + 30 days
   - Auto-revert to fallback if data is stale

### Testing Checklist

- [ ] Verify all 50 states + DC have complete records
- [ ] Test fallback behavior with missing data
- [ ] Validate numeric formatting (commas, decimals, currency symbols)
- [ ] Confirm template variable substitution (e.g., `{{STATE_NAME}}` → "California")
- [ ] Cross-reference with authoritative sources quarterly

---

## Maintenance Log

| Date | Update | Author | Notes |
|------|--------|--------|-------|
| Dec 2024 | Initial creation | Claude | Documented L-05, L-06, L-50, L-52 variables |
| | | | Added L-45, L-51 state name localization |

---

## Contact

For questions about data sources, update schedules, or implementation:
- **Sebastian & Danik** (Engineering Team)
- **Content Team:** Curriculum updates requiring new variables

---

**Next Steps:**
1. Implement database schema
2. Set up automated data ingestion pipelines (quarterly/annual)
3. Create admin dashboard for manual data verification
4. Build fallback monitoring and alerting system

# PFL Academy - Data Dictionary
## Dynamic State Variables for Hyper-Localized Content

**Version:** 2.0 (Final Complete)
**Last Updated:** December 21, 2025
**For:** Engineering Team (Sebastian & Danik)

---

## Overview

This document defines the **complete variable data layer** used across the PFL Academy slide decks. These variables replace static national averages with real-time state-specific data to ensure the curriculum is hyper-localized.

**CRITICAL:** This data feeds not just the "Big 6" chapters, but **26 total chapters**, including Auto Finance (L-46) and Education (L-02).

### Key Chapters Using State Variables
* **Housing:** L-05, L-30, L-31, L-32, L-50, L-59
* **Taxes:** L-06, L-59, L-68
* **Auto:** L-46 (16 variables)
* **Economy:** L-45, L-51, L-52, L-54, L-58
* **Education:** L-02, L-25

---

## Variable Definitions

### 1. Core Identity

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_NAME` | Full state name | "California" | Static | "your state" |
| `STATE_CODE` | Two-letter postal code | "CA" | Static | "XX" |

### 2. Housing & Cost of Living (L-05, L-30, L-50)

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_MEDIAN_RENT` | Median monthly rent (1BR) | 1850 | **Quarterly** | 1200 |
| `STATE_MEDIAN_HOME_PRICE` | Median home sale price | 450000 | **Quarterly** | 350000 |
| `STATE_AVG_MORTGAGE_RATE` | Avg 30-year fixed rate | 6.8 | **Monthly** | 7.0 |
| `STATE_HOUSING_INVENTORY` | Available housing units | 125000 | **Quarterly** | "varies" |
| `STATE_MEDIAN_INCOME` | Median household income | 75000 | **Annually** | 70000 |

### 3. Taxes (L-06, L-59, L-68)

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_INCOME_TAX_RATE` | Top marginal income tax rate (%) | 9.3 | **Annually** | 5.0 |
| `STATE_SALES_TAX` | Combined state sales tax rate (%) | 7.25 | **Annually** | 6.5 |
| `STATE_PROPERTY_TAX_AVG` | Effective property tax rate (%) | 0.74 | **Annually** | 1.07 |
| `STATE_GAS_TAX` | State gasoline excise tax ($/gal) | 0.539 | **Annually** | 0.30 |
| `STATE_HOMESTEAD_EXEMPTION` | Property tax exemption amount | 7000 | **Annually** | 0 |
| `STATE_ASSESSMENT_PERCENTAGE`| % of home value taxed | 100 | **Static** | 100 |
| `STATE_CAPITAL_GAINS_TAX` | Cap gains tax rate (%) | 9.3 | **Annually** | 5.0 |

### 4. Automotive & Transportation (L-46)

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_GAS_PRICE` | Current avg gas price ($/gal) | 4.85 | **Monthly** | 3.50 |
| `STATE_INSURANCE_AVG_TEEN` | Avg annual premium (Teen Driver) | 4200 | **Annually** | 3500 |
| `STATE_INSURANCE_AVG_ADULT`| Avg annual premium (Adult) | 1800 | **Annually** | 1500 |
| `STATE_REGISTRATION_INITIAL`| Initial vehicle reg/title fees | 350 | **Annually** | 200 |
| `STATE_REGISTRATION_ANNUAL`| Annual renewal fee | 150 | **Annually** | 75 |
| `STATE_AVG_AUTO_LOAN_RATE_NEW`| Avg APR (New Car) | 6.5 | **Monthly** | 6.0 |
| `STATE_AVG_AUTO_LOAN_RATE_USED`| Avg APR (Used Car) | 10.5 | **Monthly** | 10.0 |

### 5. Education (L-02, L-25)

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_TUITION_PUBLIC` | Avg In-State Tuition (Public 4yr) | 11000 | **Annually** | 10500 |
| `STATE_TUITION_COMMUNITY`| Avg Community College Tuition | 3500 | **Annually** | 3800 |
| `STATE_GRANT_PROGRAM` | Name of state aid program | "Cal Grant"| **Static** | "State Grant"|

### 6. Labor & Economy (L-52, L-54)

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_MIN_WAGE` | State minimum wage ($/hr) | 15.50 | **Annually** | 7.25 |
| `STATE_UNEMPLOYMENT_RATE` | Current unemployment rate (%) | 4.2 | **Monthly** | 3.8 |
| `STATE_JOB_GROWTH` | YoY job growth rate (%) | 2.1 | **Annually** | 1.5 |

### 7. Niche Context (L-13, L-61)

| Variable | Description | Example | Update Freq | Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `STATE_CONSUMER_PROTECTION_AGENCY` | Agency Name | "Dept of Consumer Affairs" | **Static** | "Consumer Protection" |
| `STATE_AVG_OVERDRAFT_FEE`| Avg bank overdraft fee | 35.00 | **Annually** | 35.00 |

---

## Data Sources

### Recommended Sources (Priority Order)
1.  **BLS (Bureau of Labor Statistics):** Unemployment, Wages, Job Growth.
2.  **Census Bureau:** Income, Population.
3.  **Zillow/Redfin:** Home Prices, Rents, Inventory.
4.  **AAA / Bankrate:** Gas Prices, Mortgage Rates, Auto Loan Rates.
5.  **Tax Foundation:** All Tax Rates.
6.  **College Board:** Tuition trends.

---

## Fallback Strategy

**CRITICAL FOR DEV TEAM:**
If a specific state data point returns `NULL` or fails to fetch:
1.  **DO NOT** leave the slide blank.
2.  **DO NOT** return an error string like `{{ERROR}}`.
3.  **MUST** fallback to the **National Average** defined in the tables above.
4.  *Optional:* Append "(National Avg)" to the display string for transparency.

---

## Database Implementation Notes

### Suggested Table Schema
```sql
CREATE TABLE state_variables (
  state_code VARCHAR(2) PRIMARY KEY,
  median_rent INT,
  median_home_price INT,
  avg_mortgage_rate DECIMAL(4,2),
  income_tax_rate DECIMAL(4,2),
  sales_tax_rate DECIMAL(4,2),
  property_tax_rate DECIMAL(4,3),
  gas_price DECIMAL(4,2),
  min_wage DECIMAL(4,2),
  tuition_public INT,
  tuition_community INT,
  insurance_teen INT,
  -- Add all other fields mapped above
  last_updated TIMESTAMP
);

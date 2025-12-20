#!/usr/bin/env python3
import json
import sys

def update_l15():
    # Read the JSON file
    with open('slide-content/L-15.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update Slide 2
    for slide in data['slides']:
        if slide['number'] == 2:
            slide['content']['question'] = "Micah wants to show his younger brother that $100 invested at 8% annual return can grow to $800 without adding more money. His brother is skeptical about this 'magic' of compound interest. <br><br> How does compound interest turn $100 into $800, and how can you calculate how long this transformation takes?"
            slide['notes'] = "THE CHALLENGE (5 min):\n• Read Micah's scenario. Ask: 'Is it really possible for $100 to become $800?'\n• Explain that today's lesson reveals the 'magic' (actually math!).\n• Preview the Rule of 72 as a quick mental math tool."

        # Update Slide 11 - add Common Misconceptions
        elif slide['number'] == 11:
            slide['notes'] = "COMMON MISCONCEPTIONS:\n\n1. \"The Rule of 72 is exact.\"\n   → It's an approximation. The actual formula is more complex. Rule of 72 is close enough for quick mental math and planning purposes.\n\n2. \"I need to start with a lot of money for compounding to matter.\"\n   → Time matters more than starting amount. $100/month for 40 years at 7% grows to ~$264,000. The key is starting early.\n\n3. \"Past returns guarantee future returns.\"\n   → Historical averages help with planning, but actual returns vary year to year. Diversification and long time horizons help manage this uncertainty."

        # Update Slide 17 - add Assessment Answer Key
        elif slide['number'] == 17:
            slide['notes'] = "ANSWER KEY:\n\n1. What makes compound interest more powerful than simple interest?\n   → You earn interest on your interest, not just the principal. Time is the most important factor in compounding. More time = more doubling periods = exponentially more money. Starting 10 years earlier can be worth more than doubling your contributions.\n\n2. Using the Rule of 72, how long will it take $5,000 to double at 9% interest?\n   → 72 ÷ 9 = 8 years to double. After two doublings: $5,000 → $10,000 → $20,000\n\n3. Why does starting to invest at 22 vs. 32 make such a huge difference, even with less total money invested?\n   → Time is the most important factor in compounding. More time = more doubling periods = exponentially more money. Starting 10 years earlier can be worth more than doubling your contributions.\n\n4. $1,000 at 5% simple interest for 30 years = $2,500. Compound interest = $4,322. How much more does compounding earn?\n   → 72 ÷ 3 = 24 years (This shows why higher rates matter for shorter goals)"

    # Write back to file
    with open('slide-content/L-15.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("L-15.json updated successfully!")

if __name__ == '__main__':
    update_l15()

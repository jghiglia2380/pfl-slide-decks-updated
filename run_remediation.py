import os
import json
import re
import shutil

# --- CONFIGURATION ---
ROOT_DIR = "."
# The specific corruption pattern found in your previous audits
# Matches " in {{STATE_NAME}}" appearing at the end of titles/labels
CORRUPTION_REGEX = re.compile(r'\s+in\s+\{\{STATE_NAME\}\}\s*$', re.IGNORECASE)

# Golden Template v3.0 Mappings
COLOR_MAP = {
    "teal": "indigo", 
    "purple": "indigo", 
    "blue": "amber"
}

SECTION_FIXES = {
    # Terminology fixes
    "Essential Question": "The Challenge",
    "Hook": "The Challenge",
    "Key Terms": "Core Concepts",
    "Vocabulary": "Core Concepts",
    "Check for Understanding": "Check Your Understanding",
    "Assessment": "Check Your Understanding",
    "Activity Preview": "Tomorrow's Challenge",
    "Day 2 Preview": "Tomorrow's Challenge",
}

def clean_text(text):
    """Surgically removes the specific corruption pattern."""
    if isinstance(text, str):
        return CORRUPTION_REGEX.sub("", text)
    return text

def recursive_clean(obj):
    """Walks the JSON tree to clean strings."""
    if isinstance(obj, dict):
        return {k: recursive_clean(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [recursive_clean(i) for i in obj]
    elif isinstance(obj, str):
        return clean_text(obj)
    return obj

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return "❌ INVALID JSON"

    # Validation: Is this a slide deck?
    if "slides" not in data or not isinstance(data["slides"], list):
        return "⏭️  SKIPPED (Not a slide deck)"
    
    # Audit: Check Slide Count
    slide_count = len(data["slides"])
    if slide_count < 19:
        return f"⚠️  NEEDS ATTENTION (Only {slide_count} slides)"

    modified = False
    
    # 1. Clean Corruption (Recursive)
    clean_data = recursive_clean(data)
    if clean_data != data:
        data = clean_data
        modified = True

    # 2. Apply Golden Template Rules
    for i, slide in enumerate(data["slides"]):
        # Fix Terminology (Labels & Titles)
        if "content" in slide:
            # Fix Label (e.g., Slide 2)
            if "label" in slide["content"]:
                curr_label = slide["content"]["label"]
                if curr_label in SECTION_FIXES:
                    slide["content"]["label"] = SECTION_FIXES[curr_label]
                    modified = True
            
            # Fix Header Title (e.g., Core Concepts)
            if "headerTitle" in slide["content"]:
                curr_title = slide["content"]["headerTitle"]
                if curr_title in SECTION_FIXES:
                    slide["content"]["headerTitle"] = SECTION_FIXES[curr_title]
                    modified = True

        # Fix Colors (Context Aware)
        # Force Slide 2 (Challenge) to Amber
        if i == 1: 
            if slide.get("headerColor") != "amber":
                slide["headerColor"] = "amber"
                modified = True
        
        # Force Slide 17 (Assessment) to Emerald
        elif i == 16:
            if slide.get("headerColor") != "emerald":
                slide["headerColor"] = "emerald"
                modified = True

        # Apply General Map
        elif slide.get("headerColor") in COLOR_MAP:
            slide["headerColor"] = COLOR_MAP[slide.get("headerColor")]
            modified = True

    # 3. Save
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return "✅ FIXED"
    return "✨ ALREADY CLEAN"

def main():
    print("--- STARTING REMEDIATION ---")
    results = {"✅ FIXED": 0, "✨ ALREADY CLEAN": 0, "⚠️  NEEDS ATTENTION (Only {slide_count} slides)": 0}
    
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.startswith("L-") and file.endswith(".json"):
                path = os.path.join(root, file)
                status = process_file(path)
                
                # Group structural failures in output
                if "NEEDS ATTENTION" in status:
                    print(f"{file}: {status}")
                elif "FIXED" in status:
                    # Optional: Print fixed files if you want to see progress
                    pass 
                
    print("\n--- DONE. RUN 'git diff' TO SEE CHANGES. ---")

if __name__ == "__main__":
    main()
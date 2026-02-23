import json
from pathlib import Path
from nlp_utils import extract_keywords

BASE_DIR = Path(__file__).parent
SKILLS_PATH = BASE_DIR / "skills.json"


def load_skills():
    with open(SKILLS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def match_job_description(jd_text):
    skills = load_skills()
    jd_keywords = extract_keywords(jd_text)

    all_skills = {
        "technical": [s.lower() for s in skills["technical_skills"]],
        "soft": [s.lower() for s in skills["soft_skills"]],
    }

    matched_technical = [s for s in all_skills["technical"] if s in jd_keywords]
    matched_soft = [s for s in all_skills["soft"] if s in jd_keywords]

    total_possible = len(all_skills["technical"]) + len(all_skills["soft"])
    total_matched = len(matched_technical) + len(matched_soft)
    match_percent = round((total_matched / total_possible) * 100, 1) if total_possible else 0

    missing_technical = [s for s in all_skills["technical"] if s not in matched_technical]
    missing_soft = [s for s in all_skills["soft"] if s not in matched_soft]

    return {
        "match_percent": match_percent,
        "matched_technical": matched_technical,
        "matched_soft": matched_soft,
        "missing_technical": missing_technical,
        "missing_soft": missing_soft,
    }


def main():
    print("Paste the job description below. End with a blank line:")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    jd_text = "\n".join(lines)
    result = match_job_description(jd_text)

    print("\n=== Match Report ===")
    print(f"Overall match: {result['match_percent']}%")
    print("\nMatched technical skills:", ", ".join(result["matched_technical"]) or "None")
    print("Matched soft skills:", ", ".join(result["matched_soft"]) or "None")
    print("\nMissing technical skills:", ", ".join(result["missing_technical"]) or "None")
    print("Missing soft skills:", ", ".join(result["missing_soft"]) or "None")


if __name__ == "__main__":
    main()

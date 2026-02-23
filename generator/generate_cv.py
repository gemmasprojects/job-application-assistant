from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATE_PATH = BASE_DIR / "templates" / "cv_template.md"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_cv(skills, role_notes, filename="cv_generated.md"):
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    skills_str = "- " + "\n- ".join(skills) if skills else "See core skills section."
    content = template.replace("{{SKILLS}}", skills_str)
    content = content.replace("{{ROLE_NOTES}}", role_notes or "I am keen to grow into this role.")

    output_path = OUTPUT_DIR / filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"CV generated at: {output_path}")


def main():
    print("Enter skills to highlight (comma-separated):")
    skills_input = input("> ").strip()
    skills = [s.strip() for s in skills_input.split(",") if s.strip()]

    print("\nEnter notes about why you're a good fit for this role:")
    role_notes = input("> ").strip()

    generate_cv(skills, role_notes)


if __name__ == "__main__":
    main()

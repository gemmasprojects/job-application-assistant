from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATE_PATH = BASE_DIR / "templates" / "cover_letter_template.md"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_cover_letter(company_name, job_title, role_reason, skills, filename="cover_letter_generated.md"):
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    skills_str = "- " + "\n- ".join(skills) if skills else "- Strong motivation to learn."
    content = template.replace("{{COMPANY_NAME}}", company_name or "your")
    content = content.replace("{{JOB_TITLE}}", job_title or "role")
    content = content.replace("{{ROLE_REASON}}", role_reason or "it aligns with my skills.")
    content = content.replace("{{SKILLS}}", skills_str)

    output_path = OUTPUT_DIR / filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Cover letter generated at: {output_path}")


def main():
    company = input("Company name: ").strip()
    title = input("Job title: ").strip()
    reason = input("Why does this role appeal to you?: ").strip()
    print("Skills to highlight (comma-separated):")
    skills_input = input("> ").strip()
    skills = [s.strip() for s in skills_input.split(",") if s.strip()]

    generate_cover_letter(company, title, reason, skills)


if __name__ == "__main__":
    main()

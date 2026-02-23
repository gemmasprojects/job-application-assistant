import json
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "database.json"


def load_db():
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_job():
    jobs = load_db()
    print("Add a new job application")
    title = input("Job title: ").strip()
    company = input("Company: ").strip()
    link = input("Job link (URL): ").strip()
    status = "Applied"
    notes = input("Notes (optional): ").strip()
    skills = input("Key skills for this role (comma-separated): ").strip()

    job = {
        "id": len(jobs) + 1,
        "title": title,
        "company": company,
        "link": link,
        "status": status,
        "notes": notes,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "applied_at": datetime.utcnow().isoformat() + "Z",
        "cv_version": None,
    }
    jobs.append(job)
    save_db(jobs)
    print(f"\nSaved job #{job['id']} for {company} - {title}")


def list_jobs():
    jobs = load_db()
    if not jobs:
        print("No jobs saved yet.")
        return
    print("\nYour job applications:\n")
    for job in jobs:
        print(f"[{job['id']}] {job['company']} - {job['title']} ({job['status']})")
        print(f"    Link: {job['link']}")
        if job.get("cv_version"):
            print(f"    CV version: {job['cv_version']}")
        if job.get("notes"):
            print(f"    Notes: {job['notes']}")
        print()


def update_status():
    jobs = load_db()
    if not jobs:
        print("No jobs to update.")
        return
    list_jobs()
    try:
        job_id = int(input("Enter job ID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    job = next((j for j in jobs if j["id"] == job_id), None)
    if not job:
        print("Job not found.")
        return
    print(f"Current status: {job['status']}")
    new_status = input("New status (Applied/Interview/Rejected/Offer): ").strip()
    if new_status:
        job["status"] = new_status
    cv_version = input("CV version used (optional): ").strip()
    if cv_version:
        job["cv_version"] = cv_version
    save_db(jobs)
    print("Job updated.")


def main():
    while True:
        print("\nJob Application Tracker")
        print("1. Add job")
        print("2. List jobs")
        print("3. Update job status")
        print("4. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_job()
        elif choice == "2":
            list_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("Good luck with your applications!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

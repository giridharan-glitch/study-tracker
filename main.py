print("Study Tracker")

study_data = []

def add_session():
    subject = input("Enter subject: ")
    hours = float(input("Enter study hours: "))

    session = {
        "subject": subject,
        "hours": hours
    }

    study_data.append(session)
    print("Session added successfully!")


def view_sessions():
    if not study_data:
        print("No study sessions recorded.")
        return

    print("Study Sessions:")
    for session in study_data:
        print(f"Subject: {session['subject']}, Hours: {session['hours']}")


def total_hours():
    total = sum(session["hours"] for session in study_data)
    print("Total Study Hours:", total)


if __name__ == "__main__":
    add_session()
    add_session()
    view_sessions()
    total_hours()

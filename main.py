print("===== STUDY TRACKER =====")

study_data = []

goal_hours = float(input("Enter your study goal (hours): "))


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

    if len(study_data) == 0:
        print("No study sessions found.")
        return

    print("\n===== STUDY SESSIONS =====")

    for i, session in enumerate(study_data, start=1):
        print(f"{i}. Subject: {session['subject']}, Hours: {session['hours']}")


def total_hours():

    total = 0

    for session in study_data:
        total += session["hours"]

    print("\n===== TOTAL HOURS =====")
    print("Total Study Hours:", total)


def most_studied_subject():

    if len(study_data) == 0:
        print("No study sessions found.")
        return

    top_subject = study_data[0]

    for session in study_data:
        if session["hours"] > top_subject["hours"]:
            top_subject = session

    print("\n===== ANALYTICS =====")
    print("Most Studied Subject:", top_subject["subject"])
    print("Hours:", top_subject["hours"])


def goal_progress():

    completed_hours = 0

    for session in study_data:
        completed_hours += session["hours"]

    progress = (completed_hours / goal_hours) * 100

    print("\n===== GOAL PROGRESS =====")
    print("Goal:", goal_hours, "Hours")
    print("Completed:", completed_hours, "Hours")
    print("Progress:", round(progress, 2), "%")


def xp_dashboard():

    total_hours_studied = 0

    for session in study_data:
        total_hours_studied += session["hours"]

    xp = total_hours_studied * 10

    if xp >= 500:
        level = 4
    elif xp >= 250:
        level = 3
    elif xp >= 100:
        level = 2
    else:
        level = 1

    print("\n===== XP DASHBOARD =====")
    print("Total XP:", xp)
    print("Current Level:", level)

    if level == 1:
        print("Keep studying to reach Level 2!")
    elif level == 2:
        print("Nice progress!")
    elif level == 3:
        print("Advanced learner!")
    else:
        print("Study Master!")


def motivation_message():

    print("\n===== MOTIVATION =====")
    print("Consistency beats intensity.")
    print("Every hour of study compounds over time.")


# ----------------------
# MENU SYSTEM
# ----------------------

while True:

    print("\n===== STUDY TRACKER MENU =====")
    print("1. Add Session")
    print("2. View Sessions")
    print("3. Total Hours")
    print("4. Most Studied Subject")
    print("5. Goal Progress")
    print("6. XP Dashboard")
    print("7. Motivation")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_session()

    elif choice == "2":
        view_sessions()

    elif choice == "3":
        total_hours()

    elif choice == "4":
        most_studied_subject()

    elif choice == "5":
        goal_progress()

    elif choice == "6":
        xp_dashboard()

    elif choice == "7":
        motivation_message()

    elif choice == "8":
        print("Thank you for using Study Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
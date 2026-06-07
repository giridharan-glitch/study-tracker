print("Study Tracker")
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

add_session()

print(study_data)
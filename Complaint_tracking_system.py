complaints = []

def submit_complaint():
    user = input("Enter your name: ")
    complaint = input("Enter complaint: ")
    complaints.append({
        "user": user,
        "complaint": complaint
    })
    print("Complaint submitted")

def view_complaints():
    if not complaints:
        print("No complaints recorded")
    else:
        for c in complaints:
            print("User:", c["user"])
            print("Complaint:", c["complaint"])
            print("----------------")

def main():
    while True:
        print("1. Submit Complaint")
        print("2. View Complaints")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            submit_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()

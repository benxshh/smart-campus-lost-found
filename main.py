from data_manager import save_data, load_data
from matching import find_matches
from statistics import view_statistics
from items import report_lost_item, report_found_item, view_lost_items, view_found_items, search_items

items=[]

users={
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "student1": {"password": "student123", "role": "user"},
    "student2": {"password": "student234", "role": "user"},
    "student3": {"password": "student345", "role": "user"},
    "rayan": {"password": "rayan123", "role": "user"}
}

def update_report(username, role):
    print("\n--- Update Report ---")

    try:
        report_id=int(input("Enter report ID to update: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for item in items:
        if item["id"]==report_id:

            if role!="admin" and item.get("username")!=username:
                print("You can only update your own reports.")
                return
            
            print("\nCurrent Details:")
            print("Item:",item["name"])
            print("Category:",item["category"])
            print("Location:",item["location"])
            print("Description:",item["description"])

            print("\nEnter new details:")

            name=input("Enter item name: ").strip()
            while name=="":
                print("Item name cannot be empty.")
                name=input("Enter item name: ").strip()

            category=input("Enter category: ").strip()
            while category=="":
                print("Category cannot be empty.")
                category=input("Enter category: ").strip()

            location=input("Enter location: ").strip()
            while location=="":
                print("Location cannot be empty.")
                location=input("Enter location : ").strip()

            description=input("Enter description: ").strip()
            while description=="":
                print("Description cannot be empty.")
                description=input("Enter description: ").strip()

            item["name"]=name
            item["category"]=category
            item["location"]=location
            item["description"]=description

            save_data(items)

            print("\nReport updated successfully!")
            return
        
    print("Report ID not found.")

def delete_report(username, role):
    print("\n--- Delete Report---")

    try:
        report_id=int(input("Enter report id to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for item in items:
        if item["id"]==report_id:

            if role!="admin" and item.get("username")!=username:
                print("You can only delete your own reports.")
                return

            print("\nReport found:")
            print("Item:",item["name"])
            print("Type:",item["type"])

            confirm=input("Are you sure you want to delete this report? (yes/no): ").lower()

            if confirm=="yes":
                items.remove(item)
                save_data(items)
                print("Report deleted successfully")
            else:
                print("Deletion cancelled.")

            return
    print("Report ID not found.")

                
def claim_item(username):
    print("\n--- Claim Found Item ---")

    try:
        report_id=int(input("Enter found item report ID:"))
    except ValueError:
        print("Please enter a valid number.")
        return

    for item in items:
        if item["id"]==report_id and item["type"]=="found":

            if item["status"]=="claimed":
                print("This item has already been claimed.")
                return

            if item.get("username")==username:
                print("You cannot claim an item that you reported yourself.")
                return
            

            claimant_name=username

            item["status"]="claimed"
            item["claimed_by"]=claimant_name

            save_data(items)

            print("\nItem claimed successfully!")
            print("Report ID:",item["id"])
            print("Item:",item["name"])
            print("Claimed by:",claimant_name)

            return
        
    print("Found item report not found.")

def login():
    while True:
        print("\n==============================================")
        print("     SMART CAMPUS LOST-AND-FOUND SYSTEM")
        print("==============================================")
        print("              CAMPUS LOGIN")
        print("----------------------------------------------")
        print("Demo User Credentials:")
        print("1. Username: user      | Password: user123")
        print("2. Username: student1  | Password: student123")
        print("3. Username: student2  | Password: student234")
        print("4. Username: student3  | Password: student345")
        print("5. Username: rayan     | Password: rayan123")
        print("Admin: Confidential Credentials")
        print("----------------------------------------------")
        print("Enter 0 as username to exit the program.")

        username = input("Enter username: ")
        
        if username == "0":
            return None, None

        password = input("Enter password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]

            print("\nLogin successful!")
            print("Welcome,", username)

            return username, role

        else:
            print("\nInvalid username or password.")
            print("Please try again.")

def user_menu(username):
    while True:
        print("\n==============================")
        print("         USER MENU")
        print("==============================")
        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. View Lost Items")
        print("4. View Found Items")
        print("5. Search Items")
        print("6. Find Possible Matches")
        print("7. Update Report")
        print("8. Delete Report")
        print("9. Claim Found Item")
        print("10. Logout")

        choice=input("\nEnter your choice: ")

        if choice=="1":
            report_lost_item(items, username)

        elif choice=="2":
            report_found_item(items,username)

        elif choice=="3":
            view_lost_items(items)

        elif choice=="4":
            view_found_items(items)

        elif choice=="5":
            search_items(items)

        elif choice=="6":
            find_matches(items)

        elif choice=="7":
            update_report(username, "user")

        elif choice=="8":
            delete_report(username, "user")

        elif choice=="9":
            claim_item(username)

        elif choice=="10":
            print("\nLogging out...")
            break

        else:
            print("\nInvalid choice. Please try again.")

def admin_menu():
    while True:
        print("\n==============================")
        print("        ADMIN MENU")
        print("==============================")
        print("1. View Lost Items")
        print("2. View Found Items")
        print("3. Search Items")
        print("4. View Statistics")
        print("5. Update Report")
        print("6. Delete Report")
        print("7. Logout")

        choice=input("\nEnter your choice: ")

        if choice=="1":
            view_lost_items(items)

        elif choice=="2":
            view_found_items(items)

        elif choice=="3":
            search_items(items)

        elif choice=="4":
            view_statistics(items)

        elif choice=="5":
            update_report("admin", "admin")

        elif choice=="6":
            delete_report("admin", "admin")

        elif choice=="7":
            print("\nLogging out...")
            break

        else:
            print("\nInvalid choice. Please try again.")

def main(username, role):

    if role=="admin":
        admin_menu()

    elif role=="user":
        user_menu(username)

items=load_data()

while True:

    username, role=login()

    if role is None:
        print("\nProgram ended.")
        break

    main(username,role)

    print("\nYou have been logged out.")




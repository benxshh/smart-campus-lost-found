from data_manager import save_data

def report_lost_item(items,username):

    print("\n--- Report Lost Item ---")

    name=input("Enter item name: ").strip()
    while name=="":
        print("Item name cannot be empty.")
        name=input("Enter item name: ").strip()

    category=input("Enter category: ").strip()
    while category=="":
        print("Category cannot be empty.")
        category=input("Enter category: ").strip()

    location=input("Enter location where it was lost: ").strip()
    while location=="":
        print("Location cannot be empty.")
        location=input("Enter location where it was lost: ").strip()

    description=input("Enter description: ").strip()
    while description=="":
        print("Description cannot be empty.")
        description=input("Enter description: ").strip()

    item={
        "id":max([item["id"] for item in items], default=0) + 1,
        "type":"lost",
        "username":username,
        "name":name,
        "category":category,
        "location":location,
        "description":description,
        "status":"active"
    }

    items.append(item)
    save_data(items)

    print("\nLost item reported successfully!")
    print("Report ID:",item["id"])


def report_found_item(items, username):
    print("\n--- Report Found Item ---")

    name=input("Enter item name: ").strip()
    while name=="":
        print("Item name cannot be empty.")
        name=input("Enter item name: ").strip()

    category=input("Enter category: ").strip()
    while category=="":
        print("Category cannot be empty.")
        category=input("Enter category: ").strip()

    location=input("Enter location where it was found: ").strip()
    while location=="":
        print("Location cannot be empty.")
        location=input("Enter location where it was found: ").strip()

    description=input("Enter description: ").strip()
    while description=="":
        print("Description cannot be empty.")
        description=input("Enter description: ").strip()

    item={
        "id":max([item["id"] for item in items], default=0) + 1,
        "type":"found",
        "username":username,
        "name":name,
        "category":category,
        "location":location,
        "description":description,
        "status":"active"
    }

    items.append(item)
    save_data(items)

    print("\nFound item reported successfully!")
    print("Report ID:",item["id"])


def view_lost_items(items):
    print("\n--- Lost Items ---")

    found=False

    for item in items:
        if item["type"]=="lost":
            print("\n------------------------------")
            print("Report ID:",item["id"])
            print("Item:",item["name"])
            print("Category:",item["category"])
            print("Location:",item["location"])
            print("Description:",item["description"])
            print("Status:",item["status"])
            print("Reported By:",item.get("username", "Unknown"))

            found=True

    if not found:
        print("No lost items found.")


def view_found_items(items):
    print("\n--- Found Items ---")

    found=False

    for item in items:
        if item["type"]=="found":

            print("\n------------------------------")
            print("Report ID:",item["id"])
            print("Item:",item["name"])
            print("Category:",item["category"])
            print("Location:",item["location"])
            print("Description:",item["description"])
            print("Status:",item["status"])
            print("Reported By:",item.get("username", "Unknown"))

            if item["status"]=="claimed":
                print("Claimed By:",item.get("claimed_by", "Unknown"))

            found=True

    if not found:
        print("No found items available.")


def search_items(items):
    print("\n--- Search Items ---")

    search=input(
        "Enter item name, category, location, or description: "
    ).lower()

    found=False

    for item in items:
        if (search in item["name"].lower() or
            search in item["category"].lower() or
            search in item["location"].lower() or
            search in item["description"].lower()):

            print("\n------------------------------")
            print("Matching Report")
            print("------------------------------")

            print("Report ID:", item["id"])
            print("Type:", item["type"])
            print("Item:", item["name"])
            print("Category:", item["category"])
            print("Location:", item["location"])
            print("Description:", item["description"])
            print("Status:", item["status"])

            found=True

    if not found:
        print("No matching items found.")
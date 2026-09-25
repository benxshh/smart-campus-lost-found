def find_matches(items):
    print("\n--- Find Possible Matches ---")

    try:
        report_id = int(input("Enter lost item report ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    lost_item=None

    for item in items:
        if item["id"]==report_id and item["type"]=="lost":
            lost_item=item
            break

    if lost_item is None:
        print("Lost item report not found.")
        return

    print("\nSearching for possible matches...")

    found_match=False

    for item in items:
        if item["type"]=="found" and item["status"]=="active":

            score=0

            lost_name=lost_item["name"].lower().split()
            found_name=item["name"].lower().split()

            common_words=set(lost_name) & set(found_name)

            if len(common_words)>0:
                score+=40

            if lost_item["category"].lower()==item["category"].lower():
                score+=20

            if lost_item["location"].lower()==item["location"].lower():
                score+=20

            if lost_item["description"].lower()==item["description"].lower():
                score+=20

            if score>=40:
                print("\nPossible Match Found!")
                print("Found Report ID:", item["id"])
                print("Item:", item["name"])
                print("Category:", item["category"])
                print("Location:", item["location"])
                print("Description:", item["description"])
                print("Match Score:", score, "%")

                found_match=True

    if not found_match:
        print("No possible matches found.")
def view_statistics(items):
    print("\n--- Campus Lost & Found Statistics ---")

    total=len(items)
    lost=0
    found=0
    active_lost=0
    active=0
    claimed=0
    user_reports ={}

    for item in items:

        username=item.get("username","Unknown")

        if username not in user_reports:
            user_reports[username]=0

        user_reports[username]+=1

        if item["type"]=="lost":
            lost+=1

            if item["status"]=="active":
                active_lost+=1

        elif item["type"]=="found":
            found+=1

            if item["status"]=="active":
                active+=1

            elif item["status"]=="claimed":
                claimed+=1

    print("\nTotal Reports:",total)
    print("Lost Items:",lost)
    print("Active Lost Items:",active_lost)
    print("Found Items:",found)
    print("Active Found Items:",active)
    print("Claimed Items:",claimed)

    print("\nReports By :-")

    for username, count in user_reports.items():
        print(username,":",count)
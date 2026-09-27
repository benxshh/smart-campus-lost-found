# Smart Campus Lost-and-Found Management System

## Problem Statement

In a college campus, students and staff may lose personal belongings such as wallets, ID cards, books, mobile phones, bags, and other items. Found items may also be reported by other students, but without an organized system, it can be difficult to maintain records, search for reports, and identify whether a found item belongs to someone who reported an item as lost.

The Smart Campus Lost-and-Found Management System is developed to provide a simple and organized way to manage these reports. The system allows users to report lost and found items, view and search reports, find possible matches, update or delete their own reports, and claim found items. An administrator can manage all reports and view basic statistics.

## Scope of the Project

The project is designed for managing lost-and-found records within a campus environment. It provides a command-line interface using Python and stores the report information locally in a JSON file.

The scope of the project includes user and administrator login, lost and found item reporting, viewing reports, searching, rule-based matching, updating and deleting reports, claiming found items, input validation, access control, and basic statistics.

The current version is developed as an educational project and does not include a web interface, mobile application, cloud storage, email/SMS notifications, image recognition, or a database.

## Target Users

The main target users of the system are:

- Students who lose personal belongings on campus.
- Students or staff members who find and report items.
- Campus administrators who need to manage lost-and-found records.

Normal users can manage their own reports and use the available lost-and-found functions. Administrators can view and manage all reports and access statistics.

## High-Level Features

The main features of the system are:

1. User and administrator login with role-based access.
2. Report lost items.
3. Report found items.
4. View lost and found reports.
5. Search reports using item name, category, location, or description.
6. Find possible matches using a rule-based matching score.
7. Update reports according to user permissions.
8. Delete reports with confirmation.
9. Claim found items.
10. Prevent users from claiming their own found reports.
11. Prevent already claimed items from being claimed again.
12. Store report data in a JSON file.
13. Automatically generate report IDs.
14. Validate user input.
15. Display basic lost-and-found statistics.
16. Save changes automatically after data modifications.
# Smart Campus Lost-and-Found Management System

A Python-based command-line application designed to help students and campus users report, search, manage, and claim lost-and-found items within a college campus.

## Project Overview

The Smart Campus Lost-and-Found Management System provides a simple digital platform for managing lost and found item reports.

Users can report lost or found items, search existing reports, find possible matches, update or delete their own reports, and claim found items. An administrator has additional privileges to manage reports and view system statistics.

The project uses Python and JSON for data storage and is designed to run directly from the command line.

## Features

### User Features

- Report a lost item
- Report a found item
- View lost items
- View found items
- Search items using name, category, location, or description
- Find possible matches between lost and found items
- Update personal reports
- Delete personal reports
- Claim found items
- View the status of reports
- Logout and switch between users

### Administrator Features

- View all lost item reports
- View all found item reports
- Search reports
- Update reports
- Delete reports
- View campus lost-and-found statistics

### System Features

- User login and role-based access
- Multiple user accounts
- Automatic report ID generation
- Input validation
- Delete confirmation
- Automatic saving of data
- JSON-based data storage
- Basic rule-based item matching
- Persistent data between program runs

## Technologies Used

- **Python 3** — Main programming language
- **JSON** — Used for storing and loading project data
- **Python Standard Library** — Used for built-in functionality
- **Command Line / PowerShell** — Used to run and interact with the application
- **Git and GitHub** — Used for version control and project submission

No external Python libraries are required to run this project.

## Project Structure

```text
smart-campus-lost-found/
│
├── main.py
├── data_manager.py
├── items.py
├── matching.py
├── statistics.py
├── data.json
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

- **`main.py`** — Contains the main program flow, login system, user and administrator menus, report updating, report deletion, and item claiming.
- **`data_manager.py`** — Handles saving and loading item data using JSON.
- **`items.py`** — Contains functions for reporting, viewing, and searching lost and found items.
- **`matching.py`** — Contains the rule-based matching system for finding possible matches between lost and found reports.
- **`statistics.py`** — Calculates and displays statistics about reports and users.
- **`data.json`** — Stores the application's report data.
- **`requirements.txt`** — Lists external dependencies. This project currently does not require any external Python packages.
- **`.gitignore`** — Specifies files and folders that should not be tracked by Git.
- **`README.md`** — Contains project documentation and instructions.

## Requirements

Before running the project, make sure the following are installed:

- Python 3.x
- Git (required if you want to clone the repository)

No external Python packages are required.

## Installation and Setup

### 1. Clone the Repository

Open PowerShell or Command Prompt and run:

```bash
git clone https://github.com/benxshh/smart-campus-lost-found.git
```

### 2. Open the Project Folder

```bash
cd smart-campus-lost-found
```

### 3. Check Python Installation

Run:

```bash
python --version
```

If Python is installed correctly, its version will be displayed.

### 4. Install Dependencies

This project uses only Python's built-in modules, so no external packages need to be installed.

The `requirements.txt` file is included for project structure and dependency documentation.

### 5. Run the Application

Run the following command:

```bash
python main.py
```

The application will start in the command-line terminal and display the login screen.

## Configuration

No additional configuration or environment variables are required.

The application automatically uses `data.json` to store and load report information.

## How to Use

### 1. Start the Application

Run:

```bash
python main.py
```

The login screen will appear in the terminal.

### 2. Login

Enter a valid username and password.

For demonstration purposes, the following user accounts are available:

| Username | Password | Role |
|---|---|---|
| user | user123 | User |
| student1 | student123 | User |
| student2 | student234 | User |
| student3 | student345 | User |
| rayan | rayan123 | User |

The administrator account is used for administrative functions and its credentials are kept separate from the public project documentation.

### 3. User Menu

After logging in as a normal user, the following operations are available:

1. Report Lost Item
2. Report Found Item
3. View Lost Items
4. View Found Items
5. Search Items
6. Find Possible Matches
7. Update Report
8. Delete Report
9. Claim Found Item
10. Logout

### 4. Administrator Menu

An administrator can:

- View lost item reports
- View found item reports
- Search reports
- View statistics
- Update reports
- Delete reports
- Logout

### 5. Exit the Application

To completely exit the application from the login screen, enter:

```text
0
```

The program will then terminate.

## Data Storage

The project uses a JSON file named `data.json` to store lost-and-found reports.

Each report contains information such as:

- Report ID
- Report type (lost or found)
- Username of the person who reported the item
- Item name
- Category
- Location
- Description
- Status

When a new report is created, the program adds it to the list of existing reports and automatically saves the updated data to `data.json`.

The application loads the existing data when it starts. This allows previously created reports to remain available even after the program is closed.

The project also handles situations where the JSON file is missing or contains invalid JSON data by starting with an empty list of reports.

## Matching Logic

The **Find Possible Matches** feature uses a basic rule-based approach to compare a lost item with found items.

The program checks active found-item reports and compares them with the selected lost-item report.

The matching score is calculated using the following conditions:

| Matching Condition | Score |
|---|---:|
| Common words in item names | 40% |
| Same category | 20% |
| Same location | 20% |
| Same description | 20% |

If the total score reaches **40% or more**, the found item is displayed as a possible match.

For example, if a user reports a lost **black wallet** and another user reports finding a **black leather wallet**, the common word in the item names can contribute to the matching score. If other details such as category and location also match, the score increases.

The matching system is rule-based and is intended to provide possible matches rather than guarantee that two reports refer to the same physical item.

## Input Validation and Access Control

The application includes basic validation to improve reliability and prevent invalid input.

- Empty item names, categories, locations, and descriptions are not accepted.
- Report IDs are checked to ensure that numeric input is provided.
- Delete operations require confirmation from the user.
- Users can update and delete only their own reports.
- Administrators can manage reports across the system.
- A user cannot claim a found item that they reported themselves.
- An already claimed found item cannot be claimed again.
- Report IDs are generated automatically to avoid manually entering IDs.
- User roles determine which menu options and operations are available.

## Limitations

The current version is a command-line application and uses a local JSON file for data storage.

Some limitations include:

- It does not use a database server.
- It does not provide a graphical user interface.
- The matching system uses simple rule-based comparisons rather than machine learning.
- User authentication is designed for a college project demonstration and is not intended for production-level security.
- The application is intended to run locally on a computer.

## Future Improvements

The project can be extended in the future by adding:

- A graphical or web-based user interface
- Database integration using MySQL or SQLite
- Stronger password security
- Email or notification support
- Image upload for lost and found items
- More advanced item matching
- Search filters by category, location, and status
- Improved administrator controls
- Cloud-based data storage
- Deployment for use across multiple campus locations

## Author

**Mohd Rayan Khan**

BTech CSE — First Year

This project was developed as part of the Python Essentials course project.
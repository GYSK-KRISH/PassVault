# PASSVAULT

PASSVAULT is a Class 12 Informatics Practices desktop project built with Python, Tkinter, MySQL, Pandas, and Matplotlib.

It demonstrates password generation, basic password-strength analysis, credential storage, database operations, and security analytics.

## Project Objectives

- Generate customizable passwords.
- Analyze password strength using simple rules.
- Store credential records in MySQL.
- Display stored records through a desktop GUI.
- Keep passwords masked in the normal table view.
- Analyze credential categories using Pandas.
- Visualize category counts and password-strength distribution with Matplotlib.
- Demonstrate how Python, a database, data analysis, and visualization work together.

## Important Security Limitation

This is an educational project, not a production password manager. Passwords are stored using Base64 encoding so the database representation differs from the original password.

Base64 is encoding, not encryption. A real password manager would require proper cryptographic protection, secure key management, and a security review.

## Project Structure

```text
PassVault/
├── app.py
├── database.sql
├── requirements.txt
├── README.md
└── screenshots/
```

## Required Software

- Python 3
- MySQL Server
- MySQL Workbench or another MySQL client
- VS Code with the Python extension

## Installation

For the exact 10-step procedure to configure the project on another computer, read [SCHOOL_SETUP.md](SCHOOL_SETUP.md).

Install the Python packages from the project folder:

```powershell
python -m pip install -r requirements.txt
```

Tkinter normally comes with Python on Windows and is not listed in `requirements.txt`.

## Database Setup

1. Start the MySQL service.
2. Open `database.sql` in MySQL Workbench.
3. Execute the script.
4. Open `app.py`.
5. Set the database environment variables in PowerShell before running the app:

```powershell
$env:PASSVAULT_DB_HOST = "localhost"
$env:PASSVAULT_DB_USER = "root"
$env:PASSVAULT_DB_PASSWORD = "YOUR_MYSQL_PASSWORD"
$env:PASSVAULT_DB_NAME = "passvault_db"
```

Do not publish a real database password in source code or commit it to Git.

## Run the Application

```powershell
python app.py
```

## Main Features

- Generate passwords from 8 to 32 characters
- Select lowercase, uppercase, numbers, and symbols
- Analyze password strength as Weak, Moderate, or Strong
- Copy generated passwords to the clipboard
- Save credential records in MySQL
- View records in a masked Tkinter table
- Reveal or delete a selected record
- Refresh the table
- Display category and strength analytics with Pandas and Matplotlib

### Password Generator

The generator accepts a length from 8 to 32 characters and supports lowercase letters, uppercase letters, numbers, and symbols. Every selected character category is represented in the generated result before the remaining characters are randomized.

### Password Strength Analyzer

The analyzer gives a `Weak`, `Moderate`, or `Strong` result. It checks whether the password has at least 8 or 12 characters and whether it contains lowercase letters, uppercase letters, numbers, and symbols. This is a simple educational indicator, not a professional security audit.

### Credential Vault

Each record contains an account name, username or email, password, category, strength tier, and creation date. Records can be saved, viewed, refreshed, revealed, and deleted. Passwords are masked in the Treeview.

### Analytics

The View Analytics button loads only `category` and `strength_tier` into a Pandas DataFrame. `value_counts()` produces the statistics used for a category bar chart and a password-strength pie chart.

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Tkinter | Desktop graphical user interface |
| MySQL | Persistent credential database |
| mysql-connector-python | Python-to-MySQL connection |
| Pandas | DataFrame analysis and counting |
| Matplotlib | Bar and pie charts |
| Base64 | Encoding demonstration only |

Base64 is an encoding method, not encryption.

## System Architecture

```text
User
	|
Tkinter GUI
	|
Application Logic
	|
MySQL Database
	|
Pandas Analysis
	|
Matplotlib Visualization
```

The user operates the Tkinter interface. Python validates inputs and performs application tasks. MySQL stores records. Pandas analyzes non-sensitive summary fields, and Matplotlib displays the results.

## Database Design

Database: `passvault_db`

Table: `credentials`

| Field | Purpose |
|-------|---------|
| `id` | Unique record identifier |
| `account_name` | Website or service name |
| `username_email` | Associated username or email |
| `encrypted_password` | Base64-encoded classroom demonstration value |
| `category` | Social, Work, Education, Finance, Gaming, or Other |
| `strength_tier` | Weak, Moderate, or Strong |
| `created_date` | Date on which the record was saved |

The column is named `encrypted_password` in the supplied schema, but the value stored by this project is Base64 encoded, not encrypted.

## SQL Operations

- `CREATE DATABASE` creates `passvault_db` if it does not exist.
- `CREATE TABLE` creates the `credentials` table.
- `INSERT` saves a new credential.
- `SELECT` reads records for the Treeview or analytics.
- `DELETE` removes the selected record.

The `id` field is a primary key, so it uniquely identifies a row. `AUTO_INCREMENT` creates a new numeric ID automatically. `NOT NULL` requires a value for important fields.

## Application Workflow

1. The user opens PASSVAULT.
2. The user generates a password.
3. The strength analyzer evaluates it.
4. The user can copy the password.
5. The user enters credential information.
6. The credential is encoded for this classroom demonstration and saved in MySQL.
7. Records appear in the masked Treeview after refresh.
8. The user can reveal, delete, or refresh records.
9. The user selects View Analytics.
10. Pandas reads category and strength data from MySQL.
11. Matplotlib displays the two charts.

## Error Handling and Validation

The application handles invalid password lengths, non-numeric lengths, disabled character types, empty form fields, invalid categories, missing Treeview selections, database failures, empty analytics data, decoding errors, and clipboard errors with message boxes. Database connections are closed in `finally` blocks where applicable.

## Common Problems

- **Access denied:** Check the MySQL username and password in `DB_CONFIG`.
- **Database does not exist:** Execute `database.sql` in MySQL Workbench.
- **Connection failed:** Confirm that the MySQL service is running.
- **No analytics shown:** Save at least one credential before opening analytics.
- **No row selected:** Select a table row before revealing or deleting it.

## Security Limitations

PASSVAULT is an educational Class 12 project, not a production-grade password manager.

- Base64 is encoding, not encryption.
- The Base64 value can be decoded and does not provide real password protection.
- Real password managers use cryptographic protection and secure key management.
- Database credentials should not be hard-coded in a real production application.
- Sensitive data requires appropriate access control, storage, and auditing in real systems.

## Future Scope

The following are future improvements and are not currently implemented:

- Strong cryptographic encryption
- Secure key management
- User authentication
- Stronger password policies
- Audit logging
- Backup and recovery
- More detailed security analytics
- Professional deployment and security testing

## Educational Topics Demonstrated

- Python functions, classes, conditions, and loops
- Tkinter widgets and event-driven programming
- MySQL connectivity and parameterized SQL
- Create, read, and delete database operations
- Pandas DataFrames and `value_counts()`
- Matplotlib bar and pie charts
- Exception handling and input validation

## Submission Checklist

- [ ] Python and MySQL are installed.
- [ ] Required packages are installed from `requirements.txt`.
- [ ] MySQL service is running.
- [ ] `database.sql` has been executed successfully.
- [ ] `DB_CONFIG` contains the correct local settings.
- [ ] The application starts with `python app.py`.
- [ ] Password generation and strength analysis work.
- [ ] A credential can be saved and displayed in the table.
- [ ] Passwords are masked in the table.
- [ ] Reveal and delete actions work.
- [ ] Both analytics charts open.
- [ ] Screenshots are stored in the `screenshots/` folder.
- [ ] No real password has been published in the project files.

## Suggested Demonstration Order

1. Start the application.
2. Generate a password and show its strength.
3. Copy the generated password.
4. Save a sample credential.
5. Refresh the table and show the masked password.
6. Reveal the selected password and explain the Base64 limitation.
7. Delete the sample record.
8. Open Security Analytics and explain both charts.

## Testing Documentation

| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| Application startup | Window opens without a traceback | PASS |
| Python compilation | `app.py` compiles successfully | PASS |
| Password generation | Requested lengths and selected categories work | PASS |
| Invalid generator input | Clear error message appears | PASS |
| Strength analysis | Weak, Moderate, and Strong tiers work | PASS |
| Clipboard handling | Copy succeeds or shows a handled error | PASS |
| Form validation | Invalid data is blocked | PASS |
| Database connection | Valid local credentials connect | PENDING local password |
| Credential insertion | Record is saved in MySQL | PENDING local database |
| Treeview display | Records appear with masked passwords | PENDING local database |
| Password masking | Actual password is hidden by default | PASS by code inspection |
| Reveal | Selected record password is decoded | PENDING local database |
| Delete | Selected record is deleted after confirmation | PENDING local database |
| Refresh | Latest records are loaded | PENDING local database |
| Pandas analytics | Category and strength data are analyzed | PASS by simulated failure and code validation |
| Matplotlib charts | Both charts open from real records | PENDING local database |
| Empty database | No Data message appears | PENDING local database |
| Database failure | Useful error message appears without crashing | PASS by simulation |

Tests marked pending require the user's local MySQL password and database setup. They must not be described as completed until run with real records.

## Screenshots to Capture

Use dummy data only and store screenshots in `screenshots/`:

1. Main PASSVAULT interface
2. Generated password and strength result
3. Credential form
4. Masked credentials Treeview
5. Reveal or delete workflow
6. Category bar chart
7. Strength pie chart
8. MySQL `credentials` table

Do not include real usernames, emails, passwords, or database credentials.

## Viva Questions and Answers

### 1. What is the purpose of PASSVAULT?

It generates passwords, evaluates their basic strength, stores credential records, and displays simple security analytics.

### 2. Why is Tkinter used?

Tkinter is Python's standard GUI library. It allows the project to create windows, forms, buttons, checkboxes, tables, and message boxes.

### 3. Why is MySQL used?

MySQL stores credential records permanently so they can be loaded again when the application runs.

### 4. What is a primary key?

A primary key uniquely identifies each record in a table. In this project, `id` is the primary key.

### 5. What does `AUTO_INCREMENT` do?

It automatically generates a new numeric ID for each inserted record.

### 6. Why are parameterized queries used?

They separate SQL instructions from user data and help prevent SQL injection problems.

### 7. What is Base64?

Base64 is an encoding technique that represents data using text characters. It is not encryption and does not provide real password security.

### 8. How is password strength calculated?

The program checks password length and whether it contains lowercase letters, uppercase letters, numbers, and symbols.

### 9. Why are selected character categories guaranteed in generated passwords?

The program first chooses one character from every selected category and fills the remaining positions afterward.

### 10. What is a Pandas DataFrame?

A DataFrame is a table-like data structure used by Pandas for storing and analyzing rows and columns.

### 11. How is Pandas used in this project?

Pandas loads category and strength data from MySQL and uses `value_counts()` to calculate frequencies.

### 12. How is Matplotlib used?

Matplotlib creates the category bar chart and the password-strength pie chart.

### 13. What is exception handling?

Exception handling allows the program to respond to errors, such as an unavailable MySQL server, without crashing immediately.

### 14. What is CRUD?

CRUD means Create, Read, Update, and Delete. This project demonstrates Create, Read, and Delete operations.

### 15. Is this a production-grade password manager?

No. It is a classroom project. A real password manager would need encryption, secure key management, authentication, auditing, and professional security testing.

### 16. What is Python?

Python is a high-level programming language used in this project for the GUI, logic, database connection, and analysis.

### 17. What is a variable?

A variable is a named place used to store a value, such as a password length or account name.

### 18. What is a function?

A function is a reusable block of code that performs a particular task.

### 19. What is a conditional statement?

A conditional statement makes a decision using conditions such as `if` and `else`.

### 20. What is a loop?

A loop repeats a block of code, for example while checking character categories or loading table rows.

### 21. What is a GUI?

A GUI is a graphical interface containing windows, fields, buttons, labels, and tables.

### 22. What is a widget?

A widget is one GUI component, such as a Button, Entry, Checkbutton, Label, or Treeview.

### 23. What is event-driven programming?

It is programming where functions run in response to events such as button clicks.

### 24. What is MySQL?

MySQL is a relational database management system used to store the credential records.

### 25. What is a database table?

A table stores related data in rows and columns. PASSVAULT uses the `credentials` table.

### 26. What do `INSERT`, `SELECT`, and `DELETE` do?

`INSERT` adds a record, `SELECT` reads records, and `DELETE` removes a record.

### 27. What is a Pandas DataFrame?

A DataFrame is a table-like Pandas structure containing rows and columns for analysis.

### 28. What does `value_counts()` do?

It counts the occurrences of each different value in a DataFrame column.

### 29. What is an edge case?

An edge case is an unusual situation, such as an empty database or all generator options being disabled.

### 30. Why is exception handling important?

It allows the application to show a useful error message instead of stopping unexpectedly.

## Project Abstract

PASSVAULT is a Python desktop application developed as a Class 12 Informatics Practices project. Its purpose is to demonstrate how a graphical user interface, a relational database, data analysis, and data visualization can work together. The application uses Tkinter to provide a password generator, a rule-based password-strength analyzer, a credential form, and a masked record table. Credential records are stored in a MySQL database named `passvault_db` in the `credentials` table. Pandas reads non-sensitive category and strength fields into a DataFrame and calculates frequencies using `value_counts()`. Matplotlib then displays a category bar chart and a password-strength pie chart. The application includes input validation, database error handling, clipboard handling, record deletion, password revealing, and table refreshing. For educational demonstration, passwords are stored using Base64 encoding, which is not encryption. Therefore, PASSVAULT is not a production-grade password manager. The project demonstrates Python programming, GUI design, SQL operations, exception handling, DataFrame analysis, and graphical visualization in one understandable desktop application.

## Project Conclusion

PASSVAULT successfully demonstrates the integration of Python, Tkinter, MySQL, Pandas, and Matplotlib in a single desktop application. It generates customizable passwords, evaluates their basic strength, stores credential records, displays masked data, and presents database-driven charts. During development, concepts such as functions, classes, validation, parameterized SQL, exception handling, DataFrames, and visualization were practiced. The project is educational rather than production software because its Base64 password representation is only encoding and does not provide encryption. Even with this limitation, PASSVAULT is useful for understanding how a Python program can collect user input, store structured data, analyze records, and convert results into visual information.

## 30-45 Second Project Introduction

PASSVAULT is a Python desktop application for password generation, credential storage, and basic security analysis. It helps users generate customizable passwords, check their strength, and save credential records in a MySQL database. The interface is built with Tkinter. Pandas loads category and strength information into a DataFrame, and Matplotlib displays a category bar chart and a password-strength pie chart. The project demonstrates how Python, GUI programming, SQL, data analysis, and visualization can be combined in one application. It is a Class 12 educational project, so Base64 is used only as encoding for demonstration and is not claimed to be encryption.

## One-Minute Project Explanation

The problem addressed by PASSVAULT is that users need a simple way to generate and organize sample credential records while learning about password strength. The solution is a Tkinter desktop application with a password generator, a rule-based strength analyzer, and a credential form. The form saves records to the MySQL database `passvault_db`, table `credentials`. The application can read records into a Treeview with passwords masked, reveal a selected encoded value for demonstration, delete records, and refresh the table. For analytics, only category and strength fields are read into a Pandas DataFrame. `value_counts()` calculates the number of records in each group, and Matplotlib displays the results as a bar chart and a pie chart. The result is a complete, understandable example of GUI, database, analysis, and visualization integration.

## Final Submission Checklist

- [ ] `app.py` included
- [ ] `database.sql` included
- [ ] `requirements.txt` included
- [ ] `README.md` included
- [ ] Screenshots captured using dummy data
- [ ] Application starts successfully
- [ ] MySQL database and table created
- [ ] Local `DB_CONFIG` tested without publishing the password
- [ ] Database-dependent tests completed locally
- [ ] Testing results updated honestly
- [ ] Viva questions reviewed
- [ ] No real credentials included in screenshots or source files

## Final Verification

The documented implementation currently includes the password generator, strength analyzer, clipboard copy, credential form, MySQL storage, masked Treeview, reveal, delete, refresh, Pandas analytics, Matplotlib charts, input validation, exception handling, and UI polish.

Before submission, the only remaining project-specific verification is to configure the local MySQL password, execute `database.sql`, and complete the pending real-database tests listed above. No unrelated code changes are required.

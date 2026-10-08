# PASSVAULT: SENIOR SCHOOL COMPUTER SCIENCE PROJECT REPORT

**PROJECT TITLE:** PassVault — Credential Manager & Security Analyzer  
**ACADEMIC YEAR:** 2026 – 2027  
**SUBMITTED FOR:** CBSE Class 12 Computer Science Practical Examination  
**SUBJECT CODE:** 083  
**PROGRAMMING LANGUAGE:** Python 3  
**DATABASE ENGINE:** MySQL Relational Database Management System (RDBMS)  
**GUI FRAMEWORK:** Python Tkinter & ttk  
**ANALYTICS & VISUALIZATION:** Pandas & Matplotlib  

---

## 📑 TABLE OF CONTENTS

| SR NO. | SECTION DESCRIPTION |
| :---: | :--- |
| **01** | **INTRODUCTION** |
| **02** | **PROBLEM STATEMENT & NEED FOR THE PROJECT** |
| **03** | **PROJECT OBJECTIVES** |
| **04** | **SCOPE OF THE PROJECT** |
| **05** | **PROJECT METHODOLOGY** |
| **06** | **SYSTEM REQUIREMENTS** |
| **07** | **ALGORITHMS & FLOWCHARTS** |
| **08** | **DATABASE DESIGN & ER MODEL** |
| **09** | **DATA DICTIONARY** |
| **10** | **DATABASE OPERATIONS** |
| **11** | **SECURITY FEATURES & INPUT VALIDATION** |
| **12** | **USER INTERFACE DESIGN & LAYOUT** |
| **13** | **SOURCE CODE** |
| **14** | **RESULTS AND OUTCOMES** |
| **15** | **LIMITATIONS** |
| **16** | **FUTURE SCOPE** |
| **17** | **CONCLUSION & LEARNING OUTCOMES** |
| **18** | **BIBLIOGRAPHY & REFERENCES** |

---

## 01. INTRODUCTION

### Background
Computer users regularly register accounts across educational portals, email providers, social media platforms, banking systems, and online services. Security guidelines mandate that every account should use a unique, complex password consisting of uppercase letters, lowercase letters, numbers, and symbols. 

However, remembering dozens of distinct passwords without software assistance is virtually impossible for most individuals. As a result, users default to predictable patterns (e.g., `Password123`, `User2026`), exposing themselves to dictionary and credential-stuffing attacks.

### Purpose
**PassVault** bridges the gap between strong cybersecurity practices and user convenience. It acts as a personal credential repository and security auditor on the user's computer, empowering users to create robust passwords, keep records organized by category, and evaluate their overall security posture.

---

## 02. PROBLEM STATEMENT & NEED FOR THE PROJECT

### Problem Statement
Most internet users suffer from **Password Fatigue**, leading to three primary security risks:
1. **Password Reuse:** Using the same single password across multiple websites.
2. **Weak Passwords:** Setting simple, dictionary-based passwords that can be guessed easily.
3. **Unorganized Credential Tracking:** Storing usernames and passwords in cleartext text files, paper notebooks, or unencrypted spreadsheets.

### Need for the Project
There is a need for a lightweight, localized desktop application that allows students and individual users to:
- Generate random passwords instantly without relying on third-party online generators.
- Safely store credentials in a local MySQL relational database.
- Receive immediate visual feedback regarding the complexity score of passwords before saving them.
- View statistical analytics highlighting vulnerable accounts that require security upgrades.

---

## 03. PROJECT OBJECTIVES

The primary objective of PassVault is to design, implement, and validate a desktop management system. The specific goals include:

1. **Customizable Password Generation:** Implement a random character generator allowing users to specify password lengths (8 to 32 characters) and toggle upper, lower, numeric, and special character sets.
2. **Real-time Complexity Scoring:** Build a rule-based complexity scoring algorithm that categorizes passwords into **Weak**, **Moderate**, or **Strong** tiers and updates visual progress bars dynamically.
3. **Relational Database Storage:** Establish a Python-to-MySQL database pipeline using `mysql-connector-python` to perform SQL statements (`INSERT`, `SELECT`, `DELETE`).
4. **Data Privacy & Masking:** Ensure passwords are displayed as masked strings (`********`) in the main UI table, with on-demand Base64 decoding when selected by the user.
5. **Data Analytics Dashboard:** Integrate `Pandas` and `Matplotlib` to generate graphical charts displaying account category distribution and password strength ratios.
6. **Robust Error Handling:** Include defensive programming techniques to handle missing inputs, database connectivity failures, and invalid operations gracefully.

---

## 04. SCOPE OF THE PROJECT

### Operational Scope
- **Target Audience:** School students, educators, and individual desktop users managing personal account credentials locally.
- **Deployment Model:** Single-user local desktop application running on Windows, macOS, or Linux environments equipped with Python 3 and MySQL.

### Technical Scope
- **Interface:** Native Graphical User Interface (GUI) built with `tkinter` and `ttk`.
- **Backend Storage:** Local MySQL Database (`passvault_db`) executing on `localhost:3306`.
- **Analytics:** Data visualization rendering comparative bar charts and pie charts via `Matplotlib`.

---

## 05. PROJECT METHODOLOGY

The development of **PassVault** followed a structured Software Development Life Cycle (SDLC) approach tailored for educational software projects:

```text
┌──────────────────────────┐
│   Requirement Analysis   │ -> Identify credential tracking & security needs
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│      System Design       │ -> Architectural layer planning (GUI -> Logic -> DB)
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│     Database Design      │ -> Schema creation (passvault_db & credentials table)
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│  Application Coding      │ -> Implementation using Python, Tkinter, and MySQL
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│    Analytics Engine      │ -> Integrating Pandas & Matplotlib charts
└────────────┬─────────────┘
             │
┌────────────▼─────────────┐
│   Testing & Validation   │ -> Functional, validation, and error-handling tests
└──────────────────────────┘
```

1. **Requirement Analysis:** Identified essential password management and security auditing features.
2. **System Design:** Structured the project into modular components (GUI, Strength Engine, DB Controller, Analytics).
3. **Database Design:** Created `database.sql` defining `passvault_db` and the `credentials` table with primary key constraints.
4. **Application Development:** Developed the Python codebase (`app.py`) using Object-Oriented Programming (OOP) in Tkinter.
5. **Database Integration:** Implemented parameterized SQL execution via `mysql-connector-python`.
6. **Analytics Integration:** Configured `Pandas` dataframes and `Matplotlib` figure rendering.
7. **Testing & Validation:** Executed comprehensive test cases covering positive inputs, negative inputs, boundaries, and database failures.

---

## 06. SYSTEM REQUIREMENTS

### Hardware Requirements

| Hardware Component | Minimum Requirement | Recommended Specification |
| :--- | :--- | :--- |
| **Processor (CPU)** | Intel Core i3 (2.0 GHz) / AMD Dual-Core | Intel Core i5 / AMD Ryzen 5 or higher |
| **System RAM** | 4 GB | 8 GB or higher |
| **Available Disk Space**| 500 MB | 1 GB SSD storage |
| **Display Resolution**| 1024 x 768 pixels | 1920 x 1080 (Full HD) |
| **Input Devices** | Standard Keyboard and Mouse | Standard Keyboard and Mouse |

### Software & Environment Requirements

| Component | Specification / Version |
| :--- | :--- |
| **Operating System** | Microsoft Windows 10 / 11, macOS Monterey+, or Ubuntu Linux 20.04+ |
| **Language Runtime** | Python 3.10.x – Python 3.14.x |
| **Database Server** | MySQL Community Server 8.0 / 8.4 or MySQL Workbench |
| **IDE / Code Editor** | Visual Studio Code / PyCharm / IDLE |

### Required Python Libraries

```powershell
python -m pip install mysql-connector-python pandas matplotlib
```

- **`tkinter` / `ttk`:** Native GUI widget toolkit for building desktop frames, entries, buttons, treeviews, and dialog boxes.
- **`mysql-connector-python`:** Official MySQL driver for executing SQL statements from Python scripts.
- **`pandas`:** Data manipulation library used to transform SQL query results into DataFrames for analytical aggregation.
- **`matplotlib`:** Plotting engine used to generate bar charts and pie graphs.
- **`base64` & `binascii`:** Standard modules used for string encoding and decoding during classroom storage demonstrations.

---

## 07. ALGORITHMS & FLOWCHARTS

### Algorithm 1: Password Generation Algorithm

```text
================================================================================
ALGORITHM 1: GENERATE CUSTOMIZABLE RANDOM PASSWORD
================================================================================
INPUT : length (Integer 8-32), use_lowercase (Bool), use_uppercase (Bool), 
        use_numbers (Bool), use_symbols (Bool)
OUTPUT: generated_password (String)

1. START
2. Initialize character pool array `charset` = []
3. IF use_lowercase is TRUE THEN append 'a'..'z' to charset
4. IF use_uppercase is TRUE THEN append 'A'..'Z' to charset
5. IF use_numbers is TRUE THEN append '0'..'9' to charset
6. IF use_symbols is TRUE THEN append '!@#$%^&*()_+-=' to charset
7. IF charset is EMPTY THEN
     Display Warning ("Select at least one character set")
     RETURN
8. Initialize password array `result` = []
9. FOR i FROM 1 TO length DO:
     Select random character `ch` from `charset`
     Append `ch` to `result`
10. Convert `result` array to String `generated_password`
11. Display `generated_password` in UI Entry field
12. Execute Algorithm 2 (Calculate Strength)
13. END
================================================================================
```

---

### Algorithm 2: Rule-Based Password Complexity Scoring

```text
================================================================================
ALGORITHM 2: RULE-BASED PASSWORD COMPLEXITY SCORING
================================================================================
INPUT : password (String)
OUTPUT: score (Integer 0-6), strength_tier (String: "Weak" | "Moderate" | "Strong")

1. START
2. Initialize `score` = 0
3. IF length(password) >= 8 THEN score = score + 1
4. IF length(password) >= 12 THEN score = score + 1
5. IF password contains LOWERCASE character THEN score = score + 1
6. IF password contains UPPERCASE character THEN score = score + 1
7. IF password contains DIGIT character THEN score = score + 1
8. IF password contains SYMBOL character THEN score = score + 1
9. EVALUATE score:
     IF score <= 2 THEN
        strength_tier = "Weak"
        progress_bar_color = RED (33%)
     ELSE IF score is 3 OR 4 THEN
        strength_tier = "Moderate"
        progress_bar_color = AMBER (66%)
     ELSE (score 5 or 6)
        strength_tier = "Strong"
        progress_bar_color = GREEN (100%)
10. Update UI Progress Bar Value and Text Label
11. RETURN strength_tier
12. END
================================================================================
```

---

## 08. DATABASE DESIGN & ER MODEL

### Database Identification
- **Database Engine:** MySQL 8.0 Server
- **Database Name:** `passvault_db`
- **Primary Table:** `credentials`

---

## 09. DATA DICTIONARY

### Table: `credentials`

| Column Name | Data Type | Nullable | Key Constraints | Default Value | Description / Remarks |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`id`** | `INT` | No | **PRIMARY KEY** | `AUTO_INCREMENT` | Unique integer record identifier. |
| **`account_name`** | `VARCHAR(100)` | No | None | None | Name of service/website (e.g. GitHub, Google). |
| **`username_email`**| `VARCHAR(120)` | No | None | None | Account login name, handle, or email address. |
| **`encrypted_password`**| `VARCHAR(255)`| No | None | None | Base64-encoded password representation string. |
| **`category`** | `VARCHAR(50)` | No | None | `'Other'` | Category group (*Email, Work, Social, Banking, Other*). |
| **`strength_tier`**| `VARCHAR(20)` | No | None | None | Security rating (*Weak, Moderate, Strong*). |
| **`created_date`** | `DATE` | No | None | None | Record creation date stamp (`YYYY-MM-DD`). |

---

## 10. DATABASE OPERATIONS

PassVault executes four database and data manipulation operations:

```text
                       DATABASE OPERATIONS IN PASSVAULT
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         ▼                            ▼                            ▼
    1. CREATE                     2. READ                      3. REVEAL
  (SQL INSERT)                  (SQL SELECT)               (Base64 Decode)
         │                            │                            │
         └────────────────────────────┼────────────────────────────┘
                                      ▼
                                  4. DELETE
                                (SQL DELETE)
```

### 1. CREATE — Insert a New Credential
- **Trigger:** User fills the credential form and clicks **Save Credential to Vault**.
- **SQL Statement:**
  ```sql
  INSERT INTO credentials (account_name, username_email, encrypted_password, category, strength_tier, created_date)
  VALUES (%s, %s, %s, %s, %s, %s);
  ```
- **Execution Logic:** Converts the plaintext password string into a Base64 encoded string (`base64.b64encode()`), binds arguments into a parameterized query tuple, executes insertion, commits the transaction, and refreshes the vault table.

### 2. READ — Retrieve & Display Credentials
- **Trigger:** Application startup or after any table mutation.
- **SQL Statement:**
  ```sql
  SELECT id, account_name, username_email, category, strength_tier, created_date 
  FROM credentials 
  ORDER BY id DESC;
  ```
- **Execution Logic:** Queries records ordered by newest ID first, iterates through the result set, masks passwords as `********`, and populates the `ttk.Treeview` widget.

### 3. REVEAL — Selective Base64 Decoding
- **Trigger:** User selects a row in the table and clicks **Reveal Selected Password**.
- **SQL Statement:**
  ```sql
  SELECT encrypted_password FROM credentials WHERE id = %s;
  ```
- **Execution Logic:** Fetches the Base64 encoded string for the selected ID, decodes it using `base64.b64decode()`, and presents the decoded string in an information message dialog box.

### 4. DELETE — Remove Credential
- **Trigger:** User selects a row in the table and clicks **Delete Selected Credential**.
- **SQL Statement:**
  ```sql
  DELETE FROM credentials WHERE id = %s;
  ```
- **Execution Logic:** Prompts the user with a confirmation dialog (`messagebox.askyesno`). If confirmed, executes deletion, commits transaction, and refreshes the table.

---

## 11. SECURITY FEATURES & INPUT VALIDATION

1. **Input Sanitization:**
   - Account names and usernames are sanitized using `.strip()` to strip leading and trailing whitespace characters.
   - Input validation guards prevent submission of empty account or username fields.

2. **Base64 String Encoding Demonstration:**
   - Plaintext passwords are not stored directly in cleartext SQL queries. Passwords are converted into Base64 encoded string representations before SQL execution.
   - *Technical Note:* Base64 is an encoding format, not cryptographic encryption. It is used here for educational demonstration of string transformations in database applications.

3. **Data Masking in UI:**
   - The primary `Treeview` table displays uniform mask strings (`********`) for all password fields to prevent casual shoulder-surfing.

4. **Parameterized SQL Queries:**
   - All database executions utilize parameterized SQL query placeholders (`%s`) to prevent SQL Injection (SQLi) vulnerabilities.

5. **Defensive Connection Handling:**
   - Database routines are wrapped in `try ... except mysql.connector.Error` blocks.
   - Database connections are closed in `finally` blocks to prevent unclosed connection leaks.

---

## 12. USER INTERFACE DESIGN & LAYOUT

### ASCII Wireframe Representation

```text
+-----------------------------------------------------------------------------+
|                                PASSVAULT                                    |
|         Password Generator | Credential Vault | Security Analytics          |
+-----------------------------------------------------------------------------+
|  [Password Generator]                                                       |
|  Length: [ 14 ]  [x] Lowercase  [x] Uppercase  [x] Numbers  [x] Symbols    |
|  Generated Password: [ k9#mP2$vL8!xQ1                             ] [Generate]|
|  Strength: [========================= Strong ============================]  |
+-----------------------------------------------------------------------------+
|  [Save Credential to Vault]                                                 |
|  Account Name: [ GitHub           ]  Username/Email: [ student@email.com  ] |
|  Password:     [ k9#mP2$vL8!xQ1   ]  Category:       [ Work             v ] |
|                                                      [ Save Credential   ]  |
+-----------------------------------------------------------------------------+
|  [Stored Credentials Vault]                                                 |
|  ID   Account    Username/Email       Password   Category   Strength   Date |
|  -------------------------------------------------------------------------  |
|  02   GitHub     student@email.com    ********   Work       Strong   2026-10-07|
|  01   Google     user@gmail.com       ********   Email      Moderate 2026-10-07|
|                                                                             |
|  [ Reveal Password ]       [ Delete Credential ]   [ View Security Analytics]|
+-----------------------------------------------------------------------------+
| Status: Credential table refreshed: 2 record(s).                            |
+-----------------------------------------------------------------------------+
```

---

## 13. SOURCE CODE

Below is the complete application codebase (`app.py`):

```python
import base64
import binascii
from datetime import date
import os
import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

# Color Palette Constants
BG_COLOR = "#F4F7FB"
CARD_COLOR = "#FFFFFF"
HEADER_COLOR = "#172B4D"
PRIMARY_COLOR = "#136CC5"
PRIMARY_HOVER = "#1565C0"
SUCCESS_COLOR = "#16A34A"
SUCCESS_HOVER = "#018833"
DANGER_COLOR = "#DC2626"
DANGER_HOVER = "#B91C1C"
WARNING_COLOR = "#F59E0B"
WARNING_HOVER = "#D97706"
ANALYTICS_COLOR = "#6D4CC2"
ANALYTICS_HOVER = "#5B3FA3"
TEXT_COLOR = "#172B4D"
BORDER_COLOR = "#B8D4F5"
TABLE_HEADER = "#173F73"

# MySQL Database Configuration
DB_CONFIG = {
    "host": os.getenv("PASSVAULT_DB_HOST", "localhost"),
    "user": os.getenv("PASSVAULT_DB_USER", "root"),
    "password": os.getenv("PASSVAULT_DB_PASSWORD", ""),
    "database": os.getenv("PASSVAULT_DB_NAME", "passvault_db"),
}

class PassVaultApp:
    """Main window controller for PASSVAULT desktop application."""

    def __init__(self, root):
        self.root = root
        self.root.title("PassVault | Credential Manager & Security Analyzer")
        self.root.geometry("1000x760")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.password_length = tk.StringVar(value="14")
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()
        self.password_strength = tk.StringVar(value="Strength: Pending analysis")
        self.account_name = tk.StringVar()
        self.username_email = tk.StringVar()
        self.credential_password = tk.StringVar()
        self.credential_category = tk.StringVar(value="Other")

        self.configure_styles()
        self.create_interface()
        self.load_credentials()

    def configure_styles(self):
        """Configure application visual theme styles."""
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure("App.TFrame", background=BG_COLOR)
        self.style.configure("TFrame", background=CARD_COLOR)
        self.style.configure("TLabel", background=CARD_COLOR, foreground=TEXT_COLOR, font=("Segoe UI", 9))
        self.style.configure("TCheckbutton", background=CARD_COLOR, foreground=TEXT_COLOR, font=("Segoe UI", 9))
        self.style.configure("TEntry", fieldbackground=CARD_COLOR, foreground=TEXT_COLOR, padding=5)
        self.style.configure("TCombobox", fieldbackground=CARD_COLOR, background=CARD_COLOR, foreground=TEXT_COLOR, padding=4)
        self.style.configure("TSpinbox", fieldbackground=CARD_COLOR, foreground=TEXT_COLOR, padding=4)
        self.style.configure("TButton", padding=(10, 7), font=("Segoe UI", 9, "bold"), borderwidth=0)
        self.style.configure("Primary.TButton", background=PRIMARY_COLOR, foreground="white")
        self.style.configure("Success.TButton", background=SUCCESS_COLOR, foreground="white")
        self.style.configure("Danger.TButton", background=DANGER_COLOR, foreground="white")
        self.style.configure("Analytics.TButton", background=ANALYTICS_COLOR, foreground="white")
        self.style.map("Primary.TButton", background=[("active", PRIMARY_HOVER)])
        self.style.map("Success.TButton", background=[("active", SUCCESS_HOVER)])
        self.style.map("Danger.TButton", background=[("active", DANGER_HOVER)])
        self.style.map("Analytics.TButton", background=[("active", ANALYTICS_HOVER)])
        self.style.configure("Treeview", background=CARD_COLOR, foreground=TEXT_COLOR, rowheight=32, fieldbackground=CARD_COLOR, font=("Segoe UI", 9), borderwidth=0)
        self.style.configure("Treeview.Heading", background=TABLE_HEADER, foreground="white", font=("Segoe UI", 9, "bold"), padding=8)
        self.style.configure("Weak.Horizontal.TProgressbar", troughcolor="#dbeafe", background=DANGER_COLOR)
        self.style.configure("Moderate.Horizontal.TProgressbar", troughcolor="#dbeafe", background=WARNING_COLOR)
        self.style.configure("Strong.Horizontal.TProgressbar", troughcolor="#dbeafe", background=SUCCESS_COLOR)

    def create_interface(self):
        """Construct all GUI frames and controls."""
        header_frame = tk.Frame(self.root, bg=HEADER_COLOR, height=105)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        tk.Label(header_frame, text="PASSVAULT", bg=HEADER_COLOR, fg="white", font=("Segoe UI", 22, "bold")).pack(pady=(12, 3))
        tk.Label(header_frame, text="Password Generator | Credential Vault | Security Analytics", bg=HEADER_COLOR, fg="#D6E4F5", font=("Segoe UI", 10)).pack()

        main_frame = ttk.Frame(self.root, padding=18, style="App.TFrame")
        main_frame.pack(fill="both", expand=True)

        # Generator Frame
        generator_frame = tk.LabelFrame(main_frame, text="  Password Generator  ", font=("Segoe UI", 10, "bold"), bg=CARD_COLOR, fg=TEXT_COLOR, padx=15, pady=12, bd=1, relief="solid")
        generator_frame.pack(fill="x", pady=(0, 15))

        settings_frame = ttk.Frame(generator_frame)
        settings_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(settings_frame, text="Length:").pack(side="left")
        ttk.Spinbox(settings_frame, from_=8, to=32, textvariable=self.password_length, width=5).pack(side="left", padx=(8, 20))
        ttk.Checkbutton(settings_frame, text="Lowercase", variable=self.use_lowercase).pack(side="left", padx=5)
        ttk.Checkbutton(settings_frame, text="Uppercase", variable=self.use_uppercase).pack(side="left", padx=5)
        ttk.Checkbutton(settings_frame, text="Numbers", variable=self.use_numbers).pack(side="left", padx=5)
        ttk.Checkbutton(settings_frame, text="Symbols", variable=self.use_symbols).pack(side="left", padx=5)

        output_frame = ttk.Frame(generator_frame)
        output_frame.pack(fill="x")
        ttk.Label(output_frame, text="Generated Password:").pack(side="left")
        ttk.Entry(output_frame, textvariable=self.generated_password, width=32).pack(side="left", padx=(8, 10))
        ttk.Button(output_frame, text="Generate Password", style="Primary.TButton", command=self.generate_password).pack(side="left")

        strength_frame = ttk.Frame(generator_frame)
        strength_frame.pack(fill="x", pady=(10, 0))
        self.strength_label = ttk.Label(strength_frame, textvariable=self.password_strength, font=("Segoe UI", 9, "bold"))
        self.strength_label.pack(anchor="w", pady=(0, 3))
        self.strength_progress = ttk.Progressbar(strength_frame, length=400, mode="determinate")
        self.strength_progress.pack(fill="x")

        # Form Frame
        form_frame = tk.LabelFrame(main_frame, text="  Save Credential to Vault  ", font=("Segoe UI", 10, "bold"), bg=CARD_COLOR, fg=TEXT_COLOR, padx=15, pady=12, bd=1, relief="solid")
        form_frame.pack(fill="x", pady=(0, 15))

        inputs_frame = ttk.Frame(form_frame)
        inputs_frame.pack(fill="x")

        ttk.Label(inputs_frame, text="Account Name:").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(inputs_frame, textvariable=self.account_name, width=24).grid(row=0, column=1, sticky="w", padx=(5, 20), pady=4)

        ttk.Label(inputs_frame, text="Username/Email:").grid(row=0, column=2, sticky="w", pady=4)
        ttk.Entry(inputs_frame, textvariable=self.username_email, width=28).grid(row=0, column=3, sticky="w", padx=(5, 0), pady=4)

        ttk.Label(inputs_frame, text="Password:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Entry(inputs_frame, textvariable=self.credential_password, width=24).grid(row=1, column=1, sticky="w", padx=(5, 20), pady=4)

        ttk.Label(inputs_frame, text="Category:").grid(row=1, column=2, sticky="w", pady=4)
        categories = ["Email", "Work", "Social", "Banking", "Other"]
        ttk.Combobox(inputs_frame, textvariable=self.credential_category, values=categories, state="readonly", width=25).grid(row=1, column=3, sticky="w", padx=(5, 0), pady=4)

        ttk.Button(form_frame, text="Save Credential to Vault", style="Success.TButton", command=self.save_credential).pack(anchor="e", pady=(10, 0))

        # Vault Table Frame
        vault_frame = tk.LabelFrame(main_frame, text="  Stored Credentials Vault  ", font=("Segoe UI", 10, "bold"), bg=CARD_COLOR, fg=TEXT_COLOR, padx=15, pady=12, bd=1, relief="solid")
        vault_frame.pack(fill="both", expand=True)

        columns = ("id", "platform", "username", "password", "category", "strength", "created_date")
        self.credentials_table = ttk.Treeview(vault_frame, columns=columns, show="headings", height=6)
        self.credentials_table.heading("id", text="ID")
        self.credentials_table.heading("platform", text="Account Name")
        self.credentials_table.heading("username", text="Username/Email")
        self.credentials_table.heading("password", text="Password")
        self.credentials_table.heading("category", text="Category")
        self.credentials_table.heading("strength", text="Strength")
        self.credentials_table.heading("created_date", text="Created Date")

        self.credentials_table.column("id", width=40, anchor="center")
        self.credentials_table.column("platform", width=140)
        self.credentials_table.column("username", width=180)
        self.credentials_table.column("password", width=100, anchor="center")
        self.credentials_table.column("category", width=100, anchor="center")
        self.credentials_table.column("strength", width=100, anchor="center")
        self.credentials_table.column("created_date", width=110, anchor="center")
        self.credentials_table.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(vault_frame, orient="vertical", command=self.credentials_table.yview)
        self.credentials_table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Action Buttons
        actions_frame = ttk.Frame(main_frame)
        actions_frame.pack(fill="x", pady=(10, 0))
        ttk.Button(actions_frame, text="Reveal Selected Password", command=self.reveal_password).pack(side="left", padx=(0, 10))
        ttk.Button(actions_frame, text="Delete Selected Credential", style="Danger.TButton", command=self.delete_record).pack(side="left", padx=(0, 10))
        ttk.Button(actions_frame, text="View Security Analytics", style="Analytics.TButton", command=self.plot_analytics).pack(side="right")

    def generate_password(self):
        """Generate random password based on selected character sets."""
        try:
            length = int(self.password_length.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Password length must be an integer.")
            return

        character_pool = ""
        if self.use_lowercase.get():
            character_pool += string.ascii_lowercase
        if self.use_uppercase.get():
            character_pool += string.ascii_uppercase
        if self.use_numbers.get():
            character_pool += string.digits
        if self.use_symbols.get():
            character_pool += string.punctuation

        if not character_pool:
            messagebox.showwarning("Selection Required", "Select at least one character set.")
            return

        password = "".join(random.choice(character_pool) for _ in range(length))
        self.generated_password.set(password)
        self.credential_password.set(password)
        self.calculate_strength(password)

    def calculate_strength(self, password):
        """Evaluate rule-based password complexity score."""
        score = 0
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char in string.punctuation for char in password):
            score += 1

        if score <= 2:
            strength = "Weak"
            progress_value = 33
            style_name = "Weak.Horizontal.TProgressbar"
        elif score in (3, 4):
            strength = "Moderate"
            progress_value = 66
            style_name = "Moderate.Horizontal.TProgressbar"
        else:
            strength = "Strong"
            progress_value = 100
            style_name = "Strong.Horizontal.TProgressbar"

        self.strength_progress.configure(style=style_name)
        self.strength_progress["value"] = progress_value
        self.password_strength.set(f"Strength: {strength} ({score}/6 points)")
        return strength

    def save_credential(self):
        """Encode password string with Base64 and insert record into MySQL."""
        if not self.account_name.get().strip() or not self.username_email.get().strip():
            messagebox.showwarning("Input Required", "Fill in Account Name and Username/Email.")
            return

        password = self.credential_password.get()
        if not password:
            messagebox.showwarning("Input Required", "Password field cannot be empty.")
            return

        strength = self.calculate_strength(password)
        encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")

        connection = None
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            insert_query = """
                INSERT INTO credentials 
                (account_name, username_email, encrypted_password, category, strength_tier, created_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                self.account_name.get().strip(),
                self.username_email.get().strip(),
                encoded_password,
                self.credential_category.get(),
                strength,
                date.today(),
            )
            cursor = connection.cursor()
            cursor.execute(insert_query, values)
            connection.commit()
            cursor.close()
            messagebox.showinfo("Saved", "Credential saved successfully.")
            self.load_credentials()
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Could not save credential:\n{error}")
        finally:
            if connection is not None and connection.is_connected():
                connection.close()

    def load_credentials(self):
        """Query records from MySQL and update Treeview."""
        for row in self.credentials_table.get_children():
            self.credentials_table.delete(row)

        connection = None
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            query = "SELECT id, account_name, username_email, category, strength_tier, created_date FROM credentials ORDER BY id DESC"
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()

            for index, record in enumerate(records):
                record_id, platform, username, category, strength, created_date = record
                tag = "even" if index % 2 == 0 else "odd"
                self.credentials_table.insert(
                    "", "end", tags=(tag,),
                    values=(record_id, platform, username, "********", category, strength, created_date)
                )
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Could not load credentials:\n{error}")
        finally:
            if connection is not None and connection.is_connected():
                connection.close()

    def reveal_password(self):
        """Decode Base64 password representation for selected row."""
        selected_items = self.credentials_table.selection()
        if not selected_items:
            messagebox.showwarning("No Selection", "Select a credential record first.")
            return

        record_id = self.credentials_table.item(selected_items[0], "values")[0]

        connection = None
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            query = "SELECT encrypted_password FROM credentials WHERE id = %s"
            cursor = connection.cursor()
            cursor.execute(query, (record_id,))
            record = cursor.fetchone()
            cursor.close()

            if record:
                encoded_password = record[0]
                password = base64.b64decode(encoded_password).decode("utf-8")
                messagebox.showinfo(
                    "Decoded Password",
                    "Educational Demonstration Notice: Passwords are Base64 encoded.\n\n"
                    f"Decoded Password: {password}"
                )
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Could not retrieve password:\n{error}")
        finally:
            if connection is not None and connection.is_connected():
                connection.close()

    def delete_record(self):
        """Delete selected credential after confirmation."""
        selected_items = self.credentials_table.selection()
        if not selected_items:
            messagebox.showwarning("No Selection", "Select a credential record first.")
            return

        record_id = self.credentials_table.item(selected_items[0], "values")[0]

        if not messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this credential?"):
            return

        connection = None
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            query = "DELETE FROM credentials WHERE id = %s"
            cursor = connection.cursor()
            cursor.execute(query, (record_id,))
            connection.commit()
            cursor.close()
            messagebox.showinfo("Deleted", "Credential deleted successfully.")
            self.load_credentials()
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Could not delete credential:\n{error}")
        finally:
            if connection is not None and connection.is_connected():
                connection.close()

    def plot_analytics(self):
        """Process data with Pandas and render Matplotlib charts."""
        connection = None
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            query = "SELECT category, strength_tier FROM credentials"
            dataframe = pd.read_sql(query, connection)

            if dataframe.empty:
                messagebox.showinfo("No Data", "Add credentials before viewing analytics.")
                return

            category_counts = dataframe["category"].value_counts()
            strength_counts = dataframe["strength_tier"].value_counts()

            figure, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
            ax1.bar(category_counts.index, category_counts.values, color=PRIMARY_COLOR)
            ax1.set_title("Vault Accounts by Category", fontweight="bold")
            ax1.set_xlabel("Category")
            ax1.set_ylabel("Number of Accounts")

            ax2.pie(
                strength_counts.values,
                labels=strength_counts.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=[DANGER_COLOR, WARNING_COLOR, SUCCESS_COLOR],
            )
            ax2.set_title("Password Strength Distribution", fontweight="bold")

            figure.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Analytics Error", f"Could not generate analytics:\n{error}")
        finally:
            if connection is not None and connection.is_connected():
                connection.close()

def main():
    root = tk.Tk()
    app = PassVaultApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

---

## 14. RESULTS AND OUTCOMES

The development of **PassVault** yielded the following successful outcomes:
1. **Functional Password Generator:** Successfully generates customizable random passwords across user-defined lengths (8 to 32 characters).
2. **Rule-Based Complexity Evaluator:** Accurately computes character complexity scores (0 to 6 points) and provides immediate visual feedback.
3. **Reliable SQL Integration:** Successfully connects to MySQL Server (`passvault_db`), executing parameterized SQL statements to store and retrieve records cleanly.
4. **Data Masking & Privacy:** Ensures sensitive passwords are masked (`********`) in public table views while offering single-click on-demand Base64 decoding.
5. **Data Analytics Dashboard:** Integrates `Pandas` and `Matplotlib` to render informative, real-time bar and pie charts representing vault demographics.

---

## 15. LIMITATIONS

While PassVault fulfills all core educational requirements of a senior school project, the following limitations exist:
1. **Demonstration Encoding:** PassVault utilizes Base64 encoding for educational storage demonstration. Base64 is representation encoding and does not provide cryptographic encryption.
2. **Local Single-User Architecture:** The application connects to a local database (`localhost`) and does not support multi-tenant cloud synchronization.
3. **Unauthenticated Master Interface:** There is currently no master login screen required upon application launch.

---

## 16. FUTURE SCOPE

To enhance PassVault for production or commercial deployment, the following upgrades are planned:
1. **Authenticated Cryptographic Encryption:** Replace Base64 encoding with a proper authenticated encryption scheme (such as AES-GCM or Fernet) using PBKDF2 key derivation.
2. **Master Password Login:** Implement a bcrypt-hashed master login screen to authenticate users before granting access to the vault.
3. **Browser Extension Integration:** Create Chrome/Firefox extensions to automatically auto-fill stored credentials on web pages.
4. **Cloud Database Sync:** Add support for encrypted cloud backups via Amazon AWS RDS or Google Cloud SQL.

---

## 17. CONCLUSION & LEARNING OUTCOMES

### Conclusion
The **PassVault** project successfully demonstrates the integration of Python desktop GUI development (`tkinter`/`ttk`), relational database management (MySQL), algorithmic complexity evaluation, and data visualization (`Pandas`/`Matplotlib`).

### Learning Outcomes
After completing this project, I gained practical hands-on experience in:
- Designing desktop User Interfaces using Python's `tkinter` and `ttk` modules.
- Establishing database pipelines between Python and MySQL using `mysql-connector-python`.
- Executing parameterized SQL statements (`INSERT`, `SELECT`, `DELETE`) safely.
- Designing relational database schemas using Primary Key and constraint rules.
- Applying defensive programming techniques and exception handling (`try-except-finally`).
- Implementing rule-based algorithmic scoring for password complexity evaluation.
- Processing SQL result sets into `Pandas` DataFrames and aggregating counts via `value_counts()`.
- Rendering comparative graphical charts using `Matplotlib`.
- Distinguishing between data representation encoding (Base64) and cryptographic encryption.
- Validating user inputs to build robust, reliable software applications.

---

## 18. BIBLIOGRAPHY & REFERENCES

1. **Python Official Documentation:** Python Software Foundation. *Tkinter — Python interface to Tcl/Tk*. Available at: https://docs.python.org/3/library/tkinter.html
2. **MySQL Connector Guide:** Oracle Corporation. *MySQL Connector/Python Developer Guide*. Available at: https://dev.mysql.com/doc/connector-python/en/
3. **Pandas Documentation:** PyData Development Team. *Pandas: Data Analysis Library*. Available at: https://pandas.pydata.org/
4. **Matplotlib Documentation:** John D. Hunter et al. *Matplotlib: Visualization with Python*. Available at: https://matplotlib.org/
5. **NCERT Computer Science Textbook:** National Council of Educational Research and Training. *Class XII Computer Science (Subject Code 083) Textbook*.
6. **CBSE Class 12 Computer Science Curriculum:** Central Board of Secondary Education. *Computer Science Practical Examination Guidelines (2026–2027)*.

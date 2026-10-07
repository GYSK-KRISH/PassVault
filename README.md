<div align="center">

# 🔐 PASSVAULT
### *Credential Manager & Security Analytics Desktop System*

![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![GUI Framework](https://img.shields.io/badge/GUI-Tkinter%20%2F%20ttk-FF6F00?style=for-the-badge&logo=python&logoColor=white)
![Data Analytics](https://img.shields.io/badge/Analytics-Pandas%20%26%20Matplotlib-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<p align="center">
  <b>PassVault</b> is a localized desktop management system built with Python, Tkinter, and MySQL. It empowers users to generate high-entropy passwords, securely record credentials, evaluate real-time password strength, and visualize vault security demographics through data analytics.
</p>

[Quick Start](#-quick-start) • [Key Features](#-key-features) • [System Architecture](#-system-architecture) • [Database Schema](#-database-schema) • [Troubleshooting](#-troubleshooting)

</div>

---

## 📌 Executive Summary

**PassVault** bridges the gap between strong cybersecurity practices and user convenience. In modern digital environments, users face severe **Password Fatigue**, leading to weak password choices and dangerous cross-account password reuse. 

PassVault resolves this challenge by delivering a localized desktop solution that:
* 🎲 **Generates high-entropy random passwords** with custom length and character variety parameters.
* 📊 **Evaluates password strength real-time** using rule-based scoring and dynamic progress indicators.
* 🗄️ **Stores credentials in a relational database** using MySQL (`passvault_db`).
* 🙈 **Protects privacy with masked UI fields** (`********`) and on-demand password revealing.
* 📈 **Visualizes security statistics** with interactive Pandas dataframes and Matplotlib side-by-side charts.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| ⚡ **Password Generator** | Generates 8 to 32-character complex passwords with custom lowercase, uppercase, numeric, and special symbol toggles. |
| 🛡️ **Real-time Security Analyzer** | Evaluates entropy complexity, categorizes passwords into **Weak**, **Moderate**, or **Strong** tiers, and updates progress bars dynamically. |
| 🗃️ **Relational Credential Vault** | Stores credentials with fields for Platform/Account, Username/Email, Encoded Password, Category, Strength Tier, and Date. |
| 👁️ **Data Privacy & Masking** | Conceals password strings in table views with a single-click **Reveal** option for authorized verification. |
| 📊 **Security Analytics Dashboard** | Aggregates vault data using Pandas and renders Matplotlib bar charts (Category breakdown) and pie charts (Strength ratios). |
| 🛠️ **Built-in Connection Tester** | Includes `test_connection.py` to instantly verify MySQL password and database setup before launching. |

---

## 🛠️ Technology Stack

```text
               +-------------------------------------------------------+
               |                    PASSVAULT GUI                      |
               |                (Tkinter / ttk Themes)                 |
               +---------------------------+---------------------------+
                                           |
                    +----------------------+----------------------+
                    |                                             |
       +------------v------------+                   +------------v------------+
       |   Security & Logic      |                   |    Data Science Stack   |
       |  (Python Standard Lib)  |                   |   (Pandas & Matplotlib) |
       +------------+------------+                   +------------+------------+
                    |                                             |
                    +----------------------+----------------------+
                                           |
                               +-----------v-----------+
                               |     MySQL Database    |
                               | (mysql-connector-py)  |
                               +-----------------------+
```

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core application logic and execution runtime. |
| **GUI Framework** | Tkinter / ttk (`clam` theme) | Native desktop layout, treeview tables, styled dialogs. |
| **Database Engine** | MySQL Server 8.0+ | Relational storage for credential records. |
| **DB Driver** | `mysql-connector-python` | Parameterized SQL query execution and database connectivity. |
| **Data Analytics** | Pandas | Data manipulation, filtering, and `value_counts()` aggregation. |
| **Visualization** | Matplotlib (`pyplot`) | Rendering side-by-side bar charts and pie graphs. |

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have installed:
* [Python 3.10+](https://www.python.org/downloads/) (with *Add Python to PATH* enabled)
* [MySQL Server](https://dev.mysql.com/downloads/installer/) & [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

### 2. Install Python Dependencies
Open your PowerShell or Command Prompt terminal in the project directory and run:

```powershell
python -m pip install -r requirements.txt
```

### 3. Initialize the MySQL Database
1. Open MySQL Workbench and log into your local server instance.
2. Open [database.sql](database.sql) and execute the complete script (click the **Lightning Bolt** icon).
3. This creates the database `passvault_db` and table `credentials`.

### 4. Test & Run the Application
Set your local MySQL password in PowerShell and launch `app.py`:

```powershell
# Set your local MySQL password
$env:PASSVAULT_DB_HOST = "localhost"
$env:PASSVAULT_DB_USER = "root"
$env:PASSVAULT_DB_PASSWORD = "YOUR_MYSQL_PASSWORD"
$env:PASSVAULT_DB_NAME = "passvault_db"

# Optional: Run the automated connection tester
python test_connection.py

# Launch PassVault Desktop Application
python app.py
```

---

## 🗄️ Database Schema

### Database: `passvault_db` | Table: `credentials`

| Field | Type | Nullable | Key / Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `INT` | No | **PRIMARY KEY** (Auto Increment) | Unique identification key. |
| **`account_name`** | `VARCHAR(100)` | No | None | Platform name (e.g. GitHub, Google). |
| **`username_email`**| `VARCHAR(120)` | No | None | User's account login handle or email. |
| **`encrypted_password`**| `VARCHAR(255)`| No | None | Base64-encoded password string. |
| **`category`** | `VARCHAR(50)` | No | `'Other'` | Category (*Email, Work, Social, Banking, Other*). |
| **`strength_tier`**| `VARCHAR(20)` | No | None | Security rating (*Weak, Moderate, Strong*). |
| **`created_date`** | `DATE` | No | None | Date timestamp (`YYYY-MM-DD`). |

---

## 📂 Project Directory Structure

```text
PassVault/
├── 📄 app.py                  # Main application entry point & Tkinter GUI
├── 📄 test_connection.py      # Interactive MySQL database connection tester
├── 📄 database.sql            # MySQL database schema initialization script
├── 📄 requirements.txt        # Python package dependencies
├── 📄 SCHOOL_SETUP.md         # Step-by-step school computer setup guide
├── 📄 PROJECT_REPORT.md       # Complete 25-section CBSE Computer Science Project Report
├── 📄 SECURITY_REVIEW.md      # Security analysis & educational disclaimer document
└── 📄 README.md               # Project documentation homepage
```

---

## ⚠️ Important Educational Security Disclaimer

> [!IMPORTANT]
> **Classroom Demonstration Project Notice:** PassVault is designed as a Class 12 Computer Science project to demonstrate GUI development, SQL integration, and data visualization. Passwords in this project are stored using **Base64 encoding** for classroom presentation simplicity. 
> 
> Base64 is an **encoding format**, not cryptographic encryption. A production-grade password manager requires AES-256 authenticated encryption, master password key derivation (PBKDF2), and secure key storage.

---

## ❓ Troubleshooting & FAQs

| Problem | Cause | Solution |
| :--- | :--- | :--- |
| **`python is not recognized`** | Python is not added to system PATH. | Re-install Python and check **Add Python to PATH**. |
| **`Access denied for user 'root'@'localhost'`** | Incorrect MySQL root password. | Run `python test_connection.py` to test your password interactively. |
| **`Unknown database 'passvault_db'`** | Database script not executed. | Open `database.sql` in MySQL Workbench and click the execute lightning bolt. |
| **`Can't connect to MySQL server`** | MySQL Service is stopped. | Start the MySQL service from Windows Services or MySQL Workbench. |
| **Browser tab opens displaying nothing** | Visual Studio Code Live Server extension. | Close the browser tab. PassVault is a **Tkinter Desktop App** (look for the window on your taskbar). |

---

## 📜 Documentation Links

* 📑 **[PROJECT_REPORT.md](PROJECT_REPORT.md)** — Complete 25-section CBSE Senior School Computer Science Project Report.
* 🏫 **[SCHOOL_SETUP.md](SCHOOL_SETUP.md)** — Step-by-step installation guide for school computer labs.
* 🔒 **[SECURITY_REVIEW.md](SECURITY_REVIEW.md)** — In-depth architectural security review and analysis.

---

<div align="center">
  <sub>Developed for Senior Secondary Computer Science Demonstration • Built with ❤️ using Python & MySQL</sub>
</div>

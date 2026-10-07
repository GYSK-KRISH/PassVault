# PASSVAULT: Setup & Troubleshooting Guide

Use these steps to set up, configure, and run **PassVault** on a local computer or school lab machine.

> [!IMPORTANT]
> **Application Type Notice:** PassVault is a **Python Tkinter Desktop Window Application**, NOT a web app. When you run `python app.py`, it launches a native desktop window on your screen/taskbar. It does **not** host a web server or open a browser tab.

---

## Quick Setup Steps

### 1. Copy the Project Files
Ensure all project files are kept together in your workspace folder:
- `app.py`
- `database.sql`
- `requirements.txt`
- `test_connection.py`

### 2. Verify Python 3 Installation
Ensure Python 3 is installed and added to your system PATH. Test it in PowerShell:

```powershell
python --version
```

### 3. Open PowerShell in VS Code
In VS Code, open the project folder and open a new terminal (**Terminal > New Terminal**). Ensure the terminal path points to the project folder.

### 4. Install Required Python Packages
Run the following command to install the required libraries (`mysql-connector-python`, `pandas`, `matplotlib`):

```powershell
python -m pip install -r requirements.txt
```

*(Note: `tkinter` comes pre-installed with standard Python distributions on Windows).*

### 5. Start MySQL Server & Import Database
1. Make sure your local MySQL service is running (via MySQL Workbench or Windows Services).
2. Open `database.sql` in **MySQL Workbench** and execute the entire script (click the **Lightning Bolt** icon).
3. This creates the database `passvault_db` and the `credentials` table.

### 6. Configure MySQL Environment Variables
Set your local MySQL credentials in your PowerShell terminal before launching the application:

```powershell
$env:PASSVAULT_DB_HOST = "localhost"
$env:PASSVAULT_DB_USER = "root"
$env:PASSVAULT_DB_PASSWORD = "YOUR_MYSQL_PASSWORD"
$env:PASSVAULT_DB_NAME = "passvault_db"
```

> **Note:** Replace `YOUR_MYSQL_PASSWORD` with your actual MySQL Workbench password.

### 7. Test Database Connection
Run the connection helper script to verify your database settings before launching the GUI:

```powershell
python test_connection.py
```

If successful, you will see `SUCCESS! Connected to database 'passvault_db'` and `'credentials' table is present and ready!`.

### 8. Run the Application
In the same terminal window, launch the app:

```powershell
python app.py
```

Check your Windows desktop or taskbar for the window titled **PassVault | Credential Manager & Security Analyzer**.

---

## Common Configuration Scenarios

| Environment | Variable Setup |
| :--- | :--- |
| **Default (Local Machine)** | `$env:PASSVAULT_DB_PASSWORD = "your_mysql_password"` |
| **Custom User** | `$env:PASSVAULT_DB_USER = "school_user"` |
| **Remote Host** | `$env:PASSVAULT_DB_HOST = "192.168.1.100"` |

---

## Common Errors & Troubleshooting

- **`python is not recognized`**: Python is not installed or was not added to system PATH. Re-install Python and select *Add Python to PATH*.
- **`No module named mysql`**: Re-run `python -m pip install -r requirements.txt`.
- **`Access denied for user 'root'@'localhost'`**: The MySQL password set in `$env:PASSVAULT_DB_PASSWORD` is incorrect or missing. Run `python test_connection.py` to test your password interactively.
- **`Unknown database 'passvault_db'`**: Run `database.sql` in MySQL Workbench to create the database schema.
- **`Can't connect to MySQL server`**: Ensure the MySQL service is started in Windows Services or MySQL Workbench.
- **Browser tab opens but displays nothing**: Close the browser tab. `PassVault` is a native desktop window app, not a web page. Look for the window on your taskbar.

---

## Presentation & Demonstration Notes

1. **Security Disclaimer**: This project uses Base64 encoding for educational demonstration purposes. Base64 is encoding, not cryptographic encryption. Always use sample/dummy usernames and passwords for school demonstrations.
2. **Clean Up**: Before submitting or presenting your project, delete test credentials and ensure no real passwords or secret database credentials remain hardcoded in `app.py`.

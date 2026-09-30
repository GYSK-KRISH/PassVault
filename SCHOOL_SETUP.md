# PASSVAULT: School Computer Setup

Use these 10 steps on the school computer. You need permission to install Python packages and MySQL. If the school computer is restricted, ask the teacher or lab administrator to perform the installation steps.

## 10 Steps

1. **Copy the project folder**

   Copy the complete project folder to the school computer. Keep these files together:

   - `app.py`
   - `database.sql`
   - `requirements.txt`

2. **Install Python 3**

   Install Python 3 from the approved school software source. During installation, enable **Add Python to PATH** if that option is available.

   Test it in PowerShell:

   ```powershell
   python --version
   ```

3. **Open PowerShell in the project folder**

   In VS Code, open the project folder. Then open **Terminal > New Terminal**. The terminal path should end with the project folder name.

4. **Install the Python packages**

   Run:

   ```powershell
   python -m pip install -r requirements.txt
   ```

   This installs MySQL Connector, Pandas, and Matplotlib. Tkinter normally comes with Python on Windows.

5. **Install or start MySQL Server**

   Start the MySQL service from MySQL Workbench or Windows Services. The service must be running before PASSVAULT can connect.

   The default local host is `localhost` and the default MySQL user in this project is `root`.

6. **Create the database**

   Open `database.sql` in MySQL Workbench and execute the complete script. It creates the database `passvault_db` and the table `credentials`.

7. **Find the school MySQL password**

   Ask the teacher or lab administrator for the MySQL password for the school computer. Do not guess it and do not publish it in the project files.

8. **Configure the school MySQL settings**

   Do not write the MySQL password inside `app.py`. Set these environment variables in the same PowerShell window before starting the application:

   ```powershell
   $env:PASSVAULT_DB_HOST = "localhost"
   $env:PASSVAULT_DB_USER = "root"
   $env:PASSVAULT_DB_PASSWORD = "SCHOOL_MYSQL_PASSWORD"
   $env:PASSVAULT_DB_NAME = "passvault_db"
   ```

   Replace `SCHOOL_MYSQL_PASSWORD` with the real local MySQL password. If the school gives you a different username or host, change those values too. These settings last for the current PowerShell window only.

9. **Test the application**

   Run:

   ```powershell
   python app.py
   ```

   Generate a test password, save a dummy credential, refresh the table, and open analytics. Use fake data only for a school demonstration.

10. **Clean up before presenting or submitting**

    Delete test records containing personal information. Do not submit or share the real MySQL password. If `app.py` contains a school password, replace it with a placeholder before sharing the project outside the school computer.

## What normally changes at school?

Usually, only this environment variable changes:

```powershell
$env:PASSVAULT_DB_PASSWORD = "SCHOOL_MYSQL_PASSWORD"
```

If MySQL was installed with another account, also change:

```powershell
$env:PASSVAULT_DB_USER = "school_mysql_user"
```

If MySQL is running on another computer, change:

```powershell
$env:PASSVAULT_DB_HOST = "computer-name-or-ip"
```

For a normal single-computer setup, keep `host` as `localhost`.

## Common errors

- **`python is not recognized`**: Python is not installed or was not added to PATH. Reopen VS Code after installation, or use the full Python executable path.
- **`No module named mysql`**: Run `python -m pip install -r requirements.txt` again.
- **`Unknown database 'passvault_db'`**: Execute `database.sql` in MySQL Workbench.
- **`Access denied for user`**: Check the MySQL username and password in `DB_CONFIG`.
- **`Can't connect to MySQL server`**: Start the MySQL service and try again.
- **The window opens but charts fail**: Save at least one dummy credential before selecting **View Analytics**.

## Important school safety note

This is a classroom demonstration. The project uses Base64 encoding, which is not encryption. Use dummy usernames, emails, and passwords during the demonstration.

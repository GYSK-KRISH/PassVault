import base64
import binascii
from datetime import date
import os
import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import random
import string
from tkinter import ttk
from tkinter import messagebox


# PASSVAULT professional color theme
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
MUTED_COLOR = "#244A7C"
TEXT_COLOR = "#172B4D"
MUTED_TEXT_COLOR = "#5B6B82"
BORDER_COLOR = "#B8D4F5"
SECTION_COLOR = "#E5F0FF"
INPUT_BORDER = "#C7D3E3"
TABLE_HEADER = "#173F73"
TABLE_ALT = "#F8FAFC"
TABLE_SELECTED = "#DCEBFF"


DB_CONFIG = {
	"host": os.getenv("PASSVAULT_DB_HOST", "localhost"),
	"user": os.getenv("PASSVAULT_DB_USER", "root"),
	"password": os.getenv("PASSVAULT_DB_PASSWORD", ""),
	"database": os.getenv("PASSVAULT_DB_NAME", "passvault_db"),
}


class PassVaultApp:
	"""Main window for the PASSVAULT desktop application."""

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

	def configure_styles(self):
		"""Configure the complete PASSVAULT visual theme."""
		self.style = ttk.Style(self.root)
		self.style.theme_use("clam")
		self.style.configure("App.TFrame", background=BG_COLOR)
		self.style.configure("TFrame", background=CARD_COLOR)
		self.style.configure("TLabel", background=CARD_COLOR, foreground=TEXT_COLOR,
			font=("Segoe UI", 9))
		self.style.configure("TCheckbutton", background=CARD_COLOR, foreground=TEXT_COLOR,
			font=("Segoe UI", 9))
		self.style.configure("TEntry", fieldbackground=CARD_COLOR, foreground=TEXT_COLOR,
			padding=5)
		self.style.configure("TCombobox", fieldbackground=CARD_COLOR, background=CARD_COLOR,
			foreground=TEXT_COLOR, padding=4)
		self.style.configure("TSpinbox", fieldbackground=CARD_COLOR, foreground=TEXT_COLOR,
			padding=4)
		self.style.configure("TButton", padding=(10, 7), font=("Segoe UI", 9, "bold"),
			borderwidth=0)
		self.style.configure("Primary.TButton", background=PRIMARY_COLOR, foreground="white")
		self.style.configure("Success.TButton", background=SUCCESS_COLOR, foreground="white")
		self.style.configure("Danger.TButton", background=DANGER_COLOR, foreground="white")
		self.style.configure("Muted.TButton", background=MUTED_COLOR, foreground="white")
		self.style.configure("Analytics.TButton", background=ANALYTICS_COLOR, foreground="white")
		self.style.map("Primary.TButton", background=[("active", PRIMARY_HOVER)])
		self.style.map("Success.TButton", background=[("active", SUCCESS_HOVER)])
		self.style.map("Danger.TButton", background=[("active", DANGER_HOVER)])
		self.style.map("Muted.TButton", background=[("active", TABLE_HEADER)])
		self.style.map("Analytics.TButton", background=[("active", ANALYTICS_HOVER)])
		self.style.configure("Treeview", background=CARD_COLOR, foreground=TEXT_COLOR,
			rowheight=32, fieldbackground=CARD_COLOR, font=("Segoe UI", 9), borderwidth=0)
		self.style.configure("Treeview.Heading", background=TABLE_HEADER,
			foreground="white", font=("Segoe UI", 9, "bold"), padding=8)
		self.style.map("Treeview", background=[("selected", TABLE_SELECTED)],
			foreground=[("selected", TEXT_COLOR)])
		self.style.configure("Weak.Horizontal.TProgressbar", troughcolor="#dbeafe",
			background=DANGER_COLOR)
		self.style.configure("Moderate.Horizontal.TProgressbar", troughcolor="#dbeafe",
			background=WARNING_COLOR)
		self.style.configure("Strong.Horizontal.TProgressbar", troughcolor="#dbeafe",
			background=SUCCESS_COLOR)

	def create_interface(self):
		header_frame = tk.Frame(self.root, bg=HEADER_COLOR, height=105)
		header_frame.pack(fill="x")
		header_frame.pack_propagate(False)

		title_label = tk.Label(
			header_frame,
			text="PASSVAULT",
			bg=HEADER_COLOR,
			fg="white",
			font=("Segoe UI", 22, "bold"),
		)
		title_label.pack(pady=(12, 3))

		subtitle_label = tk.Label(
			header_frame,
			text="Password Generator | Credential Vault | Security Analytics",
			bg=HEADER_COLOR,
			fg="#D6E4F5",
			font=("Segoe UI", 10),
		)
		subtitle_label.pack()

		tk.Label(
			header_frame,
			text="Stronger Passwords  |  Safer Accounts  |  Better Security",
			background=HEADER_COLOR,
			foreground="#D6E4F5",
			font=("Segoe UI", 8),
		).pack(anchor="e", padx=22, pady=(0, 4))

		main_frame = ttk.Frame(self.root, padding=18, style="App.TFrame")
		main_frame.pack(fill="both", expand=True)

		generator_frame = tk.LabelFrame(
			main_frame,
			text="  Password Generator  ",
			font=("Segoe UI", 10, "bold"),
			bg=CARD_COLOR,
			fg=TEXT_COLOR,
			padx=15,
			pady=12,
			bd=1,
			relief="solid",
			highlightbackground=BORDER_COLOR,
			highlightcolor=BORDER_COLOR,
		)
		generator_frame.pack(fill="x", pady=(0, 15))

		settings_frame = ttk.Frame(generator_frame)
		settings_frame.pack(fill="x", pady=(0, 10))
		ttk.Label(settings_frame, text="Length:").pack(side="left")
		ttk.Spinbox(
			settings_frame,
			from_=8,
			to=32,
			textvariable=self.password_length,
			width=5,
		).pack(side="left", padx=(8, 20))

		ttk.Checkbutton(
			settings_frame,
			text="Lowercase",
			variable=self.use_lowercase,
		).pack(side="left", padx=5)
		ttk.Checkbutton(
			settings_frame,
			text="Uppercase",
			variable=self.use_uppercase,
		).pack(side="left", padx=5)
		ttk.Checkbutton(
			settings_frame,
			text="Numbers",
			variable=self.use_numbers,
		).pack(side="left", padx=5)
		ttk.Checkbutton(
			settings_frame,
			text="Symbols",
			variable=self.use_symbols,
		).pack(side="left", padx=5)

		output_frame = ttk.Frame(generator_frame)
		output_frame.pack(fill="x")
		ttk.Label(output_frame, text="Generated Password:").pack(side="left")
		ttk.Entry(
			output_frame,
			textvariable=self.generated_password,
			width=38,
		).pack(side="left", padx=8, fill="x", expand=True)
		ttk.Button(
			output_frame,
			text="Generate Password",
			command=self.generate_password,
			style="Primary.TButton",
		).pack(side="left", padx=4)
		ttk.Button(
			output_frame,
			text="Copy",
			command=self.copy_password,
			style="Muted.TButton",
		).pack(side="left", padx=4)
		ttk.Button(
			output_frame,
			text="Analyze Strength",
			command=self.analyze_password_strength,
			style="Analytics.TButton",
		).pack(side="left", padx=4)

		self.strength_label = tk.Label(
			generator_frame,
			textvariable=self.password_strength,
			font=("Segoe UI", 10, "bold"),
			bg=CARD_COLOR,
			fg=MUTED_COLOR,
			anchor="w",
		)
		self.strength_label.pack(fill="x", pady=(10, 0))
		self.strength_progress = ttk.Progressbar(
			generator_frame,
			maximum=6,
			value=0,
			style="Strong.Horizontal.TProgressbar",
		)
		self.strength_progress.pack(fill="x", pady=(6, 0))

		credential_frame = tk.LabelFrame(
			main_frame,
			text="  Save Credential  ",
			font=("Segoe UI", 10, "bold"),
			bg=CARD_COLOR,
			fg=TEXT_COLOR,
			padx=15,
			pady=12,
			bd=1,
			relief="solid",
			highlightbackground=BORDER_COLOR,
			highlightcolor=BORDER_COLOR,
		)
		credential_frame.pack(fill="x", pady=(0, 15))

		ttk.Label(credential_frame, text="Account / Platform:").grid(
			row=0,
			column=0,
			sticky="w",
			padx=(0, 8),
			pady=4,
		)
		account_entry = ttk.Entry(
			credential_frame,
			textvariable=self.account_name,
			width=30,
		)
		account_entry.grid(row=0, column=1, sticky="ew", pady=4)
		account_entry.bind("<Return>", lambda event: self.save_credential())

		ttk.Label(credential_frame, text="Username / Email:").grid(
			row=1,
			column=0,
			sticky="w",
			padx=(0, 8),
			pady=4,
		)
		username_entry = ttk.Entry(
			credential_frame,
			textvariable=self.username_email,
			width=30,
		)
		username_entry.grid(row=1, column=1, sticky="ew", pady=4)
		username_entry.bind("<Return>", lambda event: self.save_credential())

		ttk.Label(credential_frame, text="Password:").grid(
			row=2,
			column=0,
			sticky="w",
			padx=(0, 8),
			pady=4,
		)
		credential_password_entry = ttk.Entry(
			credential_frame,
			textvariable=self.credential_password,
			show="*",
			width=30,
		)
		credential_password_entry.grid(row=2, column=1, sticky="ew", pady=4)
		credential_password_entry.bind("<Return>", lambda event: self.save_credential())

		ttk.Label(credential_frame, text="Category:").grid(
			row=3,
			column=0,
			sticky="w",
			padx=(0, 8),
			pady=4,
		)
		category_box = ttk.Combobox(
			credential_frame,
			textvariable=self.credential_category,
			values=("Social", "Work", "Education", "Finance", "Gaming", "Other"),
			state="readonly",
			width=27,
		)
		category_box.grid(row=3, column=1, sticky="ew", pady=4)
		category_box.bind("<Return>", lambda event: self.save_credential())

		button_frame = ttk.Frame(credential_frame)
		button_frame.grid(row=0, column=2, rowspan=4, padx=(20, 0))
		ttk.Button(
			button_frame,
			text="Save Credential",
			command=self.save_credential,
			style="Success.TButton",
		).pack(fill="x", pady=3)
		ttk.Button(
			button_frame,
			text="Clear Form",
			command=self.clear_credential_form,
			style="Muted.TButton",
		).pack(fill="x", pady=3)
		credential_frame.columnconfigure(1, weight=1)

		records_frame = tk.LabelFrame(
			main_frame,
			text="  Saved Credentials  ",
			font=("Segoe UI", 10, "bold"),
			bg=CARD_COLOR,
			fg=TEXT_COLOR,
			padx=15,
			pady=12,
			bd=1,
			relief="solid",
			highlightbackground=BORDER_COLOR,
			highlightcolor=BORDER_COLOR,
		)
		records_frame.pack(fill="both", expand=True)

		table_frame = ttk.Frame(records_frame)
		table_frame.pack(fill="both", expand=True)

		columns = (
			"id",
			"platform",
			"username",
			"password",
			"category",
			"strength",
			"date",
		)
		self.credentials_table = ttk.Treeview(
			table_frame,
			columns=columns,
			show="headings",
			height=8,
		)
		self.empty_table_label = tk.Label(
			table_frame,
			text="No credentials saved yet\nSave your first credential to get started",
			bg=CARD_COLOR,
			fg=MUTED_COLOR,
			font=("Segoe UI", 10, "bold"),
			justify="center",
		)
		headings = {
			"id": "ID",
			"platform": "Platform",
			"username": "Username",
			"password": "Password",
			"category": "Category",
			"strength": "Strength",
			"date": "Date",
		}
		widths = {
			"id": 45,
			"platform": 135,
			"username": 180,
			"password": 100,
			"category": 95,
			"strength": 85,
			"date": 95,
		}
		for column in columns:
			self.credentials_table.heading(column, text=headings[column])
			self.credentials_table.column(column, width=widths[column], anchor="center")
		self.credentials_table.column("platform", width=140, anchor="w")
		self.credentials_table.column("username", width=190, anchor="w")
		self.credentials_table.column("password", width=150, anchor="center")
		self.credentials_table.column("category", width=110, anchor="center")
		self.credentials_table.column("strength", width=100, anchor="center")
		self.credentials_table.column("date", width=110, anchor="center")
		self.credentials_table.tag_configure("even", background=TABLE_ALT)
		self.credentials_table.tag_configure("odd", background=CARD_COLOR)

		table_scrollbar = ttk.Scrollbar(
			table_frame,
			orient="vertical",
			command=self.credentials_table.yview,
		)
		self.credentials_table.configure(yscrollcommand=table_scrollbar.set)
		self.credentials_table.pack(side="left", fill="both", expand=True)
		table_scrollbar.pack(side="right", fill="y")

		action_frame = ttk.Frame(records_frame)
		action_frame.pack(anchor="e", pady=(10, 0))
		ttk.Button(
			action_frame,
			text="Reveal Password",
			command=self.reveal_password,
			style="Primary.TButton",
		).pack(side="left", padx=3)
		ttk.Button(
			action_frame,
			text="Delete Record",
			command=self.delete_record,
			style="Danger.TButton",
		).pack(side="left", padx=3)
		ttk.Button(
			action_frame,
			text="Refresh Table",
			command=self.load_credentials,
			style="Muted.TButton",
		).pack(side="left", padx=3)
		ttk.Button(
			action_frame,
			text="View Analytics",
			command=self.plot_analytics,
			style="Analytics.TButton",
		).pack(side="left", padx=3)

		self.status_label = tk.Label(
			self.root,
			text="Ready",
			anchor="w",
			bg=HEADER_COLOR,
			fg="#D6E4F5",
			font=("Segoe UI", 8),
			padx=12,
			pady=4,
		)
		self.status_label.pack(fill="x", side="bottom")
		self.load_credentials()

	def generate_password(self):
		"""Generate a password using the selected character categories."""
		try:
			length = int(self.password_length.get())
		except ValueError:
			messagebox.showerror("Invalid Length", "Enter a whole number from 8 to 32.")
			return

		if length < 8 or length > 32:
			messagebox.showerror("Invalid Length", "Password length must be from 8 to 32.")
			return

		selected_sets = []
		if self.use_lowercase.get():
			selected_sets.append(string.ascii_lowercase)
		if self.use_uppercase.get():
			selected_sets.append(string.ascii_uppercase)
		if self.use_numbers.get():
			selected_sets.append(string.digits)
		if self.use_symbols.get():
			selected_sets.append(string.punctuation)

		if not selected_sets:
			messagebox.showerror(
				"No Character Type",
				"Select at least one character category.",
			)
			return

		if length < len(selected_sets):
			messagebox.showerror(
				"Invalid Length",
				"The selected length is too short for all chosen categories.",
			)
			return

		password_characters = [random.choice(characters) for characters in selected_sets]
		all_characters = "".join(selected_sets)
		password_characters.extend(
			random.choice(all_characters)
			for _ in range(length - len(password_characters))
		)
		random.shuffle(password_characters)

		password = "".join(password_characters)
		self.generated_password.set(password)
		self.update_strength_display(password)
		self.status_label.configure(text="Password generated successfully.")

	def evaluate_password_strength(self, password):
		"""Return a simple strength tier based on understandable rules."""
		score = 0

		if len(password) >= 8:
			score += 1
		if len(password) >= 12:
			score += 1
		if any(character.islower() for character in password):
			score += 1
		if any(character.isupper() for character in password):
			score += 1
		if any(character.isdigit() for character in password):
			score += 1
		if any(character in string.punctuation for character in password):
			score += 1

		if score >= 5:
			return "Strong"
		if score >= 3:
			return "Moderate"
		return "Weak"

	def update_strength_display(self, password):
		"""Display the strength tier with a matching color."""
		strength = self.evaluate_password_strength(password)
		colors = {
			"Weak": DANGER_COLOR,
			"Moderate": WARNING_COLOR,
			"Strong": SUCCESS_COLOR,
		}
		self.password_strength.set(f"Strength: {strength}")
		self.strength_label.configure(fg=colors[strength])
		self.strength_progress.configure(
			style=f"{strength}.Horizontal.TProgressbar",
			value={"Weak": 2, "Moderate": 4, "Strong": 6}[strength],
		)

	def analyze_password_strength(self):
		"""Analyze the password currently shown in the output field."""
		password = self.generated_password.get()
		if not password:
			messagebox.showwarning("No Password", "Generate or enter a password first.")
			return
		self.update_strength_display(password)

	def copy_password(self):
		"""Copy the generated password to the system clipboard."""
		password = self.generated_password.get()
		if not password:
			messagebox.showwarning("Nothing to Copy", "Generate a password first.")
			return

		try:
			self.root.clipboard_clear()
			self.root.clipboard_append(password)
			self.status_label.configure(text="Password copied to the clipboard.")
			messagebox.showinfo("Copied", "The generated password was copied to the clipboard.")
		except tk.TclError as error:
			messagebox.showerror("Clipboard Error", f"Could not copy the password:\n{error}")

	def save_credential(self):
		"""Validate and save the credential form in MySQL."""
		if not self.account_name.get().strip():
			messagebox.showerror("Missing Account", "Enter an account or platform name.")
			return
		if not self.username_email.get().strip():
			messagebox.showerror("Missing Username", "Enter a username or email.")
			return
		if not self.credential_password.get():
			messagebox.showerror("Missing Password", "Enter a password.")
			return
		if self.credential_category.get() not in {
			"Social",
			"Work",
			"Education",
			"Finance",
			"Gaming",
			"Other",
		}:
			messagebox.showerror("Invalid Category", "Select a valid credential category.")
			return

		password = self.credential_password.get()
		encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
		strength = self.evaluate_password_strength(password)
		connection = None

		try:
			connection = mysql.connector.connect(**DB_CONFIG)
			insert_query = """
				INSERT INTO credentials
				(account_name, username_email, encrypted_password,
				 category, strength_tier, created_date)
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
			saved_account = self.account_name.get().strip()
			self.clear_credential_form()
			self.load_credentials()
			self.status_label.configure(
				text=f"Credential saved and table refreshed: {saved_account}"
			)
		except mysql.connector.Error as error:
			messagebox.showerror(
				"Database Error",
				f"Could not save the credential. Check MySQL settings and ensure "
				f"the database exists.\n\nDetails: {error}",
			)
		finally:
			if connection is not None and connection.is_connected():
				connection.close()

	def clear_credential_form(self):
		"""Clear all values entered in the credential form."""
		self.account_name.set("")
		self.username_email.set("")
		self.credential_password.set("")
		self.credential_category.set("Other")

	def load_credentials(self):
		"""Load masked credential records from MySQL into the table."""
		for row in self.credentials_table.get_children():
			self.credentials_table.delete(row)

		connection = None
		try:
			connection = mysql.connector.connect(**DB_CONFIG)
			select_query = """
				SELECT id, account_name, username_email, category,
					strength_tier, created_date
				FROM credentials
				ORDER BY id DESC
			"""
			cursor = connection.cursor()
			cursor.execute(select_query)
			records = cursor.fetchall()
			cursor.close()

			for index, record in enumerate(records):
				record_id, platform, username, category, strength, created_date = record
				tag = "even" if index % 2 == 0 else "odd"
				self.credentials_table.insert(
					"",
					"end",
					tags=(tag,),
					values=(
						record_id,
						platform,
						username,
						"********",
						category,
						strength,
						created_date,
					),
				)
			if records:
				self.empty_table_label.place_forget()
			else:
				self.empty_table_label.place(relx=0.5, rely=0.5, anchor="center")
			self.status_label.configure(
				text=f"Credential table refreshed: {len(records)} record(s)."
			)
		except mysql.connector.Error as error:
			messagebox.showerror(
				"Database Error",
				f"Could not load credentials. Check MySQL settings and ensure "
				f"the table exists.\n\nDetails: {error}",
			)
		finally:
			if connection is not None and connection.is_connected():
				connection.close()

	def get_selected_record_id(self):
		"""Return the selected table record ID or show a warning."""
		selected_items = self.credentials_table.selection()
		if not selected_items:
			messagebox.showwarning("No Selection", "Select a credential record first.")
			return None

		selected_values = self.credentials_table.item(selected_items[0], "values")
		return selected_values[0]

	def reveal_password(self):
		"""Decode and display the selected password for classroom demonstration."""
		record_id = self.get_selected_record_id()
		if record_id is None:
			return

		connection = None
		try:
			connection = mysql.connector.connect(**DB_CONFIG)
			query = "SELECT encrypted_password FROM credentials WHERE id = %s"
			cursor = connection.cursor()
			cursor.execute(query, (record_id,))
			record = cursor.fetchone()
			cursor.close()

			if record is None:
				messagebox.showerror("Not Found", "The selected record no longer exists.")
				return

			encoded_password = record[0]
			password = base64.b64decode(encoded_password).decode("utf-8")
			messagebox.showinfo(
				"Revealed Password",
				"This is a classroom demonstration. Base64 is encoding, not encryption.\n\n"
				f"Password: {password}",
			)
		except (binascii.Error, UnicodeDecodeError):
			messagebox.showerror("Decode Error", "The stored password could not be decoded.")
		except mysql.connector.Error as error:
			messagebox.showerror("Database Error", f"Could not retrieve the password.\n\nDetails: {error}")
		finally:
			if connection is not None and connection.is_connected():
				connection.close()

	def delete_record(self):
		"""Delete the selected credential after user confirmation."""
		record_id = self.get_selected_record_id()
		if record_id is None:
			return

		confirmed = messagebox.askyesno(
			"Confirm Delete",
			"Are you sure you want to delete the selected credential?",
		)
		if not confirmed:
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
			self.status_label.configure(text="Credential deleted successfully.")
			self.load_credentials()
		except mysql.connector.Error as error:
			messagebox.showerror("Database Error", f"Could not delete the credential.\n\nDetails: {error}")
		finally:
			if connection is not None and connection.is_connected():
				connection.close()

	def plot_analytics(self):
		"""Load credential data with Pandas and display security charts."""
		connection = None
		try:
			connection = mysql.connector.connect(**DB_CONFIG)
			query = """
				SELECT category, strength_tier
				FROM credentials
			"""
			dataframe = pd.read_sql(query, connection)

			if dataframe.empty:
				messagebox.showinfo(
					"No Data",
					"Add some credentials before viewing analytics.",
				)
				return

			category_counts = dataframe["category"].value_counts()
			strength_counts = dataframe["strength_tier"].value_counts()

			figure, (axis_one, axis_two) = plt.subplots(1, 2, figsize=(11, 5))
			axis_one.bar(
				category_counts.index,
				category_counts.values,
				color=PRIMARY_COLOR,
			)
			axis_one.set_title("Vault Accounts by Category", fontweight="bold")
			axis_one.set_xlabel("Category")
			axis_one.set_ylabel("Number of Accounts")
			axis_one.tick_params(axis="x", rotation=30)

			axis_two.pie(
				strength_counts.values,
				labels=strength_counts.index,
				autopct="%1.1f%%",
				startangle=90,
				colors=[DANGER_COLOR, WARNING_COLOR, SUCCESS_COLOR],
			)
			axis_two.set_title("Password Strength Distribution", fontweight="bold")

			figure.tight_layout()
			plt.show()
			self.status_label.configure(text="Analytics loaded successfully.")
		except Exception as error:
			messagebox.showerror(
				"Analytics Error",
				f"Could not generate analytics:\n{error}",
			)
		finally:
			if connection is not None and connection.is_connected():
				connection.close()


def main():
	root = tk.Tk()
	PassVaultApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()

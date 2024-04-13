import json
import tkinter as tk
from tkinter import messagebox


class PasswordManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager")

        # Initialize variables
        self.accounts = {}
        self.load_accounts()

        # Create widgets
        self.account_label = tk.Label(self.root, text="Account:")
        self.account_label.grid(row=0, column=0, sticky="e")
        self.account_entry = tk.Entry(self.root)
        self.account_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_password)
        self.save_button.grid(row=2, column=0, columnspan=2, sticky="we")

        self.show_button = tk.Button(self.root, text="Show Passwords", command=self.show_passwords)
        self.show_button.grid(row=3, column=0, columnspan=2, sticky="we")

    def load_accounts(self):
        try:
            with open("accounts.json", "r") as f:
                self.accounts = json.load(f)
        except FileNotFoundError:
            self.accounts = {}

    def save_accounts(self):
        with open("accounts.json", "w") as f:
            json.dump(self.accounts, f)

    def save_password(self):
        account = self.account_entry.get()
        password = self.password_entry.get()
        if account and password:
            self.accounts[account] = password
            self.save_accounts()
            messagebox.showinfo("Success", "Password saved successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter account and password.")

    def show_passwords(self):
        passwords = "\n".join([f"{account}: {password}" for account, password in self.accounts.items()])
        if passwords:
            messagebox.showinfo("Passwords", passwords)
        else:
            messagebox.showinfo("No Passwords", "No passwords saved.")

    def clear_entries(self):
        self.account_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.run()

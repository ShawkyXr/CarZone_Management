import tkinter as tk
import sqlite3
from Management import get_db_connection

def add_user(root):
    # Create a new window for user registration
    register_window = tk.Toplevel(root)
    register_window.title("Add User")
    register_window.geometry("700x550")
    register_window.config(bg="#020202")

    user_label = tk.Label(register_window, text="Username", font=("jetbrains mono", 12), fg="#d6a629", bg="#020202")
    user_label.pack(pady=10)
    user_entry = tk.Entry(register_window, font=("jetbrains mono", 12), bg="white")
    user_entry.pack(pady=5)

    password_label = tk.Label(register_window, text="Password", font=("jetbrains mono", 12), fg="#d6a629", bg="#020202")
    password_label.pack(pady=10)
    password_entry = tk.Entry(register_window, font=("jetbrains mono", 12), bg="white", show="*")
    password_entry.pack(pady=5)

    def save_user():
        user = user_entry.get()
        password = password_entry.get()

        if not user or not password:
            tk.messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, password))
            conn.commit()
            tk.messagebox.showinfo("Success", "User added successfully.")
            register_window.destroy()
        except sqlite3.IntegrityError:
            tk.messagebox.showerror("Error", "This user is already registered.")
        finally:
            conn.close()

    save_user_btn = tk.Button(register_window, text="Save User", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629", bd=0, highlightthickness=0, command=save_user)
    save_user_btn.pack(pady=20)


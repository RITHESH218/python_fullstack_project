# app.py

import sys
import os

# Add parent directory to sys.path so 'src' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk, messagebox
from src.logic import get_timetable
from src.db import get_connection
import pandas as pd


# --- Fetch courses dynamically from Supabase ---
def fetch_courses():
    query = "SELECT course_name FROM courses ORDER BY course_name;"
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
        return df['course_name'].tolist() if not df.empty else []
    finally:
        conn.close()


# --- GUI Setup ---
root = tk.Tk()
root.title("College Timetable Viewer")
root.geometry("650x450")

# Course selection
tk.Label(root, text="Course:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
course_var = tk.StringVar()
course_entry = ttk.Combobox(root, textvariable=course_var)
course_entry['values'] = fetch_courses()
course_entry.grid(row=0, column=1, padx=10, pady=10)

# Day selection
tk.Label(root, text="Day:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
day_var = tk.StringVar()
day_entry = ttk.Combobox(root, textvariable=day_var)
day_entry['values'] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
day_entry.grid(row=1, column=1, padx=10, pady=10)

# Text area to display timetable
text_area = tk.Text(root, height=15, width=80)
text_area.grid(row=3, column=0, columnspan=3, padx=10, pady=10)


# --- Functions ---
def show_timetable():
    text_area.delete(1.0, tk.END)
    course_name = course_var.get()
    day = day_var.get()

    if not course_name or not day:
        messagebox.showwarning("Input Error", "Please select both course and day.")
        return

    df, error = get_timetable(course_name, day)
    if error:
        text_area.insert(tk.END, f"{error}\n")
    else:
        for idx, row in df.iterrows():
            line = f"Period {row['period']}: {row['subject']} - {row['teacher']} (Class: {row['classroom']})\n"
            text_area.insert(tk.END, line)


# Button
show_btn = tk.Button(root, text="Show Timetable", command=show_timetable)
show_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Run GUI
root.mainloop()

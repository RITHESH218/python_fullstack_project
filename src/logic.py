# src/logic.py

from src.db import get_course_id, fetch_timetable_from_db
import pandas as pd

def get_timetable(course_name, day):
    """
    Fetch timetable for a course name and day.
    Returns a DataFrame and an error message (None if successful).
    """
    try:
        course_id = get_course_id(course_name)
        if not course_id:
            return None, f"Course '{course_name}' not found"

        df = fetch_timetable_from_db(course_id, day)
        if df.empty:
            return df, f"No timetable found for {course_name} on {day}"

        df = df.sort_values(by="period").reset_index(drop=True)
        return df, None

    except Exception as e:
        return None, f"Error fetching timetable: {e}"


def display_timetable(df):
    """Print timetable nicely in terminal."""
    if df is None or df.empty:
        print("No timetable to display.")
        return

    print("\nTimetable:")
    print("-" * 50)
    for idx, row in df.iterrows():
        print(f"Period {row['period']}: {row['subject']} - {row['teacher']} (Class: {row['classroom']})")
    print("-" * 50)

import sys
import os
import streamlit as st
import pandas as pd

# Add parent directory so 'src' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Page Config ---
st.set_page_config(page_title="College Timetable Viewer", layout="wide")
st.title("📅 College Timetable Viewer")

# --- Try importing logic safely ---
try:
    from src.logic import TableManager
    table_manager = TableManager()
    st.write("✅ Logic loaded successfully")
except Exception as e:
    st.error(f"⚠️ Could not load logic/db: {e}")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Fetch courses safely
try:
    courses = [c["course_name"] for c in table_manager.get_all_courses()]
except Exception as e:
    courses = []
    st.sidebar.error(f"❌ Could not load courses: {e}")

selected_course = st.sidebar.selectbox("Select Course", courses if courses else ["No courses available"])
selected_day = st.sidebar.selectbox("Select Day", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))

# --- Fetch Timetable ---
if st.sidebar.button("Show Timetable"):
    try:
        df = table_manager.get_timetable(selected_course, selected_day)

        if df is None or df.empty:
            st.warning("⚠️ No timetable found for this course and day.")
        else:
            df_display = df[["period", "subject_name", "teacher_name", "classroom"]]
            df_display = df_display.rename(columns={
                "period": "Period",
                "subject_name": "Subject",
                "teacher_name": "Teacher",
                "classroom": "Classroom"
            })
            st.success("✅ Timetable loaded successfully!")
            st.table(df_display)
    except Exception as e:
        st.error(f"💥 Error fetching timetable: {e}")

# --- Manage Timetable ---
st.sidebar.markdown("---")
st.sidebar.subheader("Manage Timetable")
action = st.sidebar.selectbox("Action", ["Add Entry", "Update Entry", "Delete Entry"])

if action:
    st.sidebar.write("Fill in the details below:")
    day = st.sidebar.selectbox("Day", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
    period = st.sidebar.number_input("Period", min_value=1, max_value=10, step=1)
    subject = st.sidebar.text_input("Subject Name")
    teacher = st.sidebar.text_input("Teacher Name")
    classroom = st.sidebar.text_input("Classroom")

    if st.sidebar.button(action):
        try:
            if action == "Add Entry":
                table_manager.add_timetable_entry(selected_course, day, period, subject, teacher, classroom)
                st.success("✅ Timetable entry added successfully!")
            elif action == "Update Entry":
                table_manager.update_timetable_entry(selected_course, day, period, subject, teacher, classroom)
                st.success("✅ Timetable entry updated successfully!")
            elif action == "Delete Entry":
                table_manager.delete_timetable_entry(selected_course, day, period)
                st.success("✅ Timetable entry deleted successfully!")
        except Exception as e:
            st.error(f"💥 Error performing action: {e}")

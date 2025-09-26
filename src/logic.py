import pandas as pd
from src.db import DatabaseManager


class TableManager:
    def __init__(self):
        self.db = DatabaseManager()

    def get_timetable(self, course_name: str, day: str):
        """Fetch timetable for a given course and day as a DataFrame."""
        course_id = self.db.get_course_id_value(course_name)
        if not course_id:
            return pd.DataFrame()  # empty if course not found

        timetable_data = self.db.fetch_timetable(course_id, day)
        df = pd.DataFrame(timetable_data)

        if df.empty:
            return df

        return df.sort_values(by="period").reset_index(drop=True)

    def add_course(self, course_name: str):
        return self.db.add_course(course_name)

    def add_timetable_entry(self, course_name: str, day: str, period: int, subject_name: str, teacher_name: str, classroom: str):
        course_id = self.db.get_course_id_value(course_name)
        if not course_id:
            return None
        return self.db.add_timetable_entry(course_id, day, period, subject_name, teacher_name, classroom)

    def update_timetable_entry(self, course_name: str, day: str, period: int, subject_name: str, teacher_name: str, classroom: str):
        course_id = self.db.get_course_id_value(course_name)
        if not course_id:
            return None
        return self.db.update_timetable_entry(course_id, day, period, subject_name, teacher_name, classroom)

    def delete_timetable_entry(self, course_name: str, day: str, period: int):
        course_id = self.db.get_course_id_value(course_name)
        if not course_id:
            return None
        return self.db.delete_timetable_entry(course_id, day, period)

    def get_all_courses(self):
        return self.db.get_courses()

    def get_all_timetables(self):
        return self.db.get_all_timetables()

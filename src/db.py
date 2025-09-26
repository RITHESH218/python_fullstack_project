import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(url, key)


class DatabaseManager:
    def __init__(self):
        self.client: Client = supabase

    # -------- Courses --------
    def get_courses(self):
        """Fetch all courses."""
        return self.client.table("courses").select("*").execute().data

    def add_course(self, course_name: str):
        """Insert a new course."""
        return self.client.table("courses").insert({"course_name": course_name}).execute().data

    def get_course_id(self, course_name: str):
        """Fetch course_id by course_name (full response)."""
        return self.client.table("courses").select("course_id").eq("course_name", course_name).execute().data

    def get_course_id_value(self, course_name: str):
        """Return course_id directly (or None if not found)."""
        result = self.get_course_id(course_name)
        return result[0]["course_id"] if result else None

    # -------- Timetable --------
    def fetch_timetable(self, course_id: int, day: str):
        """Fetch the timetable for a given course_id and day."""
        return (
            self.client.table("timetable")
            .select("*")
            .eq("course_id", course_id)
            .eq("day", day)
            .execute()
            .data
        )

    def add_timetable_entry(self, course_id: int, day: str, period: int, subject_name: str, teacher_name: str, classroom: str):
        """Insert a new timetable entry."""
        return (
            self.client.table("timetable")
            .insert({
                "course_id": course_id,
                "day": day,
                "period": period,
                "subject_name": subject_name,
                "teacher_name": teacher_name,
                "classroom": classroom,
            })
            .execute()
            .data
        )

    def update_timetable_entry(self, course_id: int, day: str, period: int, subject_name: str, teacher_name: str, classroom: str):
        """Update a timetable entry."""
        return (
            self.client.table("timetable")
            .update({
                "subject_name": subject_name,
                "teacher_name": teacher_name,
                "classroom": classroom,
            })
            .eq("course_id", course_id)
            .eq("day", day)
            .eq("period", period)
            .execute()
            .data
        )

    def delete_timetable_entry(self, course_id: int, day: str, period: int):
        """Delete a timetable entry by course_id, day, and period."""
        return (
            self.client.table("timetable")
            .delete()
            .eq("course_id", course_id)
            .eq("day", day)
            .eq("period", period)
            .execute()
            .data
        )

    def get_all_timetables(self):
        """Fetch all timetable entries."""
        return self.client.table("timetable").select("*").execute().data

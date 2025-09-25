import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(url, key)

def get_course_id(course_name: str):
    """Get the course_id for a given course_name."""
    return supabase.table("courses").select("course_id").eq("course_name", course_name).execute()


def fetch_timetable(course_id: int, day: str):
    """Fetch the timetable for a given course_id and day."""
    return supabase.table("timetable").select("*").eq("course_id", course_id).eq("day", day).execute()

def update_timetable(course_id: int, day: str, period: int, subject_name: str, teacher_name: str, classroom: str):
    """Update a timetable entry."""
    response = supabase.table("timetable").update({
        "subject_name": subject_name,
        "teacher_name": teacher_name,
        "classroom": classroom
    }).eq("course_id", course_id).eq("day", day).eq("period", period).execute()
    return response.data

def get_all_timetables():
    """Fetch all timetable entries."""
    return supabase.table("timetable").select("*").execute()

def delete_timetable_entry(course_id: int):
    """Delete a timetable entry by course_id."""
    return supabase.table("timetable").delete().eq("course_id", course_id).execute()

def add_course(course_name: str):
    """Insert a new course."""
    return supabase.table("courses").insert({"course_name": course_name}).execute()

def add_timetable_entry(course_id: int, day: str, period: int, subject_name: str, teacher_name: str, classroom: str):
    """Insert a new timetable entry."""
    return supabase.table("timetable").insert({
        "course_id": course_id,
        "day": day,
        "period": period,
        "subject_name": subject_name,
        "teacher_name": teacher_name,
        "classroom": classroom
    }).execute()

def get_courses():
    """Fetch all courses."""
    return supabase.table("courses").select("*").execute()
    


c = delete_timetable_entry(8)

print(c)

















































'''import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_connection():
    """Create a PostgreSQL connection to Supabase."""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def get_course_id(course_name):
    """Get the course_id for a given course_name."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT course_id FROM courses WHERE course_name = %s", (course_name,))
        result = cur.fetchone()
        return result[0] if result else None
    finally:
        conn.close()


def fetch_timetable_from_db(course_id, day):
    """Fetch timetable rows for a given course_id and day."""
    query = """
    SELECT period, subject_name AS subject, teacher_name AS teacher, classroom
    FROM timetable
    WHERE course_id = %s AND day = %s
    ORDER BY period;
    """
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn, params=(course_id, day))
    finally:
        conn.close()
    return df'''








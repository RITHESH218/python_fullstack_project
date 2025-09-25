# src/db.py

import psycopg2
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
    return df

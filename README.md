# College Time Table Viewer

A simple Python application to view college timetables by day.
# Features
View daily timetables for any course/branch
Displays subject, teacher, period, and classroom
User-friendly GUI with Tkinter
Timetable data stored and retrieved from PostgreSQL

## Project Structure


timetable/
|
|--- src/
|    |-- logic.py         # Core logic for timetable operations
operations/
|    |-- db.py      # Database connection and queries (PostgreSQL)
| 
|--- api/
|   |-- main.py    # FASTAPI endpoints 
|
|--- frontend/       #Frontend web application
|    |-- app.py     # Tkinter GUI application
|
|___requirements.txt  #Python dependencies
|
|___ README.md        #Project documentation
|
|___.env             #Python Variables


## Quick Start

### Prerequisites
-Python 3.8 or higher
-A supabase account
-Git (Push,cloning)

### 1.Clone or Download the Project
# option 1: Clone with Git
git clone<repository-url>

### 2.Install Dependencies

# Install all required 
pip install -r requirements.txt

### 3.get your credentials

1 . CReate a '.env' file in the project root

2 .Add your supabase credentials to '.env':

SUPABASE_URL="https://jelazjiunbjgigjnxygb.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImplbGF6aml1bmJqZ2lnam54eWdiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIzODAsImV4cCI6MjA3MzY1ODM4MH0.NlFERQFtEeWKV2Ono8G3f8l6j2sSiY-8G8r9iUvTR5g"


### Run the application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at 'https://local 









### Future enhancements

-Add dropdown menus for courses and days instead of text input.
-Export timetable to PDF or CSV.
-Add functionality to edit or update existing timetable entries.
-Support multiple semesters or batches.

### Support
 If you have any issues ,please open an issue on Github or contact the development team.
 -MOBILE-> 9494940920.
 -MAIL-> ritheshshinde5@gmail.com

# College Timetable Viewer

A simple Python application to view and manage college timetables by day using Streamlit and FastAPI, with data stored in PostgreSQL/Supabase.

---

## Features

- View daily timetables for any course or branch
- Displays subject, teacher, period, and classroom
- User-friendly web interface with Streamlit
- Supports adding, updating, and deleting timetable entries via API
- Timetable data stored and retrieved from PostgreSQL/Supabase

---

## Project Structure

```
timetable/
│
├── src/
│   ├── db.py         # Database connection and queries (PostgreSQL/Supabase)
│   └── logic.py      # Core logic for timetable operations
│
├── api/
│   └── main.py       # FastAPI endpoints
│
├── frontend/
│   └── app.py        # Streamlit GUI application
│
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── .env              # Environment variables (Supabase credentials)
```

---

## Prerequisites

- Python 3.8+
- Supabase account or PostgreSQL database
- Git (for cloning)

---

## Quick Start

### 1. Clone the Repository

```sh
git clone <repository-url>
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the project root and add your Supabase credentials:

```
SUPABASE_URL="https://your-supabase-url.supabase.co"
SUPABASE_KEY="your-supabase-api-key"
```

### 4. Database Setup

If using PostgreSQL/Supabase, create the tables:

```sql
-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL
);

-- Timetable table
CREATE TABLE IF NOT EXISTS timetable (
    timetable_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(course_id),
    day VARCHAR(20) NOT NULL,
    period INT NOT NULL,
    subject_name VARCHAR(50) NOT NULL,
    teacher_name VARCHAR(50) NOT NULL,
    classroom VARCHAR(20) NOT NULL
);
```

---

## Running the Application

### 1. Start FastAPI Backend

```sh
uvicorn api.main:app --reload
```
- API available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)


### 2. Run Streamlit Frontend

```sh
streamlit run frontend/app.py
```
- Opens in your browser (default: [http://localhost:8501](http://localhost:8501))
- Select course and day to view the timetable

---

## Usage

- Launch the Streamlit GUI or API server
- Choose a course and day
- View timetable with subject, teacher, period, and classroom
- Use API or frontend to add/update/delete entries

---

## API Endpoints

| Endpoint                | Method | Description                           |
|-------------------------|--------|---------------------------------------|
| `/add_course`           | POST   | Add a new course                      |
| `/add_timetable_entry`  | POST   | Add a new timetable entry             |
| `/update_timetable_entry`| POST  | Update an existing timetable entry    |
| `/delete_timetable`     | POST   | Delete a timetable entry              |
| `/get_all_courses`      | GET    | Retrieve all courses                  |
| `/get_timetable`        | POST   | Retrieve timetable for a course & day |
| `/get_all_timetables`   | GET    | Retrieve all timetable entries        |

---

## Future Enhancements

- Dropdown menus for courses and days (more user-friendly)
- Export timetable to PDF or CSV
- Multi-semester or batch support
- Full in-place editing of timetable entries in the frontend

---

## Support

If you encounter issues, please contact the development team:

  
- **Email:** ritheshshinde5@gmail.com  
- Or open an issue on the GitHub repository

---

## License

This project is open-source and available under the MIT
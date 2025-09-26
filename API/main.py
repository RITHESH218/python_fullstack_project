import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from functools import wraps

# --- Import TableManager from src ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import TableManager

# --- App Setup ---
app = FastAPI(
    title="Timetable API",
    description="API for managing course timetables",
    version="1.0.0"
)

# --- Allow Frontend to Access API ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Initialize TableManager ---
table_manager = TableManager()

# ----------------- DATA MODELS -------------------
class Course(BaseModel):
    course_name: str 

class TimetableEntry(BaseModel):
    course_name: str
    day: str
    period: int
    subject_name: str
    teacher_name: str
    classroom: str

class UpdateTimetableEntry(TimetableEntry):
    pass

class DeleteTimetable(BaseModel):
    course_name: str
    day: str
    period: int

class GetTimetable(BaseModel):
    course_name: str
    day: str

class ResponseModel(BaseModel):
    message: str
    data: dict | list | None

# ----------------- HELPER DECORATOR -------------------
def handle_exceptions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs) if callable(func) else func(*args, **kwargs)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return wrapper

# ----------------- ENDPOINTS -------------------

@app.post("/add_course", response_model=ResponseModel)
@handle_exceptions
async def add_course(course: Course):
    result = table_manager.add_course(course.course_name)
    return {"message": "Course added successfully", "data": result}


@app.post("/add_timetable_entry", response_model=ResponseModel)
@handle_exceptions
async def add_timetable_entry(entry: TimetableEntry):
    result = table_manager.add_timetable_entry(
        entry.course_name, entry.day, entry.period,
        entry.subject_name, entry.teacher_name, entry.classroom
    )
    return {"message": "Timetable entry added successfully", "data": result}


@app.post("/update_timetable_entry", response_model=ResponseModel)
@handle_exceptions
async def update_timetable_entry(entry: UpdateTimetableEntry):
    result = table_manager.update_timetable_entry(
        entry.course_name, entry.day, entry.period,
        entry.subject_name, entry.teacher_name, entry.classroom
    )
    return {"message": "Timetable entry updated successfully", "data": result}


@app.post("/delete_timetable", response_model=ResponseModel)
@handle_exceptions
async def delete_timetable(entry: DeleteTimetable):
    result = table_manager.delete_timetable_entry(entry.course_name, entry.day, entry.period)
    return {"message": "Timetable entry deleted successfully", "data": result}


@app.get("/get_all_courses", response_model=ResponseModel)
@handle_exceptions
async def get_all_courses():
    result = table_manager.get_all_courses()
    return {"message": "Courses retrieved successfully", "data": result}


@app.post("/get_timetable", response_model=ResponseModel)
@handle_exceptions
async def get_timetable(entry: GetTimetable):
    df = table_manager.get_timetable(entry.course_name, entry.day)
    data = df.to_dict(orient="records") if not df.empty else []
    return {"message": "Timetable retrieved successfully", "data": data}


@app.get("/get_all_timetables", response_model=ResponseModel)
@handle_exceptions
async def get_all_timetables():
    timetables = table_manager.get_all_timetables()
    return {"message": "All timetables retrieved successfully", "data": timetables}


@app.get("/", response_model=dict)
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Timetable API. Use the endpoints to manage courses and timetables."}


# --- Run App ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# frontend --> API --> logic --> db --> response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys, os
from pydantic import BaseModel

# --- Import TableManager from src ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import TableManager

# ------- App setup --------------------
app = FastAPI(
    title="Timetable API",
    description="API for managing course timetables",
    version="1.0.0"
)

# ------------- Allow Frontend to access API ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ✅ Corrected
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creating an instance of TableManager
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
    pass  # Same fields as TimetableEntry

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

# ----------------- ENDPOINTS -------------------

@app.post("/add_course", response_model=ResponseModel)
async def add_course(course: Course):
    """Add a new course."""
    try:
        result = table_manager.add_course(course.course_name)
        return {"message": "Course added successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/add_timetable_entry", response_model=ResponseModel)
async def add_timetable_entry(entry: TimetableEntry):
    """Add a new timetable entry."""
    try:
        result = table_manager.add_timetable_entry(
            entry.course_name, 
            entry.day, 
            entry.period, 
            entry.subject_name, 
            entry.teacher_name, 
            entry.classroom
        )
        return {"message": "Timetable entry added successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/update_timetable_entry", response_model=ResponseModel)
async def update_timetable_entry(entry: UpdateTimetableEntry):
    """Update an existing timetable entry."""
    try:
        result = table_manager.update_timetable_entry(
            entry.course_name, 
            entry.day, 
            entry.period, 
            entry.subject_name, 
            entry.teacher_name, 
            entry.classroom
        )
        return {"message": "Timetable entry updated successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/delete_timetable", response_model=ResponseModel)
async def delete_timetable(entry: DeleteTimetable):
    """Delete a timetable entry by course, day, and period."""
    try:
        result = table_manager.delete_timetable(
            entry.course_name, 
            entry.day, 
            entry.period
        )
        return {"message": "Timetable entry deleted successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get_all_courses", response_model=ResponseModel)
async def get_all_courses():
    """Get all courses."""
    try:
        result = table_manager.get_all_courses()
        return {"message": "Courses retrieved successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get_timetable", response_model=ResponseModel)
async def get_timetable(entry: GetTimetable):
    """Get timetable for a specific course and day."""
    try:
        result = table_manager.get_timetable(entry.course_name, entry.day)
        return {"message": "Timetable retrieved successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get_all_timetables", response_model=ResponseModel)
async def get_all_timetables():
    """Get all timetables."""
    try:
        result = table_manager.get_all_timetables()
        return {"message": "All timetables retrieved successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_model=dict)
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Timetable API. Use the endpoints to manage courses and timetables."}


# Run the FastAPI app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

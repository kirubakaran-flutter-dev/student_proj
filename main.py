# import os
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles

# from database import Base, engine
# import models

# # Student router import
# from routers.student_router import router as student_router

# # Create DB Tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # ---------- FRONTEND PATH SETUP ----------
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# frontend_path = os.path.join(BASE_DIR, "frontend")

# # Serve frontend folder
# app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")

# # Show login page as default home page
# @app.get("/", response_class=HTMLResponse)
# def show_login():
#     login_file = os.path.join(frontend_path, "login", "login.html")
#     with open(login_file, "r", encoding="utf-8") as f:
#         return f.read()


# # ---------- API ROUTES ----------
# app.include_router(student_router)


import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from database import Base, engine
import models

# Student router import
from routers.student_router import router as student_router

# Create DB Tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ---------- FRONTEND PATH ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
frontend_path = os.path.join(BASE_DIR, "frontend")

# Serve frontend
app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")

# ---------- SHOW student_add.html ----------
@app.get("/", response_class=HTMLResponse)
def show_student_add():
    html_path = os.path.join(
        frontend_path, "presentation", "student_add", "student_add.html"
    )

    # Debug print
    print("Loading HTML:", html_path)

    if not os.path.exists(html_path):
        return f"HTML file not found: {html_path}"

    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()


# ---------- API ROUTES ----------
app.include_router(student_router)

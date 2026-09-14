from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/ping")
def ping():
    return "pong"

@app.get("/login-form")
def login_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"request": request}
    )

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE (username=? OR email=?)
        AND password=?
    """, (username, username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        return {"message": "Login thành công"}

    return {"message": "Sai tài khoản hoặc mật khẩu"}

@app.get("/all")
def all_users(request: Request):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, email, password
        FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="all.html",
        context={
            "request": request,
            "users": users
        }
    )
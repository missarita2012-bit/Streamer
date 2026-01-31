from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Cinema Hub")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"status": "Cinema Hub Running"}

@app.get("/watch/{file_id}", response_class=HTMLResponse)
def watch(request: Request, file_id: str):
    return templates.TemplateResponse(
        "watch.html",
        {
            "request": request,
            "file_id": file_id
        }
    )
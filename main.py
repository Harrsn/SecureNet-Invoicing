from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.requests import Request
from invoice_generator import create_invoice_pdf
from typing import List
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("invoice_form.html", {"request": request})

@app.post("/generate", response_class=FileResponse)
async def generate_invoice(
    request: Request,
    client_name: str = Form(...),
    address: str = Form(...),
    estimate_no: str = Form(...),
    issue_date: str = Form(...),
    valid_until: str = Form(...),
    description: List[str] = Form(...),
    qty: List[int] = Form(...),
    price: List[float] = Form(...)
):
    items = list(zip(description, qty, price))
    filename = create_invoice_pdf(client_name, address, estimate_no, issue_date, valid_until, items)
    return FileResponse(path=filename, filename=os.path.basename(filename), media_type='application/pdf')

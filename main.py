from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from PIL import Image
import uvicorn
import os
import io
import time

app = FastAPI()

# Монтируем папку со статическими файлами (CSS, JS, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Указываем папку с HTML-шаблонами
templates = Jinja2Templates(directory="templates")

# Создаем папки, если их нет
os.makedirs("static/images", exist_ok=True)
os.makedirs("templates", exist_ok=True)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer " + "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"}
textReq = ""

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def res(text):
    image_bytes = query({
        "inputs": text,
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save('static/images/example.jpg')
    return image


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    textReq = request.query_params.get("text")
    timestamp = int(time.time())
    # Отображаем HTML-страницу из шаблонов
    return templates.TemplateResponse("example.html", {"request": request,
        "timestamp": timestamp})


@app.get("/result", response_class=HTMLResponse)
async def show_image(request: Request):
    res(request.query_params.get("text"))

    # Путь к изображению (относительно static)
    image_path = "images/example.jpg"

    # Контекст для передачи в шаблон
    context = {
        "request": request,
        "image_path": image_path,
        "title": "Проектный практикум",
        "description": "Результат:"
    }
    return templates.TemplateResponse("result.html", context)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

import requests
import streamlit as st
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def res (text):
	image_bytes = query({
	"inputs": text,
	})
	image = Image.open(io.BytesIO(image_bytes))
	return image

st.title('Преобразование текста в изображение')
title = st.text_input("Текст запроса", "")

result = st.button('Получить изображение')
if result:
	img = res(title)
	st.image(img, caption="")

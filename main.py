import requests
import streamlit as st
import io
from PIL import Image
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer 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"}



API_URL_TR = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
headers_TR = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxx"}

def query_TR(payload):
	response = requests.post(API_URL_TR, headers=headers_TR, json=payload)
	return response.json()
	
output = query_TR({
	"inputs": "Меня зовут Вольфганг и я живу в Берлине",
})

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def res (text):
	output = query_TR({
	"inputs": text,
	})
	image_bytes = query({
	"inputs": output,
	})
	image = Image.open(io.BytesIO(image_bytes))
	return image

st.title('Преобразование текста в изображение')
title = st.text_input("Текст запроса", "")

result = st.button('Получить изображение')
if result:
	img = res(title)
	st.image(img, caption="")

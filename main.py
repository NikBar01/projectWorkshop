import requests
import streamlit as st
import io
from PIL import Image


API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer "+"NThhJVqtIY"}

API_URL_TR = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ru-en"
headersTR = {"Authorization": "Bearer "+"NThhJVqtIY"}


def queryTR(payload):
    response = requests.post(API_URL_TR, headers=headersTR, json=payload)
    return response.json()

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def res (text):
	# output = query_TR({
	# "inputs": text,
	# })
	image_bytes = query({
	"inputs": text,
	})
	image = Image.open(io.BytesIO(image_bytes))
	return image

st.title('Преобразование текста в изображение')
title = st.text_input("Описание для генирации картинки", "")
output = queryTR({
    "inputs": title,
})
result = st.button('Получить изображение')
if result:
	img = res(output[0]['translation_text'])
	st.image(img, caption="")



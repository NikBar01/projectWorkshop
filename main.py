import requests
import streamlit as st
import io
from PIL import Image
from transformers import pipeline

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer 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"}



# API_URL_TR = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
# headers_TR = {"Authorization": "Bearer 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"}

# def query_TR(payload):
# 	response = requests.post(API_URL_TR, headers=headers_TR, json=payload)
# 	return response.json()

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

model_checkpoint = "Helsinki-NLP/opus-mt-en-ru"
translator = pipeline("translation", model=model_checkpoint)
result = translator("How are you?")
result = result[0]

st.title('Преобразование текста в изображение')
title = st.text_input(result, "")

print(result)

result = st.button('Получить изображение')
if result:
	img = res(title)
	st.image(img, caption="")

import requests
import streamlit as st
import io
from PIL import Image
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

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

# model_name = 'jbochi/madlad400-3b-mt'
# model = T5ForConditionalGeneration.from_pretrained(model_name, device_map="auto")
# tokenizer = T5Tokenizer.from_pretrained(model_name)

# text = "<2pt> I love pizza!"
# input_ids = tokenizer(text, return_tensors="pt").input_ids.to(model.device)
# outputs = model.generate(input_ids=input_ids)

# translet = tokenizer.decode(outputs[0], skip_special_tokens=True)

st.title('Преобразование текста в изображение')
title = st.text_input("Описание", "")

print(result)

result = st.button('Получить изображение')
if result:
	img = res(title)
	st.image(img, caption="")

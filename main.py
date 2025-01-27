import requests
import streamlit as st
import io
from PIL import Image

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

result = st.button('Получить изображение')
if result:
	img = res(title)
	st.image(img, caption="")


from transformers import T5ForConditionalGeneration, T5Tokenizer

device = 'cuda' #or 'cpu' for translate on cpu

model_name = 'utrobinmv/t5_translate_en_ru_zh_small_1024'
model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(device)
tokenizer = T5Tokenizer.from_pretrained(model_name)

prefix = 'translate to zh: '
src_text = prefix + "Цель разработки — предоставить пользователям личного синхронного переводчика."

# translate Russian to Chinese
input_ids = tokenizer(src_text, return_tensors="pt")

generated_tokens = model.generate(**input_ids.to(device))

result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(result)

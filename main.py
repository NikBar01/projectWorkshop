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
	image.show()
	return image

st.title('Новая улучшенная классификации изображений в облаке Streamlit')
title = st.text_input("Movie title", "Life of Brian")

result = st.button('Распознать изображение')
if result:
	img = res(title)
	st.image(img, caption="result")
	
    # x = preprocess_image(img)
    # preds = model.predict(x)
    # st.write('**Результаты распознавания:**')
    # print_predictions(preds)

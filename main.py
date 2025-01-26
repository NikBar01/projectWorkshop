import requests
import streamlit as st
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

image_bytes = query({
	"inputs": "Astronaut riding a horse",
})

# You can access the image with PIL.Image for example

image = Image.open(io.BytesIO(image_bytes))
image.show()

st.title('Новая улучшенная классификации изображений в облаке Streamlit')
title = st.text_input("Movie title", "Life of Brian")
img = load_image()
result = st.button('Распознать изображение')
if result:
    x = preprocess_image(img)
    preds = model.predict(x)
    st.write('**Результаты распознавания:**')
    print_predictions(preds)

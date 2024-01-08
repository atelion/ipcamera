import google.generativeai as genai
import os
import PIL.Image

genai.configure(api_key="AIzaSyBk6OieatfwGeKZd_Dtuw18Rze93hs87YA")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the future of AI in one sentence?")
print(response.text)
# print(response.prompt_feedback)
# print(response.candidates)
response = model.generate_content("What is the future of AI in one sentence?", stream=True)
for chunk in response:
  print(chunk.text)
  print("_"*80)

img = PIL.Image.open("image.jpeg")
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
# response = model.generate_content(["Write a short, engaging blog artile based on this picture.", img], stream=False)
response.resolve()
print(response.text)
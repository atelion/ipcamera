
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBk6OieatfwGeKZd_Dtuw18Rze93hs87YA")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    user_input = input("You: ")
    response = chat.send_message(user_input, stream=True)
    for chunk in response:
        print(chunk.text)



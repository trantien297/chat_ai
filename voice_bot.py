import speech_recognition as sr
import pyttsx3
from gpt4all import GPT4All

# Load mô hình GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Cài đặt text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Hàm để lắng nghe người dùng
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bạn nói gì đó...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(f"Bạn nói: {text}")
            return text
        except:
            print("Không nhận diện được.")
            return None

# Hàm để nói lại phản hồi
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Promt chat
def inputPromt():
    user_input = input("####### You: ")
    return user_input

# Vòng lặp chính
with model.chat_session():
    while True:
        # query = listen()
        query = inputPromt()
        if query:
            response = model.generate(query, max_tokens=256)
            print(f"AI: {response}")
            speak(response)

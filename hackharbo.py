# hackharbo.py

import speech_recognition as sr
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        start_time = time.time()
        query = recognizer.recognize_google(audio)
        end_time = time.time()
        response_time = end_time - start_time
        return query, response_time
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand.", 0
    except sr.RequestError:
        return "Service is down.", 0

def generate_response(query):
    query = query.lower()
    if "pest" in query:
        return "To control pests, try using neem oil spray every 5 days."
    elif "water" in query:
        return "Water your crops early in the morning or late in the evening."
    elif "weather" in query:
        return "Expect moderate rain this week. Take protective measures."
    else:
        return "Sorry, I don't have information on that yet."

def calculate_usability_score(accuracy, response_time):
    if response_time == 0:
        return 0
    return round(accuracy / response_time, 2)

def main():
    print("Welcome to HackHarbo - Voice Farming Assistant")
    speak("Welcome to HackHarbo. Please ask your farming question after the beep.")
    
    query, response_time = get_voice_input()
    print(f"You said: {query}")
    
    if query in ["Sorry, I couldn't understand.", "Service is down."]:
        speak(query)
        return

    # Simulated accuracy based on confidence (for prototype purposes)
    accuracy = 0.9  # Placeholder - normally you'd calculate or estimate this
    
    response = generate_response(query)
    speak(response)
    print(f"Response: {response}")
    
    usability = calculate_usability_score(accuracy, response_time)
    print(f"Usability Score (U = A/T): {usability}")

if __name__ == "__main__":
    main()

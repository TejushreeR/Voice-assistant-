#Speech Recognition
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from googlesearch import search

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user input
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust to background noise
            audio = recognizer.listen(source)  # Capture audio
            print("Audio captured, recognizing...")
            command = recognizer.recognize_google(audio)  # Recognize using Google API
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        speak("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Error with speech recognition service: {e}")
        speak("There was an issue with the speech recognition service.")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        speak("An unexpected error occurred.")
        return ""

# Function to perform a web search
def web_search(query):
    try:
        speak(f"Searching the web for {query}.")
        print(f"Searching the web for: {query}")
        results = list(search(query, num_results=3))  # Adjust num_results as needed
        if results:
            speak("Here are the top results I found.")
            for idx, result in enumerate(results, start=1):
                #speak(f"Result {idx}: {result}")
                print(f"Result {idx}: {result}")
        else:
            speak("Sorry, I couldn't find any results.")
            print("No results found.")
    except Exception as e:
        speak("An error occurred during the search.")
        print(f"Error: {e}")

# Function to respond to commands
def respond(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "who are you" in command:
        speak("I am your personal voice assistant.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")  # 12-hour format with AM/PM
        speak(f"The current time is {current_time}.")
        print(f"The current time is {current_time}.")
    elif "date" in command or "day" in command:
        today = datetime.now()
        current_date = today.strftime("%A, %B %d, %Y")  # Example: "Wednesday, November 28, 2024"
        speak(f"Today is {current_date}.")
        print(f"Today is {current_date}.")
    elif "search for" in command or "find" in command:
        query = command.replace("search for", "").replace("find", "").strip()
        web_search(query)
    else:
        speak("I didn't understand that. Can you repeat?")
    return True

# Main function
def main():
    try:
        speak("Hello, I am your voice assistant. How can I help you?")
        while True:
            command = listen()
            if command:
                if not respond(command):
                    break
    except KeyboardInterrupt:
        speak("Goodbye!")
        print("Program interrupted. Exiting...")

# Entry point
if __name__ == "__main__":
    main()

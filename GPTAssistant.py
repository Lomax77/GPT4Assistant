import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import openai

# Set OpenAI API key
openai.api_key = "insert API key here"

# Initialize the text to speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def transcribe_audio_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Transcription error")
        return None

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        #set microphone as listening device
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
            #print the recorded command
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_assistant():
    while True:
        command = take_command()
        if command:
            if 'play' in command:
                song = command.replace('play', '')
                talk('Playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time_now = datetime.datetime.now().strftime('%I:%M %p')
                talk('The current time is ' + time_now)
            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            else:
                # Generate a response using ChatGPT for unrecognized commands
                response = generate_response(command)
                print(f"ChatGPT says: {response}")
                talk(response)
            #else:
                #talk('I did not understand the command.')

if __name__ == "__main__":
    listener = sr.Recognizer()
    run_assistant()

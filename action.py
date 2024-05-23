import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
import pywhatkit
import os
import requests
import time
import keyboard


def Action(data):
    user_data = data.lower()
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"
    
    elif "current location" in user_data:
        data = requests.get('https://ipinfo.io/json')
        data = data.json()
        text_to_speech.text_to_speech("your location is")
        return data["city"] + ", " + data["region"]
    
    
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hey, sir How i can help you")
        return "hey, sir How i can help you"
    
    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I'm fine sir what about you?")
        return "I'm fine sir what about you?"

    elif "whatsapp message" in user_data :
        user_data = user_data.replace("send", "")
        user_data = user_data.replace("whatsapp message", "")
        #user_data = user_data.replace("to", "")
        name = user_data

        if 'aparna' in name:
            numb= "+918859268489"
            text_to_speech.text_to_speech("What's The message for aparna")
            mess = speech_to_text.speech_to_text()
            pywhatkit.sendwhatmsg_instantly(numb,mess , 25, True, 15)
        
        elif 'samyak' in name:
            numb= "+918000504626"
            text_to_speech.text_to_speech("What's The message for samyak")
            mess = speech_to_text.speech_to_text()
            pywhatkit.sendwhatmsg_instantly(numb,mess , 25, True, 15)
        
        elif 'avisha' in name:
            numb= "+918791659600"
            text_to_speech.text_to_speech("What's The message for avisha")
            mess = speech_to_text.speech_to_text()
            pywhatkit.sendwhatmsg_instantly(numb,mess , 25, True, 15)
        
        else:
            numb= "+919634132929"
            text_to_speech.text_to_speech("What's The message for me")
            mess = speech_to_text.speech_to_text()
            pywhatkit.sendwhatmsg_instantly(numb,mess , 25, True, 15)

        text_to_speech.text_to_speech("message sent")
        return "message sent"


    elif "morning" in user_data:
        text_to_speech.text_to_speech("good morning sir How are you")
        return "good morning sir,How are you?"
    
    elif "afternoon" in user_data:
        text_to_speech.text_to_speech("good afternoon sir How are you")
        return "good afternoon sir,How are you?"
    
    elif "night" in user_data:
        text_to_speech.text_to_speech("good night sir Take care")
        return "good night sir,Take care!"
    
    elif "time" in user_data:
        current_time = datetime.datetime.now().time()
        Time = (str)(current_time.hour) + " Hour : " + (str)(current_time.minute) + " Minutes"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "exit" in user_data or "close" in user_data:
        text_to_speech.text_to_speech("ok sir Thank you")
        return "ok sir, Thank you!"

    elif "play" in user_data:
        #text_to_speech.text_to_speech("Hello sir, what can i play for you?")
        #query=speech_to_text.speech_to_text()
        query = user_data.split(' ', 1)[1]
        pywhatkit.playonyt(query)
        text_to_speech.text_to_speech("playing, enjoy your music")
        return "Playing, enjoy your music!"
    
     
    elif "youtube" in user_data or "youtube.com" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"

   # elif "google" in user_data or "google.com" in user_data:
    #    webbrowser.open("https://google.com/")
     #   text_to_speech.text_to_speech("google.com is now ready for you")
      #  return "google.com is now ready for you"
    
    elif "google search" in user_data:
        text_to_speech.text_to_speech("what do you want to search")
        query = speech_to_text.speech_to_text()
        pywhatkit.search(query)
        text_to_speech.text_to_speech("Your search is ready!")
        return "Your search is ready!"
    

        
    
    elif "give information" in user_data or "give info" in user_data:
        text_to_speech.text_to_speech("on what topic you want?")
        query = speech_to_text.speech_to_text()
        text_to_speech.text_to_speech("how much lines you want?")
        x= speech_to_text.speech_to_text()
        pywhatkit.info(query ,lines=x)
        return "Your matter is ready!"


    elif "weather" in user_data:
        #text_to_speech.text_to_speech("Of which city do you want")
        city = user_data.split()
        ans = weather.weather(city[-1]+"+weather")
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "restart" in user_data:
        text_to_speech.text_to_speech("restarting your system")
        os.system("shutdown /r")
       
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("shutting down your system")
        os.system("shutdown /s")
      

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"








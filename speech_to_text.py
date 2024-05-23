import googletrans
import speech_recognition as sr
translator = googletrans.Translator()

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)#(Problem Solved)
        voice= recognizer.listen(source)
    try:
        voice_data= recognizer.recognize_google(voice)
        #print(voice_data)
        return voice_data
        #translated = translator.translate(voice_data, dest='es')
        #print(translated.text)
        
    except sr.UnknownValueError:
       pass 
    except sr.RequestError:
        print("RequestError")
    except:
        pass


speech_to_text()

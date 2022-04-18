"""The parameters for pywhatkit to send whatsapp message
import pywhatkit as kit
kit.sendwhatmsg("+91(phone_number)",message ,time_hour ,time_min)

phone_num (required) - Phone number of target with country code

message (required) - Message that you want to sendwhatmsg

time_hour (required) - Hours at which you want to send message in 24 hour format

time_min (required) - Minutes at which you want to send message

Some common errors

CountryCodeException - Check if the phone number passed into the parameter has country code

Message not getting delivered - Check internet speed and increase wait_time to 30 or above

CallTimeException - The web takes some time to load so some delay is required,
make sure the seconds left is greater than the wait_time

SyntaxError - Make sure the first two parameters are string and the rest are int"""

import pywhatkit as kit



import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	

try:
		
	
	with sr.Microphone() as source2:
                                               
			
	   
	    print("speak")
	    r.adjust_for_ambient_noise(source2, duration=0.2)
			
	   
	    audio2 = r.listen(source2)
			
	   
	    MyText = r.recognize_google(audio2)
	    MyText = MyText.lower()

	    print("Did you say "+MyText)
	    SpeakText(MyText)
			
except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
except sr.UnknownValueError:
		print("unknown error occured")


kit.sendwhatmsg("+91(phone_number)",MyText,time_hour,time_min)
#change phone_number,time_hour,time_min as per your requirment

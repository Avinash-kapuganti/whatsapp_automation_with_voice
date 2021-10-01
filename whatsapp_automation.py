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
# Python program to translate
# speech to text and text to speech


# Python program to translate
# speech to text and text to speech


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
	
	
# Loop infinitely for user to
# speak



    # Exception handling to handle
	# exceptions at the runtime
try:
		
	# use the microphone as source for input.
	with sr.Microphone() as source2:
                                               
			
	    # wait for a second to let the recognizer
	    # adjust the energy threshold based on
	    # the surrounding noise level
	    print("speak")
	    r.adjust_for_ambient_noise(source2, duration=0.2)
			
	    #listens for the user's input
	    audio2 = r.listen(source2)
			
	    # Using ggogle to recognize audio
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

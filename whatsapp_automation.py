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

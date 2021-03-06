#http://people.ds.cam.ac.uk/ssb22/gradint/lexconvert.html
#http://stackoverflow.com/questions/11911028/python-arpabet-phonetic-transcription
#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "usctimit_ema_f1_006_010_10ms_in.wav")

# use "english.wav" as the audio source
r = sr.Recognizer()
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source) # read the entire WAV file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
    # instead of `r.recognize_google(audio, show_all=True)`
    
    '3273104794-i9tk1tq2bapcks205jo5er4fh6iq1t7m.apps.googleusercontent.com'
    'AIzaSyDv3V5ISyJZsVggrSfoXHTGqqTWPAnu_9I'
    from pprint import pprint
    print("Google Speech Recognition results:")
    #pprint(r.recognize_google(audio, key="AIzaSyDv3V5ISyJZsVggrSfoXHTGqqTWPAnu_9I", show_all=True)) # pretty-print the recognition result
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    from pprint import pprint
    print("Wit.ai recognition results:")
    #pprint(r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)) # pretty-print the recognition result
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "a63b8c86-331d-45f4-a797-25b9ce4f7c3f" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "wxnCVsxdwOMm" # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    from pprint import pprint
    print("IBM Speech to Text results:")
    pprint(r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=False)) # pretty-print the recognition result
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

# recognize speech using AT&T Speech to Text
ATT_APP_KEY = "INSERT AT&T SPEECH TO TEXT APP KEY HERE" # AT&T Speech to Text app keys are 32-character lowercase alphanumeric strings
ATT_APP_SECRET = "INSERT AT&T SPEECH TO TEXT APP SECRET HERE" # AT&T Speech to Text app secrets are 32-character lowercase alphanumeric strings
try:
    print("AT&T Speech to Text thinks you said " + r.recognize_att(audio, app_key=ATT_APP_KEY, app_secret=ATT_APP_SECRET))
except sr.UnknownValueError:
    print("AT&T Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from AT&T Speech to Text service; {0}".format(e))
import speech_recognition as sr
import soundfile as sf

recognizer = sr.Recognizer()

data, samplerate = sf.read('t_voice5769261631200560516.ogg')

result = recognizer.recognize_google(data, language='arabic')
print(result)


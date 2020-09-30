import pickle
file="myiris"
fileobj=open(file,'rb')
myiris=pickle.load(fileobj)
print(myiris)
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
for item in myiris:
    speak(item)
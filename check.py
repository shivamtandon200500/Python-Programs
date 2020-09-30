def speak(str):
    from win32com.client import Dispatch
    from time import time
    speak=Dispatch("SAPI.spVoice")
    print(str)
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=257de4bca55d4a8fa263f9d62aa66740')
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    arts=my_json['articles']
    print("Headlines of the day")
    for articles in arts:
        speak(articles['title'])
        print("Movings on to the next news...Listen carefully")

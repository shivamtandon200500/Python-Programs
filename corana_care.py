from pygame import mixer
from time import time
from datetime import datetime
import random
def play(file,s):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==s:
            mixer.music.stop()
            break
        else:
            mixer.music.rewind()
def note(msg):
    with open("corona.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_msg=time()
    msgsec=5

    while True:
        if time()-init_msg>msgsec:
            print("Wash hands. Press 'd' to stop alarm")
            play(random.choice(["Baby Robot_01.mp3","Donald Duck_01.mp3"]),"d")
            init_msg = time()
            note("Wash hands at")

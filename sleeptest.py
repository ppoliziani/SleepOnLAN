import subprocess

def sleep():
    print("sleeping")
    subprocess.call([r'C:\Users\Philip\Desktop\sleep.bat'])

if str(input("Do you want to sleep? y/n")) == "y":
    sleep()

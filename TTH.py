import subprocess
from os import system, name
import pyfiglet
import random

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')    


clear()
# while(True):
VER=2022.1
print(pyfiglet.figlet_format("T . T . H"))
    
print(f'                     version : {VER}\n')
print('[-] Tool Created by Anontech1 \n\n')
try:
        
        print('''[+] Ctrl+c to quit anytime [+]\n
[::] select any one options to text to handwriting [::]\n
[1] Text To Handwriting Through Wikipedia Page
[2] Text To Handwriting Through Manually Write
[3] Text To Handwriting Through Already Text File  
        ''')
        user=(input("select an option : "))
        print()
        print('[$] please wait [$]')
        
        if user == '1':
            subprocess.call('E:/SAQUIB/computerScience/python/python-project/text_to_handwriting_app/launchers/launch1.py',shell=True)
        elif user == '2':
            subprocess.call('E:/SAQUIB/computerScience/python/python-project/text_to_handwriting_app/launchers/launch2.py',shell=True)  
        elif user == '3':
            subprocess.call('E:/SAQUIB/computerScience/python/python-project/text_to_handwriting_app/launchers/launch3.py',shell=True)
  
except KeyboardInterrupt: 
        print('[+] thanks for using code [+]')  
        
       


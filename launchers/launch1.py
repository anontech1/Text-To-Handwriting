from pywhatkit import text_to_handwriting
import pyttsx3
import pyfiglet
import requests
from os import system, name
import os
from bs4 import BeautifulSoup

# just ignore
l1=['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]','[10]','[11]','[12]','[13]','[14]','[15]','[16]','[17]','[18]','[19]','[21]','[22]','[23]','[24]','[25]','[26]','[27]','[28]','[29]','[30]']

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def speak():    
    engine = pyttsx3.init()
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 1.9)
    engine.say("complete")
    engine.say("check the file")
    engine.runAndWait()

clear()
try:    
                a=input('enter the wikipedia url to text to handwriting : ')
                print()
                b=int(input('enter the paragragh no : '))
                print()
                c=input('''without .png
enter the file name : ''')
                filename=(f'{c}.png')
                page=requests.get(a)
                soup=BeautifulSoup(page.content,'html.parser')
                d  = soup.find_all('p')[b].get_text()
    
     #try and first of all pehle ye text me lekhe ga aur file save karega

                with open('text.txt','w')as f:
                        f.write(d)
  
                with open('text.txt','r')as f:
                        content = f.read()

                for word in l1:
                        content= content.replace(word,"")
      
                with open('text.txt','w')as f:
                        f.write(content)
                        
                text_to_handwriting(content,save_to=filename,rgb=(0, 0, 138))
            
                if 'Other reasons this message may be displayed' in content:
                        print('not found')
                        os.remove(c)
                
                os.remove('text.txt') 
            
                clear()
                print('[#] complete [#]')
                speak()
                print('\n')
except KeyboardInterrupt:
                print('thanks for using this code\n')
except Exception as e:
                clear()
                print(f'ERROR : {e}')
                print('\n')
        

 
          












































































# while True:

#   print(Fore.RED+ '''
#                                   introducing TTH

# This script is for special student, you will be able to convert text to handwriting.
# this script for an educational purpose!!!!!
#   ''') 


#   input(Fore.WHITE+'Please enter key to start')
  

#   a=pyfiglet.figlet_format("T . T . H")
#   print(a)

#   apr = input(Fore.GREEN+'[#]' " Please enter the info to handwriting for convert : ")
#   try:
#         rr=wk.summary(apr)
#   except:
#     print("not found")
#     break
#   print()
#   print()
#   app = input('''
#  Example : writing.png
# [#] Please enter the name of this file : ''')
     
#   print()
#   print()
#   rgb = input('''
#   1-green
#   2-blue
# [#] Enter the color name to change text color : ''')
#   os.system("cls")
#   os.system("clear")
#   print("Please wait")
# # for i in tqdm(range(100)):  
# #   sleep(.05) 

#   if rgb=="blue":
#          print("Please wait...")
#          print(p.text_to_handwriting(rr,app,[0, 0, 138]))
#          os.system("cls")
#          os.system("clear")
#          print("-"*50)
#          print("      ----complete----") 
#          print("----PLease check the file----")
#          print("-"*50)
#   elif rgb=="green":
#          print("Please wait...")
#          print(p.text_to_handwriting(rr,app,[0, 128, 0]))
#          os.system("cls")
#          os.system("clear")
#          print("-"*50)
#          print("      ----complete----") 
#          print("----PLease check the file----")
#          print("-"*50)         
#   else:
#     print( Fore.RED+"[!] please correct the color name in the below")
#     ww = input(Fore.LIGHTRED_EX+"Restart for press 'r' and quit to 'q' ")
#     if ww=="r":
#      print()
#     elif ww=="q":
#         print( Fore.GREEN+"-"*50)
#         print( Fore.GREEN+"thanks for visiting")
#         print( Fore.GREEN+"-"*50)
#   break

  

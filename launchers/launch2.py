from pywhatkit import text_to_handwriting
import pyttsx3
from os import system, name

# create funtion to speak when complete program
def speak():    
    engine = pyttsx3.init()
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 1.9)
    engine.say("complete")
    engine.say("check the file")
    engine.runAndWait()
    
# create funtion to clear screen to any oerating system cli    
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')    

    
clear()   
try:
     a=input('[+] write the words to convert text to handwriting:\n\n ')
     print()
     c=input('[+] enter the file name : ')
     use=(f'{c}.png')
     print()
     print('[$] wait [$]')
     text_to_handwriting(a,save_to=use,rgb=(0, 0, 138))
     speak()
     clear()
     print('[#] complete [#]\n')
     

except KeyboardInterrupt:
     print('quit')
except Exception as e:
     print(f'ERROR : {e}')
     





          














































































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
#    rr=wk.summary(apr)
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

  

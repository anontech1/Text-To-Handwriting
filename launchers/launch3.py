import pywhatkit as kit
import pyfiglet
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
clear()

try:
    a=input('enter the path of file : ')
    print()
    b=input('''by default = C:/Users/name
enter the path to save file : ''')

    with open(a, 'r') as f:
        a = f.read()
        kit.text_to_handwriting(a,save_to=b,rgb=(0, 0, 138))
        clear()
        print('[#] complete [#]')
except KeyboardInterrupt:
    print('**quit**') 
           
except Exception as e:
    print(f'ERROR : {e}')  
      


    

#  E:/SAQUIB/computerScience/python/python-project/test.txt

# a=pyfiglet.figlet_format('sorry , undermaintance !')
# print(a)
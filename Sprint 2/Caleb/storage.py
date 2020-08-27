# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:47:53 2020

@author: Remy
"""

#List of dictionaries 
import update 
import ast 

file = open('dictionary_test.txt','r') 
a = file.read()
nested = ast.literal_eval(a) 
file.close() 


while True:
    
    print("Welcome to the dictionary tool: ")
    print("================================")
    print('1. View Stock Keys\n2. Add/Update Keys \n3. Del Keys'\
          '\n4. Add Stock\nPress <Q> to go back\n ')
    home = input()
    if home == '1' or home == '2' or home == '3' or home == '4':
        if home == '1': 
            while True: 
                print("\nWhat stock would you like to view?\n")
                screen_1 = input()
                if screen_1 == 'Q': 
                    break 
                FOUND = 'NO' 
                if screen_1 in nested: 
                        print('\nWe found it') 
                        print(nested[screen_1]) 
                        FOUND = 'YES' 
                if FOUND == 'NO':
                    print('\nWe were not able to find that')

        elif home == '2': 
            while True: 
                print("\nPlease enter Stock Ticker Symbol: \n")
                screen_1 = input() 
                if screen_1 == 'Q': 
                    break 
                FOUND = 'NO'              
                if screen_1 in nested:
                    print('Current Key Layout for ',screen_1,'\n',nested[screen_1])
                    print('\nWhat key are you adding: ') 
                    screen_2 = input() 
                    if screen_2 == 'Q': 
                        break 
                    print('\nEnter value for ',screen_2,'in ',screen_1,': ') 
                    screen_3 = input()
                    if screen_3 == 'Q':
                        break 
                    nested[screen_1][screen_2] = screen_3 
                    print('\nSuccessfully Done\n')
                    print('Current Key Layout for ',screen_1,'\n',nested[screen_1])
                    FOUND = 'YES' 
                if FOUND == 'NO':
                    print('\nWe were not able to find that')
            
        elif home == '3': 
            while True: 
                print("\nPlease enter Stock Ticker Symbol: \n")
                screen_1 = input() 
                if screen_1 == 'Q': 
                    break 
                FOUND = 'NO'              
                if screen_1 in nested: 
                    print('Current Key Layout for ',screen_1,'\n',nested[screen_1])
                    print('\nWhat key are you deleting: ') 
                    screen_2 = input() 
                    if screen_2 == 'Q': 
                        break 
                    del nested[screen_1][screen_2]
                    print('\nSuccessfully Done\n')
                    print('Current Key Layout for ',screen_1,'\n',nested[screen_1])
                    FOUND = 'YES' 
                if FOUND == 'NO':
                    print('\nWe were not able to find that') 
        else: 
            while True: 
                print("\nEnter a stock symbol to add: \n")
                screen_1 = input() 
                if screen_1 == 'Q':
                    break  
                #print(screen_1)
                nested[screen_1] = {'Name' : 'Default'}  
                print('Current Key Layout for ',screen_1,'\n',nested[screen_1])
                
    
    else: 
        print('Not a valid option\n') 
        if home == 'Q':
            break 
        
file = open('dictionary_test.txt', 'w')
file.write(str(nested))
file.close()

  
    
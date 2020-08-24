# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:47:53 2020

@author: Remy
"""

#List of dictionaries 
from temp_ import names 
from save_ import nested 
import csv 

while True:
    
    print("Welcome to the dictionary tool: ")
    print("================================")
    print('1. View\n2. Add\n3. Del\n4. Update\nPress <Q> to go back\n ')
    home = input()
    if home == '1' or home == '2' or home == '3' or home == '4':
        if home == '1': 
            while True: 
                print("\nWhat stock would you like to view?\n")
                screen_1 = input() 
                if screen_1 == 'Q': 
                    break 
                FOUND = 'NO' 
                for i in range(len(names)):  
                    if screen_1 == names[i]: 
                        print('\nWe found it') 
                        print(nested[screen_1]) 
                        FOUND = 'YES' 
                        break 
                if FOUND == 'NO':
                    print('\nWe were not able to find that')

        elif home == '2': 
            while True: 
                print("\nPlease enter Stock Ticker Symbol: \n")
                screen_1 = input() 
                if screen_1 == 'Q': 
                    break 
                FOUND = 'NO' 
                for i in range(len(names)):  
                    if screen_1 == names[i]: 
                        print('\nWhat key are you adding: ') 
                        screen_2 = input() 
                        if screen_2 == 'Q': 
                            break 
                        print('\nEnter value for ',screen_2,'in ',screen_1,': ') 
                        screen_3 = input()
                        if screen_3 == 'Q':
                            break 
                        nested[screen_1][screen_2] = screen_3 
                        #print('\nSuccessfully Done\n')
                        FOUND = 'YES' 
                        break 
                if FOUND == 'NO':
                    print('\nWe were not able to find that')
            
        elif home == '3': 
            while True: 
                print("\nWhat stock would you like to view?\n")
                screen_1 = input() 
                print(screen_1)
                if screen_1 == 'Q':
                    break  
        else: 
            while True: 
                print("\nWhat stock would you like to view?\n")
                screen_1 = input() 
                print(screen_1)
                if screen_1 == 'Q':
                    break  
    
    else: 
        print('Not a valid option\n') 
        if home == 'Q':
            break 
        
file = open('dictionary_test.txt', 'w')
file.write(str(nested))
file.close()

  
    
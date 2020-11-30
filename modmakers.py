import pandas as pd
import numpy as np


mod_values = pd.read_csv('modification.csv')

print(mod_values.head())

print(mod_values['Name'].tolist())

selected_mod = mod_values.loc[mod_values['Name'] == 'Should not be there']

print(selected_mod)

'''
while(True):
    answer = input("Would you like to continue[y/n]?")
    answer = answer.lower()
    if answer == 'n' or answer == 'no':
        new_values.to_csv('modification.csv')
        break
    
    name = input("Name: ")
    des = input("Description: ")
    basemod = input("Base Moditication: ")
    mod_opt = input("Mod Options: ")
    price = input("Price: ")
    hp = input("HP: ")
    rarity = input("Rarity: ")
    book = input("Book: ")

    data_dict = {'Name':name, 'Description':des, 'Base Modification':basemod, 'Mod Options':mod_opt,'Price':price, 'HP' : hp, 'Rarity': rarity, 'Book': book}
    new_values = new_values.append(data_dict, ignore_index=True)
    print("_________________________________________________")
    print(new_values)

'''
# name = 'Droid Brain Defense System'
# des = 'Using a droid brain chip and installing a set of sensors on the armour, the wearer is alerted to incoming fire in some fashion. More advanced versions include mini repulsor generators that push the wearer out of harm\'s way.'
# basemod = 'Defense +1.'
# mod_opt = '1x \"Defense +1 when taking Guarded Stance maneuver.\"'
# price = '5000'
# hp = '3'
# rarity = '6'
# book = 'Engineer career; [SWA47] Fully Operational'

# col_names = ['Name', 'Description', 'Base Modification', 'Mod Options' ,'Price', 'HP', 'Rarity', 'Book/Link']
# data_list = [(name, des, basemod, mod_opt, price, hp, rarity, book)]

# mods = pd.DataFrame(data_list, columns=col_names)
# new_values = mods

import pandas as pd
import numpy as np
import random


def run_complaint():
    number_complaint = random.randint(0,10)
    complain = ['Yo, you good fam?', 'You\'re pretty indesisive huh?', 'It\'s two letters?', 'Dude, choose a letter.', 'Okay, you got this fam. Choose a letter.', 'Low key impressed you haven\'t chosen yet.', 'Are you confused?', 'Do you need help?', 'Exit the program whenever you want dude.', 'Are you trapped?', 'Do you feel trapped']
    print(complain[number_complaint])

def build_database():
    col_string = input('An example input: first_col, second_col, third_col, fourth_col\nSpecify the columns you would like to see: ')
    col_names = col_string.split(',')
    row_string = input('Example Data input: first_col_data, second_col_data, third_col_data, fourth_col_data\nInput data: ')
    data = row_string.split(',')


if __name__ == "__main__":    
    # Set it up so they can either creat a document or edit an alread existing one
    num = 0
    while(1):
        val = input("Would you like to create or edit a document?[c/e]")
        option = val.lower()
        if num > 1:
            run_complaint()

        if val.lower() == 'c':
            print("You have chosen to create a CSV document")
            new_mod_database = build_database()
            break
        if val.lower() == 'e':
            print("You have chosen to edit a CSV document")
            file_name = input("Please specify path to document (if in same directory, this will be the file name): ")
            break
        print(val + " is not a valid response. Please enter a valid response.")
        num+=1

    
    # for testing
    file_name = 'modification.csv'

    mod_values = pd.read_csv(file_name)

    # print(mod_values.head())
    # print(mod_values['Name'].tolist())
    # selected_mod = mod_values.loc[mod_values['Name'] == 'Droid Brain Defense System']
    # selected_mod.empty == true if empty false if not
    # print(selected_mod.empty)

    while(True):
        answer = input("Would you like to continue[y/n]?")
        answer = answer.lower()
        if answer == 'n' or answer == 'no':
            mod_values.to_csv('modification.csv')
            break
        
        name = input("Name: ")
        selected_mod = mod_values.loc[mod_values['Name'] == name]
        if selected_mod.empty:
            des = input("Description: ")
            basemod = input("Base Moditication: ")
            mod_opt = input("Mod Options: ")
            price = input("Price: ")
            hp = input("HP: ")
            rarity = input("Rarity: ")
            book = input("Book: ")

            data_dict = {'Name':name, 'Description':des, 'Base Modification':basemod, 'Mod Options':mod_opt,'Price':price, 'HP' : hp, 'Rarity': rarity, 'Book': book}
            mod_values = mod_values.append(data_dict, ignore_index=True)
            print("_________________________________________________")
            print(mod_values)
        else:
            print("\nMod " + name + " has already been added to the csv file \n_______________________________________________\n")
            print(selected_mod)
            update = input("_______________________________________________\nWould you like to upgrade the specs [y/n]?")
            if update.lower() == 'y' or update.lower() == 'yes':
                # //update the thing
                print("Cool")
                mod_values.drop(name, axis=0)

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

#######################################################################
# Filename:  assetBalancerMain.py
# Author:    Alex Bange
#######################################################################
# Purpose:
#   To serve as the backend of the assetBalancer application
#
# Usage
#   DOS> python assetBalancer.py
#
# Functions
#     get_test_sheet_data() : Collects and returns data from defined
#                             google drive sheet.
#
#
#
#
#
#
# Assumptions
#   A) python is in the PATH
#######################################################################
import os
import time
import sys
import pprint
import gspread
from collections import namedtuple
import re
#import pickle
from oauth2client.service_account import ServiceAccountCredentials

# Define the current working directory and locations for save/config files
CONFIGFILENAME = 'config.dat'
SAVEFILENAME = 'save.txt'
CONFIGFILEPATH = os.getcwd() + CONFIGFILENAME
SAVEFILEPATH = os.getcwd() + SAVEFILENAME

TURRET_ATTRIBUTE_LIST = ['turret_name', 'burst', 'fire_rate', 'hull_dmg', 'shield_dmg', 'sound_name', 'random', 'man_accuracy', 'life_time', 'laser_thickness', 'speed', 'burst_time_in_between', 'price', 'color']

# Create a method to cleanly display collected sheet contents
pp = pprint.PrettyPrinter()

# Identify the name of the script
gsScriptName = os.path.basename(__file__

# Provide credidentials to google API, collect and display information from selected sheet
def get_turret_sheet_data():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('drive_client.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Expanse Spreadsheets').worksheet('TurretData')
    sheet_contents = sheet.get_all_records()
    return sheet_contents

# Take turret sheet output and log it's contents as objects under the Turret class.
def clean_turret_sheet_data(currentTurrets):
    i = 0
    b = 0
    selected_item_list = []
    for dict in currentTurrets:
        selected_turret = currentTurrets[i]
        for key, value in selected_turret.items():
            temp = [key, value]
            selected_item_list.append(temp)
        copyable = selected_item_list[b][1]
        b += 1
        turret_name = selected_item_list[b][1]
        b += 1
        burst = selected_item_list[b][1]
        b += 1
        fire_rate = selected_item_list[b][1]
        b += 1
        hull_dmg = selected_item_list[b][1]
        b += 1
        shield_dmg = selected_item_list[b][1]
        b += 1
        sound_name = selected_item_list[b][1]
        b += 1
        random = selected_item_list[b][1]
        b += 1
        man_accuracy = selected_item_list[b][1]
        b += 1
        life_time = selected_item_list[b][1]
        b += 1
        laser_thickness = selected_item_list[b][1]
        b += 1
        speed = selected_item_list[b][1]
        b += 1
        burst_time_in_between = selected_item_list[b][1]
        b += 2
        price = selected_item_list[b][1]
        b += 2
        color= selected_item_list[b][1]
        b += 1
        turretList[i] = Turret(copyable, turret_name, burst, fire_rate, hull_dmg, shield_dmg, sound_name, random, man_accuracy, life_time, laser_thickness, speed, burst_time_in_between, price, color)
        print(turretList[i].turret_name, "logged!")
        i += 1

# Create a list of all the turrets in the sheet
def build_turret_list(raw_turret_sheet_data):
    list_of_turrets = []
    i = len(raw_turret_sheet_data)
    b = 0
    for list in raw_turret_sheet_data:
        current_turret = rawTurretSheetContents[b]
        current_turret_name = current_turret['TurretName']
        list_of_turrets.append(current_turret_name)
        print("Added %s to name list" % current_turret_name)
        if b == i:
            break
        else:
            b += 1
    return list_of_turrets


def clean_turret_sheet_data(currentTurrets):
    _Turret = namedtuple('Turret',
                         [to_underscore(k) for k in currentTurrets[0].keys()])

    class Turret(_Turret):
        __slots__ = ()

        def is_fast(self):
            return self.speed > 500

    instances = [
        Turret(**dict((to_underscore(k), v) for k, v in t.items()))
        for t in currentTurrets]

    return dict((t.turret_name, t) for t in instances)

def initialize_turret_list():
    pass


def to_underscore(word):
    return '_'.join(x.lower() for x in re.findall(r'[A-Z]+[a-z]*', word))

def clean_turret_sheet_data(currentTurrets):
    return [Turret(**t) for t in currentTurrets]
    # or [Turret(*t.values()) for t in currentTurrets] if attribute names are changed from the initial data.

### PROGRAM STARTS HERE
# Print the date/time when this script started
print("%s has started as of %s." % (gsScriptName, time.strftime("%c")))

# Pull turret sheet data from google drive and assign it to "rawTurretSheetContents"
rawTurretSheetContents = get_turret_sheet_data()

turret_by_name = clean_turret_sheet_data(rawTurretSheetContents)

print(turret_by_name.keys())
print(turret_by_name['SmallSuppressor'].burst)
print('SmallSuppressor is fast:', turret_by_name['SmallSuppressor'].is_fast())


# Convert raw turret sheet data into identified class objects under the "Turret" class
clean_turret_sheet_data(rawTurretSheetContents)
#print(SmallSuppressor.burst)

# Print the date/time when this script finished
print("%s has finished as of %s." % (gsScriptName, time.strftime("%c")))
print("Press enter to exit.")
input()
# Python script ends here
sys.exit(0)
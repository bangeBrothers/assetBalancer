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
gsScriptName = os.path.basename(__file__)


class Turret:
    def __init__(self, copyable, turret_name, burst, fire_rate, hull_dmg, shield_dmg, sound_name, random, man_accuracy, life_time, laser_thickness, speed, burst_time_in_between, price, color):
        self.copyable = copyable
        self.turret_name = turret_name
        self.burst = burst
        self.fire_rate = fire_rate
        self.hull_damage = hull_dmg
        self.shield_damage = shield_dmg
        self.sound_name = sound_name
        self.random = random
        self.man_accuracy = man_accuracy
        self.life_time = life_time
        self.laser_thickness = laser_thickness
        self.speed = speed
        self.burst_time_in_between = burst_time_in_between
        self.price = price
        self.color = color

class TurretProcessDirector:
    def __init__(self):
        self.allClasses = []

    def construct(self, builderName):
        targetClass = getattr(Turret, builderName)
        instance = targetClass()
        self.allClasses.append(instance)

director = TurretProcessDirector()

class Test:
    pass


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
        for id in turretList[1]:
            director.construct(copyable, turret_name, burst, fire_rate, hull_dmg, shield_dmg, sound_name, random, man_accuracy, life_time, laser_thickness, speed, burst_time_in_between, price, color)
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

def initialize_turret_list():
    pass

### PROGRAM STARTS HERE
# Print the date/time when this script started
print("%s has started as of %s." % (gsScriptName, time.strftime("%c")))

# Pull turret sheet data from google drive and assign it to "rawTurretSheetContents"
rawTurretSheetContents = get_turret_sheet_data()

turretList = build_turret_list(rawTurretSheetContents)
print(turretList)
print(SmallSuppressor.burst)

turretList[1] = Test()


print(turretList)
# Convert raw turret sheet data into identified class objects under the "Turret" class
clean_turret_sheet_data(rawTurretSheetContents)
#print(SmallSuppressor.burst)

# Print the date/time when this script finished
print("%s has finished as of %s." % (gsScriptName, time.strftime("%c")))
print("Press enter to exit.")
input()
# Python script ends here
sys.exit(0)
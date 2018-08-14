#######################################################################
# Filename:  assetBalancerMain.py
# Author:    Alex Bange
#######################################################################
# Purpose:
#   To serve as the backend of the assetBalancer application
#
# Usage
#   DOS> python sample.py
#
# Assumptions
#   A) python is in the PATH
#######################################################################
import os
import time
import sys
import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create a method to cleanly display collected sheet contents
pp = pprint.PrettyPrinter()

# Identify the name of the script
gsScriptName = os.path.basename(__file__)


# Provide credidentials to google API, collect and display information from selected sheet
def get_test_sheet_data():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('drive_client.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Test Sheet').sheet1
    sheet_contents = sheet.get_all_records()
    return sheet_contents


# Print the date/time when this script started
print("%s has started as of %s." % (gsScriptName, time.strftime("%c")))

# PROGRAM STARTS HERE
testSheetContents = get_test_sheet_data()

pp.print(testSheetContents)


# Print the date/time when this script finished
print("%s has finished as of %s." % (gsScriptName, time.strftime("%c")))
print("Press enter to exit.")
input()
# Python script ends here
sys.exit(0)
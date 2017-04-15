#!/usr/bin/python
import os
import json
import sys
import time
import datetime

import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 22

spreadsheet = None
worksheet = None

try:
  scope =  ['https://spreadsheets.google.com/feeds']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
  gc = gspread.authorize(credentials)
  spreadsheet = gc.open_by_key(os.environ['RPI_SPREADSHEET_KEY'])
  worksheet = spreadsheet.worksheet(os.environ['RPI_LOCATION'])
except Exception as ex:
  print('Login Error:', ex)
  sys.exit(1)

humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

if humidity is None or temp is None:
  print('Invalid Data')
  sys.exit(1)

try:
  worksheet.append_row((datetime.datetime.now(), temp, humidity))
except Exception as ex:
  print('Append Error:', ex)
  sys.exit(1)

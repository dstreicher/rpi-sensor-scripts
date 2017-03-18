## rpi-sensor-scripts

A collection of command line scripts intended for use with raspberry pi zero units.

### Dependencies
```
sudo apt-get install python-pip
sudo pip install gspread oauth2client
```

### Setup Notes
* You will need to create a Google API service account and download the private key file for use as credentials.
* Rename the credentials file to "credentials.json".
* Share the google drive spreadsheet with the service account's email for edit access (ex. rpi-sensors@xxx-xxxx.iam.gserviceaccount.com)
* Update your bash profile with the custom environmental variables used by these scripts.
* Setup a cron job to run the python script when desired. (ex. */15 * * * * /home/pi/rpi-sensor-scripts/log-dht22-data.py)

### Environmental Variables
* RPI_SPREADSHEET_KEY: used for opening to desired spreadsheet from Google Sheets. (located in the spreadsheet url)
* RPI_LOCATION: used for logging the location descriptor in which the sensor is stationed.
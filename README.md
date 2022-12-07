# clamav-web-api

## Clamd Setup
Default install location is C:\Program Files\ClamAV
Move both .config example files from /examples into main ClamAV folder
Rename file extensions to get rid of ".example"
Open the file and comment out the requested line near the top

run `freshclam` to populate the database

## Start the clamd Deamon
Either this needs to be running as a Windows service or in a terminal by running `clamd`

##Run server

`uvicorn main:app --reload`

## App Routes

/healthcheck
/clamav-ping
/clamav-version

/scan-file

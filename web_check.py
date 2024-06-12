#!python3
# Website update check script.
import hashlib
import requests
import os

# URL to check
url = "https://mangadex.org/title/d86cf65b-5f6c-437d-a0af-19a31f94ec55/" +\
"ijiranaide-nagatoro-san?tab=chapters"

# Grab contents of URL to check
req = requests.get(url)

# Initialize sha256 hash method
hash = hashlib.sha256()

# Update hash method with URL data encoded to utf-8
hash.update(req.text.encode('utf-8'))

# Initialize hex variable to compare to prior hex value.
hex = hash.hexdigest()

# Relative file path for file to check
path = './check.txt'

try:
    # Check if path to file exists
    if os.path.exists(path):
        # Open file to be read and written to
        file = open(path, 'r+', encoding='utf-8')
        data = file.read()
        
        # Check if data in text file matches hex digest of URL content.
        # If so, notify user that website has not been.
        # Else, update file and notify user website has changed. 
        if data == hex:
            print('Website has not been updated.')
        else:
            print('Check site for updates!')
            file.write(hex)
        file.close()
    # If file does not exist, create a file.
    else:
        file = open(path, 'w', encoding='utf-8')
        file.write(hex)
        file.close()
        print('File has been created.')

except IOError:
    print('File not found or unable to write')

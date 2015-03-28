
# Imports
from bs4 import BeautifulSoup
import requests
import time
import os

# Function to get the status code of the URL
def checkIfDead (testlink):

	# Fetch the link
	r = requests.get(testlink)
	# Sleep half a second, to avoid getting blocked by the YouTube API
	time.sleep(0.5)
	# Return status code
	return(r.status_code)

# Load HTML, change this if you want to I guess
soup = BeautifulSoup(open('index.html'))

# Make an array, lol
deaded = []

# File to store output in
thefile = "rip.txt"

#For each:
for link in soup.find_all('a'):

	#Assign URL and ID to variable
    url = link.get('href')
    videoid = url[32:]
    xmlfeed = 'http://gdata.youtube.com/feeds/api/videos/' + videoid

    # Check if the video is dead
    result = checkIfDead(xmlfeed)

    # Shitty color coding and adds dead videos to the array
    if result == 404:
    	result = "\033[91m404\033[0m"
    	deaded.append(videoid)

    if result == 403:
    	result = "\033[91m403\033[0m"
    	deaded.append(videoid)

    # Output
    print(str(videoid) + " returned " + str(result))

# Delete output file if it already exists, because too lazy to check for duplicates
if os.path.isfile(thefile):
	os.remove(thefile)


# Write to the file
f = open(thefile, "w")
f.write("\n".join(map(lambda x: str(x), deaded)))
f.close()

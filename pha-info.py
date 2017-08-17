#import the library used to query a website
import urllib2
from bs4 import BeautifulSoup

print "Hello, world!"

phaStatesListURL = "https://portal.hud.gov/hudportal/HUD?src=/program_offices/public_indian_housing/pha/contacts/"

listOfStates = urllib2.urlopen(phaStatesListURL)

# getting the HTML page into BeauitfulSoup
soup = BeautifulSoup(listOfStates, "html.parser") 

# getting all <option> elements in the page
allOptionElements = soup.find_all("option")

# get the ID of each <option> element and build array of state URLs to query
stateURLArray = []
for optionElement in allOptionElements:
    stateURL = phaStatesListURL + str(optionElement.get("id").lower()) #URLs don't resolve on HUD.gov unless state abbrev. is lowercase
    stateURLArray.append(stateURL)

# create a text file, loop through array, and add each URL as new line
faqs = open("stateURLs.txt", "w+")
for arrayElement in stateURLArray:
    faqs.write("Where can I find rental information in " + arrayElement[-2:] + "?\n")
    faqs.write("Goto " + arrayElement + " to find more information.\n")
    faqs.write("\n")
faqs.close()


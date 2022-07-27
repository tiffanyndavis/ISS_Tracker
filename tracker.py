import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# Retrieve name of astronauts onboard ISS
astro_url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(astro_url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for person in people:
    file.write(person["name"] + " - onboard" + "\n")

# Find your current location from your IP address - given in lat and long
g = geocoder.ip("me")
file.write("\n Your current lat / long is: " + str(g.latlng))
file.close
webbrowser.open("iss.txt")

# Set up graphical tracker in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load map gif
screen.bgpic("Images/map.gif")
screen.register_shape("Images/iss.gif")

# Move ISS Icon
iss = turtle.Turtle()
iss.shape("Images/iss.gif")
iss.setheading(45)
iss.penup()

# input("stop")

# Get starting position for ISS
## Pull initial position data from NASA API json file 
ISS_url_int = "http://api.open-notify.org/iss-now.json"
response_int = urllib.request.urlopen(ISS_url_int)
result_int = json.loads(response_int.read())
location_int = result_int["iss_position"]

## Get initial lat and long location 
lat_int = float(location_int["latitude"])
long_int = float(location_int["longitude"])

# Go to initial position and then put the pen down for trace lines
iss.goto(long_int, lat_int)
iss.pendown() # Comment this out if you don't want trace lines
# iss.pendown()


while True:
    # Load the status of ISS in real time. 
    ISS_url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(ISS_url)
    result = json.loads(response.read())

    # Extract ISS location
    location = result["iss_position"]
    lat = location["latitude"]
    long = location["longitude"]

    # Print lat/long to text file
    lat = float(lat)
    long = float(long)
    print("\n Latitude: " + str(lat))
    print("\n Longitude: " + str(long))
    # file.write("\n The latitude of the ISS ")

    # Update ISS location on map
    iss.goto(long, lat)

    # Refresh each 5 seconds
    time.sleep(5)
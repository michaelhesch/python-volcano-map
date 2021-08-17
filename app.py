# import folium library to build web map files
# import pandas for data processing
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html= """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
# create map variable to hold folium map data
map = folium.Map(location=[39.58589540888904, -119.87107331602643], zoom_start=5, tiles = "Stamen Terrain")
# create a new feature group, holds multiple features
# helps when adding layer control feature to map
fg = folium.FeatureGroup(name="My Map")
# add elements to feature group object, such as markers
# easily loop through coordinates to add multiple markers
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(
        location=[lt, ln], 
        popup=folium.Popup(iframe), 
        icon = folium.Icon(color = "green")
        ))


map.add_child(fg)
# generate map html file based on Map method inputs
map.save("map.html")
# import folium library to build web map files
# import pandas for data processing
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# function to assign marker color based on elevation
def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# iframe content to display in markers
html= """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %sm
"""
# create map variable to hold folium map data
map = folium.Map(location=[39.9299, -104.8962], zoom_start=5, tiles = "Stamen Terrain")
# create a new feature group for population layer
# helps when adding layer control feature to map
fgp = folium.FeatureGroup(name="Volcano Locations")
# add elements to feature group object, such as markers
# loop through coordinates, elevation and name to add markers
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgp.add_child(folium.CircleMarker(
        location=[lt, ln], 
        popup=folium.Popup(iframe), 
        radius=7,
        fill_color=color_producer(el),
        fill_opacity=0.7,
        color=color_producer(el)
        ))

# add new feature group for population map layer
fgv = folium.FeatureGroup(name="Population Map")
# import geojson data to add population map layer
fgv.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}
    ))

# add feature group to the map
map.add_child(fgv)
map.add_child(fgp)
# add layer control to map to allow selection of layers
# must be added after feature group is added to map
map.add_child(folium.LayerControl())
# generate map html file based on Map method inputs
map.save("map.html")
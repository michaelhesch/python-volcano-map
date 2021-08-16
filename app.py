# import folium library to build web map files
import folium

# create map variable to hold folium map data
map = folium.Map(location=[38.89046737174874, -77.03629387153447], zoom_start=6)
# generate map html file based on Map method inputs
map.save("map.html")
import folium
import pandas, os

print(os.getcwd())

#Dohnany = 49.146499, 18.288731
map = folium.Map(location=[49.146499, 18.288731], zoom_start=8, tiles="Mapbox Bright")
data = pandas.read_csv("References/sk.csv")

longt = list(data["Longtitude"])
lat = list(data["Latitude"])
nazov = list(data["Nazov"])
mesto = list(data["Mesto"])

#feature group Letiska
fgl = folium.FeatureGroup(name="Letiska")

for lt, ln, name, city in zip(lat, longt, nazov, mesto):
    #fg.add_child(folium.Marker(location=[lt,ln], popup="[ " + name + " ]", icon=folium.Icon(color='green')))
    fgl.add_child(folium.CircleMarker(location=[lt,ln], radius=7, popup="[ " + name + " ]", fill=True, fill_color = 'yellowgreen', color='grey', fill_opacity=0.7))

#feature group Populacia
fgp = folium.FeatureGroup(name="Populacia")

#add layer polygon and color by amount of citizens
fgp.add_child(folium.GeoJson(data=open(file='References/world.json', mode='r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 7000000
else 'orange' if 7000000 <= x['properties']['POP2005'] < 20000000 else 'blue'}))


map.add_child(fgl)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map4.html")



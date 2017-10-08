import folium
import pandas
data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<=3000:
        return 'blue'
    else:
        return 'orange'

map=folium.Map(location=[30,30],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="volcanoes")
fgp=folium.FeatureGroup(name="populayion")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<x['properties']['POP2005']<=20000000 else 'grey'}))
for la,lt,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[la,lt],radius=6,popup=str(el)+"m",fill=True,color='black',fill_color=color_producer(el),fill_opacity=0.7))
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")

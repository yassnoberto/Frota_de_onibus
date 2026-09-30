from folium import Map, Marker, Popup

m = Map(location=[-22.8773542,-47.2280647], zoom_start=14)
Marker(location=[-22.8773542,-47.2280647], popup=Popup("Estudo aqui!", max_width="100", show=True)).add_to(m)
m.save("unasp.html")
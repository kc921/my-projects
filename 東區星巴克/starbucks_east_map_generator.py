import folium
import json

center_location=[23.00049, 120.22025]
main_map = folium.Map(location=center_location,zoom_start=15,tiles='cartodbpositron')

desire_redius_km=5
for i in range(desire_redius_km,0,-1):
    folium.Circle(
        radius=i*1000,
        location=center_location,
        popup=str(i)+"km",
        color="#3186cc",
        opacity=0.5,
        fill=True,
        fill_color="#3186cc",
        fill_opacity=0.1
    ).add_to(main_map)

with open('starbucks_east_storeinfo.json',encoding='utf-8') as starbucksfile:
    starbucks_json=json.load(starbucksfile)
    for store in starbucks_json:
        coordinate=list(map(float,store["coordinate"].split(",")))
        folium.Marker(
            location=coordinate,
            popup=folium.Popup(
                html='<font size="3.5"><b>%s</b>\
                        <p>%s</p>\
                            <p>%s</p>\
                                <p>%s</p>\
                                    </font>'
                                    %(store['storename'],store['storeaddress'],store['storetel'],store['storehour']),
                max_width=200)
            # icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(main_map)

main_map.save("map_east.html")
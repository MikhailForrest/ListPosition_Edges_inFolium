import folium
import xml.etree.ElementTree as ET

class GeoPoint:
    """docstring"""
 
    def __init__(self, lat, lon):
        """Constructor"""
        self.lat = lat
        self.lon = lon

map1 = folium.Map(location=[56,92],
                    zoom_start=3, tiles="OpenStreetMap",attr=False, prefer_canvas=True)

with open("Lists\\2806_CPDLS_1.txt") as file: # 
    for item in file:
        l1 = (list(map(str, item.split()))) 
        print (l1) 
        if float(l1[2])<0:
            folium.Circle(location=[float(l1[1]),float(l1[2])+360]
                    ).add_to(map1)
            folium.Marker(location=[float(l1[1]),float(l1[2])+360],
                                    icon=folium.DivIcon(html=f'''<!DOCTYPE html><html><div style="font-size: 8pt"><p>{l1[0]}</p></div></html>''',
                                    class_name="mapText")).add_to(map1)
        else:
            folium.Circle(location=[float(l1[1]),float(l1[2])]).add_to(map1)
            folium.Marker(location=[float(l1[1]),float(l1[2])],
                                    icon=folium.DivIcon(html=f'''<!DOCTYPE html><html><div style="font-size: 8pt"><p>{l1[0]}</p></div></html>''',
                                    class_name="mapText")).add_to(map1)
       
files_list = ['azimut_Simferopol_e.xml',
              'иркутск_e.xml',
              'azimut_ЕкатеринбургЗЦ_e.xml',
              'azimut_КрасноярскРЦ_e.xml',
              'azimut_МоскваЗЦ_e.xml',
              'azimut_РостовнаДонуЗЦ_e.xml',
              'azimut_РФ_Красноярск_e.xml',
              'azimut_СамараЗЦ_e.xml',
              'azimut_СПБ_e.xml',
              'петропавловск_e.xml',
              'тюмень_e.xml',
              'калининград_e.xml',
              'магадан_e.xml',
              'Yakutsk_e.xml',
              'магадан_океан_e.xml',
              'Хабаровск2_e.xml']

for str_ in files_list: 
    tree1 = ET.parse(str_)
    root_1_0 = tree1.getroot()
    root_1_1 = root_1_0[1][0][1] #массив точек тут сразу
    list_of_coord= []
    for root_1_2 in root_1_1:
        if isinstance(root_1_2.text, str):
            list_h = root_1_2.text.split(' ') #разделение строки по указанному разделителю
            lat_ = int(list_h[0][1:3])+int(list_h[0][3:5])/60+int(list_h[0][5:])/(60*6000)
            lon_ = int(list_h[1][1:4])+int(list_h[1][4:6])/60+int(list_h[1][6:])/(60*6000)
            point = GeoPoint(lat_,lon_)   
            list_of_coord.append([point.lat,point.lon])  
    folium.PolyLine(list_of_coord, color='maroon',fill = False).add_to(map1) 

map1.save("results\\map_cpdlc.html")
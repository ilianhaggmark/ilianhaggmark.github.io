# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:22:22 2023

@author: SasakiLab2022
"""
  
def coordX(long):
    Rx = (841.94598)/(24.6-10.4) # width/(E-W)
    return Rx*(long - 10.4)+55.734

def coordY(lat):
    Ry = 1836.9969/(69.5-55.1); # height/(N-S)
    return 1836.9969 - Ry*(lat - 55.1) -0.385

typeOfLocation = ['stad','natur','done']


#def color2(x):
#    colors = ['red',0,0,'blue',0,'green',0,'violet',0,0,'orange','orange']
#    return colors[x-2012]

places = [
          (59.39710922010021, 15.841031196660374, 'Arboga',1,0,1),
          (65.82875940431215, 21.707105008502747, 'Boden',1,2012,1),
          (56.88018138589324, 16.656199633275918, 'Borgholm',1,0,1),
          (59.129601493444696, 18.4050570637092, 'Dalarö',1,2021,1),
          (57.66711462559346, 14.971111611503503, 'Eksjö',1,0,1),
          (59.37357718381151, 16.51593579955147, 'Eskilstuna',1,0,1),
          (60.60771341059942, 15.630855663192753, 'Falun',1,2004,1),
          (58.64742339550176, 17.109206660029493, 'Femörefortet (Oxelösund)',1,2020,1),
          (60.402558352346674, 18.175807118870267, 'Forsmark',1,0,1),
          (60.65165102657804, 17.3329616772296, 'Furuvik',1,0,1),
          (57.996966856951666, 19.180351067325436, 'Fårö',1,2021,1),
          (58.02499627489077, 14.470060817056053, 'Gränna',1,0,1),
          (60.67611418452718, 17.15112340707909, 'Gävle',1,0,1),
          (57.70808848807534, 11.97303531571852, 'Göteborg',1,0,1),
          (56.0437579631498, 12.694885229680578, 'Helsingborg',1,0,1),
          (61.72464733801412, 17.10808608265857, 'Hudiksvall',1,2024,1),
          (57.48671100512251, 15.846508117762362, 'Hultsfred',1,0,1),
          (62.63525118556932, 17.928643685967085, 'Härnösand',1,0,1),
          (67.8465908457675, 20.620966874573707, 'Jukkasjärvi',1,0,1),
          (57.784374423181355, 14.162915308296228, 'Jönköping',1,0,1),
          (56.66432631190559, 16.36558504978889, 'Kalmar',1,0,1),
          (56.16117814700011, 15.587152433755188, 'Karlskrona',1,2021,1),
          (59.38151293396853, 13.5064075618854, 'Karlstad',1,2004,1),
          (67.86840241021957, 20.199368058625232, 'Kiruna',1,2012,1),
          (58.66296666104759, 16.453172636164467, 'Kolmården',1,2012,1),
          (57.50435326352724, 12.079227801200114, 'Kungsbacka',1,2023,1),
          (60.75933817795975, 16.497608293810565, 'Kungsberget',1,0,1),
          (58.739608014657556, 17.865665428643357, 'Landsort',1,0,1),
          (58.41596266321811, 15.625686792610002, 'Linköping',1,0,1),
          (55.706759291270586, 13.18683260232447, 'Lund',1,0,1),
          (57.7106452974358, 16.445526755652836, 'Lunds by (Gladhammar)',1,0,1),
          (58.2718558549921, 11.433995466107303, 'Lysekil',1,2010,1),
          (57.36702002095904, 17.097052374721688, 'Långe Erik',1,2020,1),
          (56.19603800140997, 16.398514954645822, 'Långe Jan',1,2016,1),
          (59.25583741988396, 17.219910115827098, 'Mariefred',1,0,1),
          (58.712445187181736, 13.822664681787373, 'Mariestad',1,2021,1),
          (59.122151400431434, 18.57217182150647, 'Mörtö-Bunsö',2,0,1),
          (59.51952272919148, 15.040551853516453, 'Nora',1,0,1),
          (60.89103172859752, 15.096320920389577, 'Rättvik',1,2004,1),
          (59.61683878545008, 17.72165649614647, 'Sigtuna',1,0,1),
          (57.70122810164977, 15.087630150024438, 'Skurugata',2,0,1),
          (59.32505482910684, 18.070831457783417, 'Stockholm',1,0,1),
          (59.37559478021347, 17.03415714333523, 'Strängnäs',1,2021,1),
          (62.39078472827217, 17.30688718822829, 'Sundsvall',1,0,1),
          (58.48224996937162, 16.32546437692729, 'Söderköping',1,2020,1),
          (57.67888565750059, 14.08205272572794, 'Taberg',1,0,1),
          (58.9500761042884, 17.58463756208113, 'Tullgarn',1,2020,1),
          (59.855410436576925, 17.6320813652231, 'Uppsala',1,0,1),
          (57.479333120203385, 12.0022644816948, 'Valda',1,2021,1),
          (59.401942741593224, 18.35530211792741, 'Vaxholm',1,0,1),
          (57.64181765609941, 18.297948494825164, 'Visby',1,2021,1),
          (58.05511930190156, 14.34795267638752, 'Visingsö',1,0,1),
          (59.05325581914599, 12.709533700054495, 'Åmål',1,2024,1),
          (63.398814494284636, 13.081291294783462, 'Åre',1,0,1),
          (59.27394347174934, 15.215375916675129, 'Örebro',1,0,1)        
          ]


for i in range(len(places)):
    #print('<circle id=\'loc{}\' r=\'1\' cx=\'{}\' cy=\'{}\' stroke="black" stroke-width="0" fill="{}"><title>{}</title></circle>'
          #.format(i,coordX(places[i][1]),coordY(places[i][0]),color[places[i][3]-1],places[i][2]))
    if type(places[i][4]) is tuple:
        temp = ''
        for j in places[i][4]:
            temp += 'y' + str(j) + ' '
        print('<circle id=\'loc{}\' class=\'loc {} {}t{}\' r=\'5\' cx=\'{}\' cy=\'{}\'><title>{}</title></circle>'
             .format(i,typeOfLocation[places[i][3]-1],temp,places[i][5],coordX(places[i][1]),coordY(places[i][0]),places[i][2]))
        continue
    print('<circle id=\'loc{}\' class=\'loc {} y{} t{}\' r=\'5\' cx=\'{}\' cy=\'{}\'><title>{}</title></circle>'
          .format(i,typeOfLocation[places[i][3]-1],places[i][4],places[i][5],coordX(places[i][1]),coordY(places[i][0]),places[i][2]))
    

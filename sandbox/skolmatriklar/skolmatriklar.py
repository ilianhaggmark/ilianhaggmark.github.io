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

typeOfLocation = ['prep','inprog','done']

places = [#(57.69591411026368, 11.974512606255677, 'Hvitfeldtska (Göteborg)',1,1654,1),
          (58.41098393108915, 15.618027451989096, 'Linköping',2,1599,1),
          (58.71198474879962, 13.822493009050765, 'Mariestad',2,1680,1),
          (58.05516557683714, 14.348125540635456,'Braheskolan (kumlaby, Visingsö)',2,1636,1),
          (58.48046118917959, 16.322710679720974, 'Söderköping',2,1646,1),
          (59.32426557284417, 18.06415353401084, 'Stockholms Gymnasium, Stockholms Trivialskola, Vasa Real (Jakob), Östra Real (Ladugårdslands skola)',2,1650,1),
          (56.87747003456916, 14.811462825188222, 'Växjö',2,1651,1),
          (56.664189945685344, 16.365811344034977, 'Kalmar',2,1655,1),
          (57.78103620382697, 14.16509556651271, 'Jönköping',1,1666,1),
          (57.66595267419247, 15.854831466266031, 'Vimmerby',1,1721,1),
          (59.37553836121076, 17.034422956025377, 'Strängnäs',1,1721,1),
          (60.60911077696517, 15.632383895346559, 'Falun',1,1721,1)
          ]


for i in range(len(places)):
    if type(places[i][4]) is tuple:
        temp = ''
        for j in places[i][4]:
            temp += 'y' + str(j) + ' '
        print('<circle id=\'loc{}\' class=\'loc {} {}t{}\' r=\'8\' cx=\'{}\' cy=\'{}\'><title>{}</title></circle>'
             .format(i,typeOfLocation[places[i][3]-1],temp,places[i][5],coordX(places[i][1]),coordY(places[i][0]),places[i][2]))
        continue
    print('<circle id=\'loc{}\' class=\'loc {} y{} t{}\' r=\'8\' cx=\'{}\' cy=\'{}\'><title>{}</title></circle>'
          .format(i,typeOfLocation[places[i][3]-1],places[i][4],places[i][5],coordX(places[i][1]),coordY(places[i][0]),places[i][2]))
    

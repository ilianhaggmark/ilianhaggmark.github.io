# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:39:43 2022

@author: ilian häggmark

Code to generate JSON file with data for map
"""
import itertools
from bs4 import BeautifulSoup

regionNumbers = [5,15,8,7,8,8,6,11,1]
regionId = ['kinai','toukaidou','tousandou','hokurikudou','sanindou','sanyoudou','nankaidou','saikaidou','hokkaidou']
regions = ['Kinai','Tōkaidō','Tōsandō','Hokurikudō','Sanindō','Sanyōdō','Nankaidō','Saikaidō','Hokkaidō']
n = sum(regionNumbers)
regId = []
for i in range(len(regionNumbers)):
    regId.append([i]*regionNumbers[i])

regId = list(itertools.chain.from_iterable(regId))

listOfProvinceId = [
        'yamashiro',
        'yamato',
        'kawachi',
        'izumi',
        'settsu',        
        'iga',
        'ise',
        'shima',
        'owari',
        'mikawa',
        'toutoumi',
        'suruga',
        'izu',
        'kai',
        'sagami',
        'musashi',
        'awa2',
        'kazusa',
        'shimousa',
        'hitachi',
        'oumi',
        'mino',
        'hida',
        'shinano',
        'kouzuke',
        'shimotsuke',
        'dewa',
        'mutsu',
        'wakasa',
        'echizen',
        'kaga',
        'noto',
        'etchuu',
        'echigo',
        'sado',
        'tanba',
        'tango',
        'tajima',
        'inaba',
        'houki',
        'izumo',
        'iwami',
        'oki',
        'harima',
        'mimasaka',
        'bizen',
        'bitchuu',
        'bingo',
        'aki',
        'suou',
        'nagato',
        'kii',
        'awaji',
        'awa1',
        'sanuki',
        'iyo',
        'tosa',
        'buzen',
        'bungo',
        'chikuzen',
        'chikugo',
        'hizen',
        'higo',
        'hyuuga',
        'oosumi',
        'satsuma',
        'iki',
        'tsushima',
        'ezo'
        ]

listOfProvinces = [
        'yamashiro',
        'yamato',
        'kawachi',
        'izumi',
        'settsu',        
        'iga',
        'ise',
        'shima',
        'owari',
        'mikawa',
        'tōtōmi',
        'suruga',
        'izu',
        'kai',
        'sagami',
        'musashi',
        'awa',
        'kazusa',
        'shimōsa',
        'hitachi',
        'ōmi',
        'mino',
        'hida',
        'shinano',
        'kōzuke',
        'shimotsuke',
        'dewa',
        'mutsu',
        'wakasa',
        'echizen',
        'kaga',
        'noto',
        'etchū',
        'echigo',
        'sado',
        'tanba',
        'tango',
        'tajima',
        'inaba',
        'hōki',
        'izumo',
        'iwami',
        'oki',
        'harima',
        'mimasaka',
        'bizen',
        'bitchū',
        'bingo',
        'aki',
        'suō',
        'nagato',
        'kii',
        'awaji',
        'awa',
        'sanuki',
        'iyo',
        'tosa',
        'buzen',
        'bungo',
        'chikuzen',
        'chikugo',
        'hizen',
        'higo',
        'hyūga',
        'ōsumi',
        'satsuma',
        'iki',
        'tsushima',
        'ezo'                
        ]

listOfProvincesKanji = [
        '山城',        
        '大和',
        '河内',
        '和泉',
        '摂津',
        '伊賀',
        '伊勢',
        '志摩',
        '尾張',
        '三河',
        '遠江',
        '駿河',
        '伊豆',
        '甲斐',
        '相模',
        '武蔵',
        '安房',
        '上総',
        '下総',
        '常陸',
        '近江',
        '美濃',
        '飛騨',
        '信濃',
        '上野',
        '下野',
        '出羽',
        '陸奥',
        '若狭',
        '越前',
        '加賀',
        '能登',
        '越中',
        '越後',
        '佐渡',
        '丹波',
        '丹後',
        '但馬',
        '因幡',
        '伯耆',
        '出雲',
        '石見',
        '隠岐',
        '播磨',
        '美作',
        '備前',
        '備中',
        '備後',
        '安芸',
        '周防',
        '長門',
        '紀伊',
        '淡路',
        '阿波',
        '讃岐',
        '伊予',
        '土佐',
        '豊前',
        '豊後',
        '筑前',
        '筑後',
        '肥前',
        '肥後',
        '日向',
        '大隅',
        '薩摩',
        '壱岐',
        '対馬',
        '蝦夷'        
        ]

listOfPrefectures = [
        'Kyōto',
        'Nara',
        'Osaka',
        'Osaka',
        'Hyōgo and Osaka',
        'Mie',
        'Mie',
        'Mie',
        'Aichi',
        'Aichi',
        'Shizuoka',
        'Shizuoka',
        'Shizuoka',
        'Yamanashi',
        'Kanagawa',
        'Tōkyō, Saitama, and Kanagawa',
        'Chiba',
        'Chiba',
        'Chiba and Ibaraki',
        'Ibaraki',
        'Shiga',
        'Gifu',
        'Gifu',
        'Nagano',
        'Gunma',
        'Tochigi',
        'Yamagata and Akita',
        'Fukushima, Miyagi, Iwate, Akita, and Aomori',
        'Fukui',
        'Fukui',
        'Ishikawa',
        'Ishikawa',
        'Toyama',
        'Niigata',
        'Niigata',
        'Hyōgo and Kyōto',
        'Kyōto',
        'Hyōgo',
        'Tottori',
        'Tottori',
        'Shimane',
        'Shimane',
        'Shimane',
        'Hyōgo',
        'Okayama',
        'Okayama',
        'Okayama',
        'Hiroshima',
        'Hiroshima',
        'Yamagata',
        'Yamagata',
        'Wakayama',
        'Hyōgo',
        'Tokushima',
        'Kagawa',
        'Ehime',
        'Kōchi',
        'Fukuoka and Ōita',
        'Ōita',
        'Fukuoka',
        'Fukuoka',
        'Saga and Nagasaki',
        'Kumamoto',
        'Miyazaki',
        'Kagoshima',
        'Kagoshima',
        'Nagasaki',
        'Nagasaki',
        'Hokkaidō'
        ]

Data = [
        1,
        1,
        1,
        1,
        1,  #5      
        1,
        1,
        1,
        1,
        1,  #10
        1,
        1,
        1,
        1,
        1,   #15
        1,
        1, #17  awa2
        1,
        1,
        1,
        1,
        1,  # mino
        1,
        1,    #24 Nagano
        1,    #25
        1,
        1,
        1,
        1,
        1,   #30
        1,
        1,  # noto
        1,    # echuu
        1,    # echigo
        1,    # sado
        1,    # tanba
        1,
        1,
        1,
        1,   #40 hoki
        1,
        1,   # iwami
        1,   # oki
        1,
        1,   # mimasaka
        1,
        1,
        1,
        1,
        1,    #50
        1,
        1,
        1,  # awaji
        1,
        1,   #55
        1,
        1,
        1,
        1,
        1,   #60
        1,
        1,
        1,
        1,
        1,
        1,
        0.1,    # iki
        0.1,    # tsushima
        1
        ]     

listOfProvinceX = [
        310,
        316,
        306,
        296,
        291,  #5        
        328,
        339,
        356,
        362,
        380,
        405,
        421,
        446,
        433,
        460,
        465,
        489,
        497,
        494,
        509,
        328,
        360,
        373,
        407,
        446,
        480,
        490,
        540,
        311,
        336,
        348,
        363, #32
        375,
        440,
        408,
        292,
        284,
        267, #38
        250,
        220,
        190,
        170,
        195, #43 oki
        267,
        232,
        234,
        215,
        197,  #48
        170,
        146,
        120, # 51 nagato
        293, # 52 kii
        269,
        246,
        234,
        190,
        210,  #57 tosa
        107,  #58 buzen
        125,
        87,
        91,
        62,  #62
        98,
        118,
        97,  #65
        75,
        63,
        55, # 68 tsushima
        580
        ]

listOfProvinceY = [
        545, #1
        572,
        563,
        568,
        551,        
        560, #6
        567,
        575,
        537,
        543,
        545,
        539,
        550,
        510,
        520,
        497,
        537,
        525,
        500,
        460,
        543,
        513,
        488,
        487,
        467,
        457,
        350,
        300,
        515,
        492,
        473,
        425,
        461,
        425,
        380,
        535,
        511,
        520,
        520,
        519,
        525,
        540,
        470,  # 43 oki
        542,
        535,
        553,
        542,
        550,   #48
        560,
        580,
        575, # 51 nagato
        590,
        575,
        595,
        581,
        600,
        610, # 57 tosa
        609,
        633,
        605,
        624, #61
        621,
        650,
        670,
        713, #65 osumi
        690, 
        585, #67 iki
        560, #68 tsushima
        100
        ]      

  
with open('provinceData.json', 'w', encoding='utf-8') as f:
    f.write('[\n')
    for i in range(n):
        line = '{{"Id":"{}","Name":"{}","Kanji":"{}","RegionId":"{}","Region":"{}","Present":"{}","Data":"{}","PositionX":"{}","PositionY":"{}"}},'\
            .format(listOfProvinceId[i],listOfProvinces[i],listOfProvincesKanji[i], \
            regionId[regId[i]],regions[regId[i]],listOfPrefectures[i],Data[i], \
            listOfProvinceX[i],listOfProvinceY[i])
        if i == n-1:
            f.write(line[:-1])
        else:
            f.write(line)
        f.write('\n')
    f.write(']')
       
with open('svgCode.txt', 'w', encoding='utf-8') as f:
    # PRINT CODE FOR REGIONS BEHAVIOUR (ONE ONE FOR EACH REGION)
    for i in range(9):
        line = '#{}:hover ~ .{} {{fill: #2d54a1; fill-opacity:1;}}'.format(regionId[i],regionId[i]) 
        f.write(line)
        f.write('\n')

"""      
with open('svgCode.txt', 'a', encoding='utf-8') as f:
    # PRINT CODE FOR REGIONS BEHAVIOUR (ONE FOR EACH PROVINCE)
    for i in range(n):
        line = '#{}:hover ~ #{} {{fill: #2d54a1; fill-opacity:1;}}'.format(regionId[regId[i]],listOfProvinceId[i]) 
        f.write(line)
        f.write('\n')        
"""


# PRINT STYLE
with open('svgCode.txt', 'a', encoding='utf-8') as f:
    for i in range(n):
        # PRINT CODE FOR DATA
        line = '#data:hover ~ #{} {{fill: #2d54a1; fill-opacity:{};}}'.format(listOfProvinceId[i],Data[i]) 
        f.write(line)
        f.write('\n') 
        # PRINT CODE FOR KANJI HOVER
        line = '#{}{}:hover ~ #{} {{fill-opacity:1;}}'.format(listOfProvinceId[i],format(i+1,'02'),listOfProvinceId[i]) 
        f.write(line)
        f.write('\n')          
 
        
with open('svgCode.txt', 'a', encoding='utf-8') as f:
    # PRINT CODE FOR KANJI LINKS
    x = -13
    y = 805
    for i in range(n):
        if i ==23:
            x = -13;
            y = 835;
        if i ==46:
            x = -13;
            y = 865;        
        rectangleX = x-3
        rectangleY = y-18
        kanjiLabelX = x+15
        kanjiLabelY = y-5
        blueSquareX = x-1
        blueSquareY = y-14
        # BLUE RECTANGLE THAT SURROUNDS KANJI
        line = '<path id="{}Square" style="display:none;stroke:#2d54a1;fill-opacity:0;" d="m {},{} 30,0 0,18 -30,0 0,-18 z"/>\n'.format(listOfProvinceId[i],blueSquareX,blueSquareY)
        f.write(line)
        # Kanji label
        line = '<text id="{}{}" onclick="toggleKanji(this.id)" x="{}" y="{}" class="non-selectable" style="font-size:14px;">{}</text>\n'.format(listOfProvinceId[i],format(i+1,'02'),x,y,listOfProvincesKanji[i])
        f.write(line)        
        # RECTANGLE HIDING KANJI
        line = '<rect id="kanjiCoverRect{}" onclick="toggleKanji(this.id)" class="ans" style="fill:#fcf5e3;" x="{}" y="{}" width="34px" height="25px"></rect>\n'.format(format(i+1,'02'),rectangleX,rectangleY)  
        f.write(line)
        line = '<text id="kanjiLabel{}" onclick=\"toggleKanji(this.id)\" class="ans non-selectable" style="cursor: pointer;font-size:11px;" x="{}" y="{}" dominant-baseline="middle" text-anchor="middle">{}</text>\n'.format(format(i+1,'02'),kanjiLabelX,kanjiLabelY,i+1)
        f.write(line) 
        x += 33 
    for i in range(n):        
        line = '<text id="provinceLabel{}" onclick="toggleKanji(this.id)" class="ans non-selectable" style="cursor:pointer;font-size:11px;" x="{}" y="{}" dominant-baseline="middle" text-anchor="middle">{}</text>\n'.format(format(i+1,'02'),listOfProvinceX[i],listOfProvinceY[i],i+1)
        f.write(line)      

        
        
                



with open('Provinces_of_JapanJS.svg', 'r', encoding='utf-8') as f:
    res = f.read()
soup = BeautifulSoup(res,"lxml")
tags = soup.find_all('path')

with open('svgCode.txt', 'a', encoding='utf-8') as f:
    
    print('Found {} tags.'.format(len(tags)))
    for tag in tags:
        #name = tag.contents[0]
        id = tag.get('id')
        if id in listOfProvinceId:
            idx = listOfProvinceId.index(id)
            titleStructure = 'Name:     ' + listOfProvinces[idx].title() + '&#xA;' \
            + 'Kanji:       ' + listOfProvincesKanji[idx]        + '&#xA;' \
            + 'Present:   '   + listOfPrefectures[idx]           + '&#xA;' \
            + 'Region:    '    + regions[regId[idx]]
            newTag = '<path class="'+ regionId[regId[idx]] \
            + ' path" id="' + id +'" onmouseover="kanjiSquareOn(this.id)" onmouseout="kanjiSquareOff(this.id)" d="' \
            + tag.get('d') +'"><title>'+ titleStructure + '</title></path>\n'
            #newTag = '<path id="' + id +'" d="' + tag.get('d') +'"></path>\n'
            f.write(newTag)
        else:
            print("Ingored tag: {}".format(id))
print('DONE!')
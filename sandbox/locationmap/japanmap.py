# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:28:33 2022

"""
    
def coordX(long):
    Rx = 581.981/(151.58-121.96)
    return Rx*(long - 121.96)

def coordY(lat):
    Ry = 579.907/(47.56-22.95);
    return 579.907 - Ry*(lat - 22.95) 

typeOfLocation = ['city','temple','other']

places = [(44.02093351177296, 144.25424520518152,  'Abashiri',1,2019,8,24,1,1),
          (36.427524007746335, 136.93685975121014, 'Ainokura (Gokayama)',1,2023,5,14,1,1),
          (34.81811432858566, 134.4739163755671,   'Aioi',1,(2019,2022),(6,6),(18,9),(2,2),2),
          (39.71692126207624, 140.12955837707483,  'Akita',1,2022,9,23,2,1),
          (40.82944585413206, 140.7319721790781,   'Aomori',1,2015,8,26,1,1),
          (34.15571624194928, 134.5068757313874,   'Bandō',1,2019,7,20,2,1),
          (33.2797091271209, 131.50025757748438,   'Beppu',1,2022,10,30,2,1),
          (36.10767568124649, 133.04155836314115,  'Beppu (Nishinoshima, Oki)',1,2023,5,20,1,1),
          (34.78917862480473, 133.61602340667946,  'Bitchū-Takahashi',1,2019,8,14,2,1),
          (35.78954576661985, 140.12551784428172,  'Chiba New Town',1,2017,10,11,1,1),
          (35.22745411890912, 138.61003624470004,  'Fujinomiya',1,2022,8,6,1,1),
          (35.296758845596344, 135.1294975322775,  'Fukuchiyama',1,2023,3,30,2,1),
          (36.061615788019594, 136.22320103519166, 'Fukui',1,2023,5,11,2,1),
          (34.4892992671408, 133.36135180732708,   'Fukuyama',1,2019,8,13,3,1),
          (37.45798272698449, 141.0265167080621,   'Futaba',1,2023,5,27,2,1),
          (35.30050432281079, 138.93434707102824,  'Gotemba',1,2015,7,3,1,1),
          (33.58975675103698, 130.42066476374472,  'Hakata',1,2022,10,29,1,1),
          (41.77383721686122, 140.72649311335675,  'Hakodate',1,2015,8,25,1,1),
          (34.70456398791904, 137.73451043554851,  'Hamamatsu',1,2019,8,11,1,1),
          (35.2522509980625, 139.6172903684927,    'Hayama',1,(2019,2022),(6,5),(12,8),(1,1),1),
          (36.14134673958577, 137.25138979330595,  'Hida-Takayama',1,2017,10,7,1,1),
          (35.27222150443177, 136.26329894962083,  'Hikone',1,2023,1,6,2,1),
          (34.827028055803765, 134.6904694465248,  'Himeji',1,(2015,2019),(9,8),(15,19),(1,1),2),
          (38.9882821092515, 141.11761333783875,   'Hiraizumi',1,2022,9,22,3,1),
          (37.21209800357996, 140.99489026927395,  'Hirano',1,2023,5,26,2,1),
          (34.39569705174114, 132.45360164899094,  'Hiroshima',1,2017,10,3,1,1),
          (34.60164693422849, 135.73903609751528,  'Hōryū-ji area',1,(2017,2023),(10,3),(9,27),(1,2),2),
          (42.92187402501365, 143.4531850019753,   'Ikeda',1,2019,8,22,1,1),
          (34.5840580123502, 137.01979595873536,   'Irago',1,2023,1,4,1,1),
          (24.355483454864547, 123.80609745078645, 'Iriomote',1,2023,6,8,1,1),
          (34.49671974249041, 136.7086514240319,   'Ise',1,(2017,2023),(10,1),(8,4),(1,1),2),
          (24.372832571582393, 124.16225429207229, 'Ishigaki',1,2023,6,4,1,1),
          (34.97475503815412, 139.0914342249083,   'Ito',1,2022,8,6,2,1),
          (34.17270081665361, 132.22512704749167,  'Iwakuni',1,2019,8,13,1,1),
          (35.360899528676704, 132.75670260965882, 'Izumo',1,2019,7,14,1,1),
          (36.515601092444726, 136.90139074629076, 'Johana',1,2023,5,14,4,1),
          (31.601930689552784, 130.5628875982547,  'Kagoshima',1,2017,9,27,1,1),
          (39.59169637178015, 140.57075734220905,  'Kakunodate',1,2022,9,23,1,1),
          (35.31945186955205, 139.55040663638616,  'Kamakura',1,(2015,2019),(6,6),(20,16),(1,1),2),
          (36.57845528286428, 136.6481023920915,   'Kanazawa',1,(2017,2023),(10,5),(10,12),(1,3),2),
          (35.970455194127965, 140.6257771130298,  'Kashima',1,2022,7,30,1,1),
          (35.897914097440406, 140.53206264662407, 'Katori',1,2022,7,30,2,1),
          (35.9071951389253, 139.4827436228762,    'Kawagoe',1,2019,8,9,1,1),
          (35.6238834989296, 134.81366947200274,   'Kinosakionsen',1,2019,7,6,2,1),
          (33.41668563636903, 131.6210702895316,   'Kitsuki',1,2022,10,31,2,1),
          (35.919369024567885, 138.4365995332827,  'Kiyosato',1,2015,8,1,1,1),
          (32.790383576077154, 130.68852011044865, 'Kumamoto',1,2022,11,2,2,1),
          (33.32050116728794, 130.50116103797674,  'Kurume',1,2022,11,4,1,1),
          (34.67968297611269, 135.17819782827164,  'Kōbe',1,2015,9,23,1,1),
          (33.567395986813345, 133.5436381721965,  'Kōchi',1,2019,8,3,2,1),
          (34.60208067589035, 133.7657674440379,   'Kurashiki',1,2012,12,0,1,1),
          (34.244861245256786, 132.55752724134737, 'Kure',1,2019,8,13,2,1),
          (42.990352919199744, 144.38247243129456, 'Kushiro',1,(2017,2019),(9,8),(24,21),(1,1),2),
          (34.986158302290676, 135.75882837971218, 'Kyoto',1,(2012,2015,2017,2019,2022,2023),(12,9,10,6,6,3),(19,3,6,22,4,29),(1,1,1,1,1,2),6),
          (35.52657207804267, 137.56748230612288,  'Magome',1,2023,2,12,1,1),
          (35.464310907273216, 133.06392224253742, 'Matsue',1,2019,7,13,1,1),
          (36.230799473630526, 137.96440484682145, 'Matsumoto',1,2023,2,10,1,1),
          (38.369732212340395, 141.06420790278045, 'Matsushima',1,2022,9,22,1,1),
          (33.840607827601474, 132.75126808584233, 'Matsuyama',1,2019,7,20,4,1),
          (36.3707875144099, 140.47620931794899,   'Mito',1,2023,2,22,1,1),
          (33.86587934237956, 132.71972790623587,  'Mitsu',1,2019,7,21,1,1),
          (30.43275354111884, 130.57116820737548,  'Miyanoura (Yakushima)',1,2017,9,28,1,1),
          (31.915737931959868, 131.4319591493026,  'Miyazaki',1,2022,11,1,2,1),
          (33.94512025260045, 130.96149633232486,  'Mojiko',1,2022,11,5,2,1),
          (39.70142436980467, 141.13652810615108,  'Morioka',1,2022,9,22,4,1),
          (36.64313811270716, 138.18844239817594,  'Nagano',1,2022,12,14,1,1),
          (32.75208501339489, 129.86786289050798,  'Nagasaki',1,2017,10,1,1,1),
          (36.09499077168216, 139.11510116514575,  'Nagatoro',1,2023,4,16,1,1),
          (35.59885370082321, 137.60840110000987,  'Nagiso',1,2023,2,12,3,1),
          (35.17107251158024, 136.88152384872566,  'Nagoya',1,(2015,2017,2023),(7,10,1),(3,6,3),(2,2,1),3),
          (26.21838992931376, 127.71320825889924,  'Naha',1,2022,5,16,1,1), 
          (36.3183665903174, 133.30443555383,      'Nakamura (Dōgo, Oki)',1,2023,5,19,4,1),
          (35.5004919860935, 137.5031659177588,    'Nakatsugawa',1,2023,2,11,2,1),
          (37.042456797638884, 136.96398061600104, 'Nanao',1,2023,5,12,4,1),
          (34.68451253048274, 135.82744424672396,  'Nara',1,(2015,2017,2023),(9,10,3),(4,9,27),(1,2,1),3),
          (37.28157907809508, 140.99413813537336,  'Naraha',1,2023,5,26,1,1),
          (35.96910974873644, 137.81554510940055,  'Narai',1,2023,2,11,1,1),
          (35.778077239901904, 140.31407806440208, 'Narita',1,2019,6,11,1,1),
          (43.33961872821058, 145.57958035752424,  'Nemuro',1,2019,8,26,2,1),
          (37.91205301170238, 139.0616220097333,   'Niigata',1,2022,12,16,1,1),
          (36.74770643365527, 139.62203569879816,  'Nikko',1,2015,9,29,1,1),
          (34.66652826031163, 134.96052816816766,  'Nishi-Akashi',1,2023,5,9,1,1),
          (30.73231883387005, 130.98990469809834,  'Nishinoomote (Tanegashima)',1,2017,9,30,1,1),
          (35.49186788882892, 135.74488913842833,  'Obama',1,2022,8,20,1,1),
          (42.91825455928792, 143.20207942211684,  'Obihiro',1,2019,8,22,2,1),
          (36.257360950795665, 136.9076308954191,  'Oginomura (Shirakawago)',1,2023,5,14,3,1),
          (34.66645877188926, 133.91779063460427,  'Okayama',1,(2012,2019),(12,8),(0,3),(1,1),2),
          (35.13985110254823, 136.09057675348063,  'Ōmihachiman',1,2023,3,31,1,1),
          (34.40507968382317, 133.19317931266875,  'Onomichi',1,2019,8,14,1,1),
          (34.70315158045177, 135.49583797578532,  'Osaka',1,(2015,2022),(9,4),(6,1),(1,1),2),
          (43.197777157213466, 140.99374859851062, 'Otaru',1,2015,8,28,1,1),
          (35.90650017390252, 139.62391964459556,  'Ōmiya',1,2023,3,4,1,1),
          (35.0035751950548, 135.86458747281367,   'Ōtsu',1,(2019,2023),(8,3),(18,29),(1,4),2),
          (44.01795386466223, 145.19284338193043,  'Rausu',1,2019,8,26,1,1),
          (38.08161392352128, 138.4381036654598,   'Ryōtsu (Sado)',1,2022,12,16,2,1),
          (36.203415626159455, 133.33516525047978, 'Saigo (Dōgo, Oki)',1,2023,5,19,2,1),
          (35.54519220061463, 133.2228593445673,   'Sakaiminato',1,2023,5,19,1,1),
          (43.06878008315218, 141.35077483655994,  'Sapporo',1,(2015,2017),(8,9),(24,20),(1,1),2),
          (33.163889947149784, 129.7257041001,     'Sasebo',1,2023,6,19,1,1),
          (35.37046984151559, 136.46160664349682,  'Sekigahara',1,2023,1,5,2,1),
          (38.26015433973186, 140.88214206540127,  'Sendai',1,2022,9,21,3,1),
          (35.75741705200435, 139.87579684441076,  'Shibamata',1,2022,1,9,1,1),
          (33.72515159018747, 135.99400085315028,  'Shingu',1,2022,8,21,2,1),
          (36.40441586568864, 136.8864593748723,   'Suganuma (Gokayama)',1,2023,5,14,2,1),          
          (34.34311178082992, 134.90048109486844,  'Sumoto',1,2023,5,10,5,1),
          (35.69788489946107, 139.41357973671106,  'Tachikawa',1,2023,3,11,1,1),
          (32.709800707633846, 131.309120660262,   'Takachiho',1,2022,11,1,1,1),
          (34.35089862690486, 134.04692342940442,  'Takamatsu',1,2019,6,29,1,1),
          (35.6429417722195, 139.28165250175417,   'Takao (Hachioji)',1,2022,5,22,1,1),
          (36.74126995731189, 137.0154360913252,   'Takaoka',1,(2022,2023),(12,5),(15,13),(1,6),1),
          (35.299330115876714, 134.83592342004974, 'Takeda',1,2019,7,6,1,1),
          (24.327397714312063, 124.08662076735048, 'Taketomi',1,2023,6,9,1,1),
          (35.073031341675396, 135.21766071870013, 'Tanba-Sasayama',1,2023,3,30,3,1),          
          (34.995952965325976, 139.86189432396492, 'Tateyama',1,2022,3,5,2,1),
          (34.48048318323294, 136.84683883689385,  'Toba',1,2023,1,4,1,1),
          (34.074656455774736, 134.55137399404586, 'Tokushima',1,2019,7,20,3,1),
          (35.68201005590568, 139.76713367104958,  'Tokyo',1,(2015,2017,2019,2022),(4,9,8,11),(2,25,18,30),(1,1,1,1),4),
          (36.262173502241396, 138.892244667773,   'Tomioka (Gunma)',1,2019,8,10,1,1),
          (37.34813856019956, 141.0084651255693,   'Tomioka (Fukushima)',1,2023,5,27,1,1),
          (35.49437160969115, 134.22586840900968,  'Tottori',1,2019,7,6,3,1),
          (43.15171692647848, 144.49725490338017,  'Tōro',1,(2017,2019),(9,8),(24,21),(2,2),2),
          (36.082594395022895, 140.11170267515104, 'Tsukuba',1,2019,8,8,1,1),
          (35.57718078423189, 137.59543870733165,  'Tsumago',1,2023,2,12,2,1),
          (35.6448528524072, 136.07576742141936,   'Tsuruga',1,2022,8,20,2,1),
          (38.74012866486995, 139.83544260020773,  'Tsuruoka',1,2022,9,23,3,1),
          (34.47256548680881, 131.77379221445935,  'Tsuwano',1,2023,5,22,1,1),
          (35.054771384392254, 134.0030765025985,  'Tsuyama',1,2023,5,24,1,1),
          (34.7675480855901, 136.12996178703017,   'Ueno (Iga)',1,2023,1,6,1,1),
          (34.893020926136366, 135.8064361698505,  'Uji',1,2015,9,21,1,1),
          (36.55910969924928, 139.8984520184904,   'Utsunomiya',1,2022,3,12,1,1),
          (35.466223094424684, 139.62209707581434, 'Yokohama',1,(2019,2022,2023),(6,4,4),(15,17,18),(1,1,1),3),
          (35.42361383409159, 133.33651519935012,  'Yonago',1,2023,5,21,1,1),
          (37.00693272001852, 140.84985661870854,  'Yumoto',1,2022,9,21,1,1),
          (45.417680912880115, 141.67715401971745, 'Wakkanai',1,2017,9,21,1,1),
          (35.2920024893565, 139.58284724205453,   'Zushi',1,(2019,2022),(6,1),(14,2),(1,1),2),
          (34.96825753647056, 139.75816532710365,  'Awa Sunosaki Jinja',2,2022,3,5,3,1),
          (36.056283404626846, 136.3568679214462,  'Daihonzen Eiheiji',2,2023,5,12,2,1),
          (33.521407505208664, 130.53482674337562, 'Dazaifu Tenmangū',2,2017,9,26,1,1),
          (38.70240259470235, 139.9813513653995,   'Dewa Jinja (Haguro)',2,2022,9,24,1,1),
          (34.892388677976065, 134.65463751285574, 'Engyōji (Shosha)',2,2015,9,15,2,1),
          (35.07167255783961, 135.84119847123674,  'Enryakuji (Hiei)',2,2015,9,20,1,1),
          (34.535806296148046, 135.90683656360343, 'Hase-dera',2,2023,3,29,1,1),
          (34.670401662013575, 135.65059505487318, 'Hiraoka Jinja',2,2022,4,2,1,1),
          (34.752773573759455, 135.34008217195586, 'Hirota Jinja',2,2022,6,9,1,1),
          (34.459888582483124, 134.85249911592922, 'Izanagi Jingū',2,2023,5,10,2,1),
          (35.05909633351751, 135.5783468387876,   'Izumo daijingū',2,2023,3,29,3,1),
          (33.840497302163776, 135.77357100401431, 'Kumano Hongu Taisha',2,2022,8,22,1,1),
          (33.67358689495716, 135.88959291629493,  'Kumano Nachi Taisha',2,2022,8,21,1,1),
          (34.50936482800459, 136.78832541769148,  'Meoto Iwa',2,2017,10,8,2,1),
          (35.925309818339215, 138.93019386812176, 'Mitsumine Jinja',2,2022,11,27,1,1),
          (35.43029186384583, 135.1543669383341,   'Motoise Naiku Kotai Jinja',2,2023,3,30,1,1),
          (35.782902921419655, 139.1496698816905,  'Musashi Mitake Jinja',2,2022,12,3,1,1),    
          (36.95422361795668, 136.7760535435055,   'Myōjōji',2,2023,5,13,5,1),
          (37.97134092425907, 138.37281803699517,  'Myosenji',2,2022,12,17,2,1),
          (35.360409242749505, 136.5257473420206,  'Nangū Taisha',2,2023,1,5,1,1),
          (34.22323222400986, 135.60558761222578,  'Oku no In (Kōyasan)',2,2015,9,7,1,1),
          (34.53684723238966, 135.4607642628895,   'Ōtori Taisha',2,2022,6,8,1,1),
          (36.596701725811386, 139.8207908651671,  'Ōya Kannon',2,2022,3,12,2,1),
          (38.31316666395517, 140.43460791093491,  'Risshaku-ji (Yamadera)',2,2022,9,25,1,1),
          (37.997770947612864, 138.43744513069888, 'Seisuiji',2,2022,12,17,1,1),
          (34.35768114722996, 134.8388348135157,   'Senzan Senkōji',2,2023,5,11,1,1),
          (38.318802943992324, 141.0126250293565,  'Shiogama Jinja',2,2022,9,22,2,1),
          (37.036522176272165, 140.83731006399893, 'Shiramizu Amidadō',2,2022,9,21,2,1),
          (37.28643118981487, 136.77004547177438,  'Sōjiji Soin',2,2023,5,13,3,1),
          (35.376217184359724, 140.360592643279,   'Tamasaki Jinja (Kazusa-Ichinomiya)',2,2022,3,5,1,1),
          (36.76104018593, 138.06901788190365,     'Togakushi Jinja',2,2022,12,14,2,1),
          (31.650463271856015, 131.46669111934406, 'Udo Jingū',2,2022,11,2,1,1),
          (33.52322727049636, 131.3772129623065,   'Usa Jingū',2,2022,10,30,1,1),
          (35.98269604987475, 140.22026771433178,  'Ushiku daibutsu',2,2022,9,10,1,1),
          (33.07386486858091, 130.10778726726173,  'Yūtoku Inari Jinja',2,2022,11,4,2,1),
          (43.4339033294261, 144.09122144417233,   'Akanko',3,2019,8,23,1,1),
          (35.57127747454685, 135.19169151095457,  'Amanohashidate',3,2022,8,19,1,1),
          (34.55354149339041, 134.97803633771952,  'Awaji Hanasajiki',3,2023,5,10,1,1),
          (26.709929647233505, 127.88004251904874, 'Bise-fukugi',3,2022,5,18,1,1),
          (35.703606524712804, 139.52785673486497, 'Buta-ya',3,2023,4,27,1,1),
          (34.288709915146285, 134.85027613091464, 'Daijōike',3,2023,5,10,4,1),
          (35.37079492858473, 133.53907608070546,  'Daisen (Misen)',3,2023,5,23,1,1),
          (36.240607392272196, 133.23591013950818, 'Dangyō no taki',3,2023,5,19,3,1),
          (33.96511487244846, 130.95658575529401,  'Dannoura',3,2022,11,5,1,1),
          (36.831376600289225, 138.96703735777967, 'Doai station',3,2022,8,14,1,1),
          (33.58313398740028, 131.60159034422705,  'Futago-san (Kunisaki)',3,2022,10,31,1,1),
          (37.09392242945956, 136.72680669325015,  'Ganmon (Noto Kongo Kaigan)',3,2023,5,13,4,1),
          (35.69611331727024, 139.57040473773674,  'Ghibli museum',3,(2015,2023),(7,3),(26,18),(1,1),2),
          (35.707901120914364, 140.86852289128632, 'Inubōsaki Lighthouse (Chōshi)',3,2022,7,30,3,1),
          (35.388383355205114, 136.93909110394148, 'Inuyama Castle',3,2023,1,5,3,1),
          (34.272160197223975, 132.30689878863268, 'Itsukushima',3,2017,10,4,1,1),
          (35.43924265467683, 132.62891303136445,  'Izumo Hinomisaki Lighthouse',3,2019,7,14,2,1),
          (26.33226448647408, 127.928951047836,    'Kaichū Dōro (Uruma)',3,2022,5,17,1,1),
          (34.72549779216165, 133.7623764024739,   'Ki no jō',3,2012,12,31,1,1),
          (43.56464258710847, 144.34202960594345,  'Kussharoko',3,2019,8,23,2,1),
          (33.40269898822234, 130.51178262475239,  'Kyushu Synchrotron Light Research Center',3,2023,6,20,2,1),
          (36.15236682451959, 136.27206020867808,  'Maruoka jō',3,2023,5,12,1,1),
          (35.340672125733775, 136.98885010310028, 'Mejimura',3,2015,7,5,1,1),
          (35.16104663407069, 139.61358690844077,  'Misaki Marine Biological Station',3,2022,4,21,1,1),
          (37.397285191263656, 137.2445711311053,  'Mitsukejima (Suzu)',3,2023,5,13,1,1),
          (35.22722482289225, 140.00294279148622,  'Koito river (Kimitsu)',3,2022,4,23,1,1),
          (34.23620799870292, 134.64194859568966,  'Naruto bridge',3,2019,7,20,1,1),
          (35.852441133694654, 139.04072966895382, 'Nippara Cave (Okutama)',3,2023,3,9,1,1),
          (35.15759663959294, 139.83435888078037,  'Nokogiriyama',3,2023,3,7,1,1),
          (36.056498707875846, 132.98335091088697, 'Onimai tenbōdai',3,2023,5,20,2,1),
          (35.440793978527466, 139.2312641618142,  'Oyama',3,2023,5,5,1,1),
          (45.24342188585031, 141.22707187357042,  'Rishiri',3,2017,9,22,1,1),
          (38.041680650610886, 138.25600579101183, 'Sado kinzan',3,2022,12,17,3,1),
          (31.58991112033029, 130.65152444444348,  'Sakurajima',3,2017,9,27,2,1),
          (35.77840588332431, 139.41555527322524,  'Sayama-ko',3,2023,4,28,1,1),
          (44.123241568037805, 145.077717661309,   'Shiretoko',3,2019,8,25,1,1),
          (37.42439534970487, 136.99819560274577,  'Shiroyone Senmaida',3,2023,5,13,2,1),
          (45.52294411245407, 141.9365903282125,   'Sōya Misaki',3,2017,9,21,2,1),
          (34.94495737470505, 134.42645293630025,  'SPring-8',3,(2019,2022),(6,6),(18,9),(3,3),2),
          (30.375651900349432, 130.95813770081173, 'Tanegashima Space Center',3,2017,9,30,2,1),
          (34.254539948163234, 134.6845393666482,  'Uzu no oka',3,2023,5,10,3,1),
          (33.217568237609015, 129.55280901088472, 'Westmost point of mainland Japan',3,2023,6,20,1,1),
          (34.5577384442793, 135.85076647620178,   'Yamanobe-no-michi',3,2023,3,28,2,1),
          (33.323955028823406, 130.38876181053158, 'Yoshinogari Kōen',3,2022,11,4,3,1),
          (34.33830971681228, 135.880496974643,    'Yoshinoyama',3,2023,3,28,1,1)]
    
airports = [
        (42.787637170039254, 141.67754383582476,'CTS'),
        (33.58597245814974, 130.45092328157668, 'FUK'),
        (35.55009541852774, 139.78625914430324, 'HND'),
        (24.39609230568927, 124.2457550857955,  'ISG'),
        (34.43209117824599, 135.23050614807116, 'KIX'),
        (43.04179300357022, 144.19284406130268, 'KUH'),
        (34.85882324174892, 136.81213720325243, 'NGO'),
        (32.91422175774846, 129.9222486752531,  'NGS'),
        (35.76617124029606, 140.38631898928807, 'NRT'),
        (26.197481983335283, 127.64592613075293,'OKA')]

# Coordinate values are rounded to four decimal places to remove redundant precision.
for i in range(len(places)):      
    if type(places[i][4]) is tuple:
        yClass = ''
        mClass = ''
        dClass = ''
        oClass = ''
        for j in range(0,len(places[i][4])):
            yClass += 'y' + str(places[i][4][j]) + ' '
            mClass += 'm' + str(places[i][5][j]) + ' '
            dClass += 'd' + str(places[i][4][j]) + "{:02d}".format(places[i][5][j]) + ' '
            oClass += 'o' + str(places[i][4][j]) + "{:02d}".format(places[i][5][j]) + "{:02d}".format(places[i][6][j]) + str(places[i][7][j]) + ' '
        print('<circle id=\'loc{}\' class=\'loc {} {}{}{}{}t{}\' o=\'{}\' r=\'1\' cx=\'{}\' cy=\'{}\'><title>{}</title></circle>'
             .format(i,typeOfLocation[places[i][3]-1],yClass,mClass,dClass,oClass,places[i][8],oClass[1:10],round(coordX(places[i][1]),4),round(coordY(places[i][0]),4),places[i][2]))
        continue
    oClass = str(places[i][4]) + "{:02d}".format(places[i][5]) + "{:02d}".format(places[i][6]) + str(places[i][7])
    print('<circle id=\'loc{}\' class=\'loc {} y{} m{} d{}{:02d} o{} t{}\' o=\'{}\' r=\'1\' cx=\'{}\' cy=\'{}\'><title>{}</title></circle>'
          .format(i,typeOfLocation[places[i][3]-1],places[i][4],places[i][5],places[i][4],places[i][5],oClass,places[i][8],oClass,round(coordX(places[i][1]),4),round(coordY(places[i][0]),4),places[i][2]))
  
for i in range(len(airports)):
    print('<use id=\'air{}\' class=\'air\' href=\'#air-tri\' transform=\'translate(-1 -0.8)\' width=\'2\' height=\'2\' x=\'{}\' y=\'{}\'><title>{}</title></use>'
          .format(i,round(coordX(airports[i][1]),4),round(coordY(airports[i][0]),4),airports[i][2]))
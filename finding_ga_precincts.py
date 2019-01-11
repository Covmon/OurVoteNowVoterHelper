import os
from collections import OrderedDict

ga_counties = ["Appling","Atkinson","Bacon","Baker","Baldwin","Banks","Bartow","Ben Hill","Berrien","Bibb","Bleckley","Brantley","Brooks","Bryan","Bulloch","Burke","Calhoun","Camden","Candler","Carroll","Catoosa","Charlton","Chatham","Chattahoochee","Chattooga","Cherokee","Clarke","Clay","Clayton","Clinch",
    "Cobb","Coffee","Colquitt","Columbia","Cook","Coweta","Crawford","Crisp","Dade","Dawson","DeKalb","Decatur","Dodge","Dooly","Dougherty","Douglas","Early","Echols","Effingham","Elbert","Emanuel","Evans","Fannin","Fayette","Floyd","Forsyth","Franklin","Fulton","Gilmer","Glascock","Glynn","Gordon","Grady","Greene",
    "Gwinnett","Habersham","Hall","Hancock","Haralson","Harris","Hart","Heard","Henry","Houston","Irwin","Jackson","Jasper","Jeff Davis","Jefferson","Jenkins","Johnson","Jones","Lamar","Lanier","Laurens","Lee","Liberty","Lincoln","Long","Lowndes","Lumpkin","Macon","Madison","Marion","McDuffie","McIntosh","Meriwether",
    "Miller","Mitchell","Monroe","Montgomery","Morgan","Murray","Muscogee","Newton","Oconee","Oglethorpe","Paulding","Peach","Pickens","Pierce","Pike","Polk","Pulaski","Putnam","Quitman","Rabun","Randolph","Richmond","Rockdale","Schley","Screven","Seminole","Spalding","Stephens","Stewart","Sumter","Talbot","Taliaferro",
    "Tattnall","Taylor","Telfair","Terrell","Thomas","Tift","Toombs","Towns","Treutlen","Troup","Turner","Twiggs","Union","Upson","Walker","Walton","Ware","Warren","Washington","Wayne","Webster","Wheeler","White","Whitfield","Wilcox","Wilkes","Wilkinson","Worth"]

precinct_files = os.listdir('/Users/sammahle/Desktop/OurVoteNowVoterHelper/Georgia_Election_Data_CSVs/2016/General/Precinct/')

precinct_dict = OrderedDict()

for county in ga_counties:
	county_list = []
	for file_name in precinct_files:
		if county.upper() + '_' in file_name and county.upper() + '_total_voted.csv' != file_name and county.upper() + '_percent_voted.csv' != file_name and county.upper() + '_total_registered.csv' != file_name and county.upper() + '_TOTAL_percent_voted.csv' != file_name:
			county_list.append(file_name.replace('{}_'.format(county.upper()),'').split('_')[0])
	precinct_dict[county] = county_list


print dict(precinct_dict)


dictt = {'Union': ['8', '9', '5', '10', '4', '11', '7', '2', '6', '3'], 'Paulding': ['09B', '04C', '14C', '07B', '11C', '02B', '12B', '13B', '10B', '03C', '88888', '06B', '08B', '05B'], 'Montgomery': ['04', '05', '06', '03', '07', '02'], 'Wayne': ['5C', '3A', '5B', '3B', '5A', '3C', '2C', '1B', '2B', '1C', '4A', '2A', '2D', '4B'], 'Screven': ['05', '04', '88888', '07', '02', '06', '03', '12', '08', '11', '09', '10'], 'Pickens': ['11', '5', '10', '4', '2', '7', '3', '12', '6', '8', '9'], 'Wilkinson': ['10', '08', '11', '04', '05', '99999', '06', '03', '07'], 'Ben Hill': ['2', '88888'], 'Worth': ['5', '4', '7', '2', '6', '3', '12', '16', 'BUTTS', '8', '15', '88888', '10', '9', '14', '11'], 'Appling': ['1C', '4A', '4D', '88888', '4C', '4B', '5B', '3A', '5C', '3A1', '3C', '5A', '2', '3B'], 'McDuffie': ['133B', '139', '133A', '134', '135', '136', '137', '99999', '88888', '132'], 'Dodge': ['IN', 'CLARK', 'LEE', 'MITCH', 'PONDT', 'JONES', 'MULLI', 'RAWLI', 'MPIR', 'JAYBI', 'YONKE', 'MILAN', 'PLAIN', 'MCCRA', 'VILUL'], 'Columbia': ['134', '034', '100', '063', '131', '105', '031', '135', '062', '130', '030', '064', '136', '080', '050', '061', '085', '107', '033', '065', '137', '051', '060', '132', '99999', '88888', '032', '075', '070', '016', '090', '040', '026', '074', '017', '025', '111', '125', '020', '108', '120', '110', '076', '115', '021', '109', '015'], 'Bibb': ['HO5', 'WA2', 'HA1', 'VV2', 'HA4', 'RU2', 'HO4', 'VV3', 'HO1', 'HA5', 'VV6', 'HO7', 'HA3', 'HO2', 'VV5', 'HO6', 'WA1', 'VV1', 'HA2', 'HO3', 'VV4', '99999', 'RU1', '88888', 'EM4', 'EM1', 'GF2', 'EM5', 'GF3', 'GF5', 'EM3', 'GF4', 'EM2', 'GF1'], 'Brooks': ['88888', '660', '1712', '1650', '1402', '1230', '659'], 'Cherokee': ['006', '032', '003', '037', '007', '033', '002', '036', '004', '018', '030', '029', '035', '88888', '005', '99999', '019', '031', '028', '034', '009', '021', '015', '042', '024', '038', '010', '008', '020', '014', '043', '039', '011', '023', '040', '026', '012', '044', '022', '016', '041', '027', '013'], 'Harris': ['MG', 'GM', 'PV', 'VP', 'percent', 'K', 'CA', 'WA', 'WH', 'L9', 'U9', 'EL'], 'Chattooga': ['940', '968', '927', '1216', '870', '925', '-968', '962', 'P-870', '1382', '961', '1484'], 'Coweta': ['10', '24', '15', '21', '09', '11', '25', '14', '20', '08', '12', '26', '17', '23', '13', '27', '16', '22', '03', '06', '02', '07', '99999', '18', '04', '28', '19', '05'], 'Dougherty': ['18', '04', '99999', '88888', '19', '05', '28', '06', '03', '07', '02', '17', '23', '12', '26', '16', '22', '13', '27', '15', '21', '09', '10', '24', '14', '20', '08', '11', '25'], 'Wilcox': ['4A', '2B', '99999', '88888', '2A', '3A', '5A'], 'Meriwether': ['99999', '04', '05', '03', '06', '02', '07', '12', '13', '10', '09', '11', '14', '08'], 'Cook': ['L', 'RB', 'M', 'S', 'EP', 'DB', 'NL'], 'Gordon': ['1055', '1064', '856', '1063', '980', '1056', '1235', '849-B', '874', '849-A', '973', '99999'], 'Henry': ['41', '27', '58', '44', '40', '26', '59', '45', '39', '43', '25', '46', '38', '42', '47', '52', '34', '28', '57', '31', '53', '35', '29', '56', '30', '62', '50', '36', '55', '33', '61', '49', '51', '37', '54', '99999', '32', '88888', '60', '48'], 'Webster': [], 'Wilkes': ['2B', '4A', '2A', '4B', '3A', '99999', '3B'], 'Thomas': ['118', '104', '119', '105', '103', '106', '102', '107', '112', '117', '113', '116', '99999', '110', '115', '109', '111', '114', '108', '120'], 'Chatham': ['5-06C', '8-09C', '4-11C', '3-10C', '2-07C', '7-08C', '7-05C', '1-13C', '6-02C', '6-01C', '7-06C', '6-11C', '1-10C', '4-02C', '3-03C', '5-08C', '8-07C', '4-12C', '5-05C', '2-04C', '3-13C', '2-09C', '3-05C', '3-08C', '2-12C', '4-04C', '8-11C', '2-02C', '3-15C', '8-01C', '4-14C', '5-03C', '1-06C', '7-10C', '1-16C', '7-03C', '1-05C', '1-08C', '6-09C', '7-13C', '8-02C', '2-11C', '4-07C', '8-12C', '5-10C', '1-09C', '7-12C', '6-08C', '6-05C', '1-14C', '8-13C', '4-06C', '5-11C', '5-01C', '8-03C', '2-03C', '3-14C', '4-15C', '5-02C', '3-04C', '99999', '88888', '3-09C', '4-08C', '8-10C', '4-05C', '1-17C', '7-01C', '6-06C', '7-11C', '7-07C', '6-10C', '4-13C', '8-06C', '2-05C', '3-12C', '3-02C', '8-15C', '3-01C', '8-08C', '5-07C', '4-10C', '8-05C', '3-11C', '2-06C', '7-14C', '6-03C', '7-09C', '7-04C', '1-12C'], 'Stephens': [], 'Newton': ['88888', '16', '13', '17', '23', '12', '14', '08', '20', '25', '15', '09', '10', '24', '19', '05', '18', '04', '07', '02', '06', '03'], 'Bacon': ['WARNO', 'EW L', 'TAYLO', 'DOUGL', 'WARE'], 'Hall': ['005', '031', '019', '028', '004', '030', '018', '029', '007', '002', '99999', '88888', '006', '003', '022', '016', '027', '013', '023', '017', '026', '012', '020', '008', '014', '025', '011', '021', '009', '015', '024', '010'], 'Heard': ['NO', 'COO', 'FRA', 'PH', 'SOU'], 'Camden': ['06', '03', '07', '02', '04', '05', '09', '10', '08', '14', '11', '12', '13'], 'Jasper': ['296', '295', '88888'], 'Effingham': ['5A', '3B', '3C', '99999', '5C', '3D', '5B', '3A', '4B', '2A', '4C', '1D', '1B', '2C', '1C', '4A', '2B'], 'Lowndes': ['003', '006', '002', '007', '004', '005', '99999', '009', '008'], 'Polk': ['05', '04', '02', '07', '03', '99999', '88888', '06'], 'Warren': [], 'Jackson': ['1704', '0465', '0455', '0255', '0248', '1765', '0257', '0255', '0253', '1407', '0428', '0245', '1691', '1747', '0245', '88888', '99999'], 'McIntosh': ['271', '1771', '99999', '88888', '22', '1515', '1480'], 'Washington': ['88', '94', '91', '1488', '97', '1350', '99'], 'Liberty': ['9', '13', '3', '6', '12', '2', '7', '88888', '99999', '11', '4', '14', '10', '5'], 'Lee': ['7', '2', '6', 'DODGE', '3', '5', '4', '10', '8', '9', '99999'], 'Jefferson': ['1593', '0077', '99999', '88888', '0083', '0082', '1460', '0081', '0085'], 'Seminole': ['2', '3', '5', '4', '99999'], 'Jenkins': ['88888', '3', '2', '4', '5'], 'White': ['061', '051', '081', '88888', '031', '101', '111', '021', '041', '091', '071'], 'Burke': ['0010', '0009', '0015', '0011', '0008', '0014', '0012', '0013', '0016', '0003', '0006', '0002', '0007', '0004', '0005'], 'Putnam': ['106', '107', '104', '105', '88888'], 'Coffee': ['5', '4', '2', '88888', '3', '6'], 'Glynn': ['3743', '5933', '2713', '2943', '2923', '3713', '1933', '4933', '99999', '88888', '3723', '4913', '5943', '3733', '2933', '4923', '1923', '1943', '5913', '2953', '5923'], 'Dooly': ['2', '7', '5', '8'], 'Catoosa': ['BOYN', 'WOOD', 'FT O', 'BLCK', 'POPS', 'KT', 'GRAY', 'RING', 'WEST', 'LAKE', 'HAM'], 'Oconee': ['12', '13', '10', '09', '11', '08', '04', '05', '03', '06', '02', '07'], 'Jeff Davis': ['501', '401', '201', '301', '202', '302', '502', '402'], 'Toombs': ['39', '43', '513', '88888', '514'], 'Marion': ['807', '955', '948', '99999', '88888', '808'], 'Ware': ['200A', '408', '200B', '409', '400', '304', '405', '300', '404', '88888', '407', 'BACON', '406'], 'Colquitt': ['0007', '0002', '0019', '0018', '0014', '0020', '0008', '0011', '0015', '0021', '0009', '0010', '0016', '0022', '0013', '0017', '0023', '0012'], 'Taliaferro': ['601', '88888'], 'Upson': ['0589', '1610', '5610'], 'Schley': [], 'Johnson': ['1301', '1266', '55'], 'Candler': ['99999', '88888', '1736'], 'Baker': ['N', 'M', 'H', 'percent', 'percent'], 'Oglethorpe': ['X', 'CR'], 'Irwin': ['1661', '1529', '1753', '1643', '1421', '1670', '1388'], 'Greene': ['003', '006', '002', '007', '004', '88888', '99999', '005', '008'], 'Bartow': ['05', '04', '18', '99999', '07', '02', '06', '03', '16', '17', '12', '08', '14', '11', '09', '15', '10'], 'Forsyth': ['27', '16', '10', '15', '21', '25', '08', '29', '04', '19', '05', '03', '06', '02', '07'], 'Clay': ['88888', '99999', '2', '3', '5', '4'], 'Fulton': ['SC04', '11K', 'ML03', 'ML07A', '04I', '09I', '06L1', 'JC12', 'SS04', 'RW22A', 'A01B', '04W', 'SS08C', '08E', 'SC08E', 'SC30B', '07M', '03C', 'RW02', '10G', 'CH04A', 'ML01B', '02J', '06D', '11N', '01P', 'SS01', 'CH05', 'CP06A', '04L', '05A1', '12J', 'CP02', 'AP10', '10B', '03F', '11P', '07H', 'SS15B', '11J', 'SS18B', '01T', 'CH01', 'SS05', '09H', '04V', '12N', 'SC08D', 'SS08B', '08D', '02L1', 'SC05D', '05D', '01J', 'AP022', '04X1', '03B', '10F', 'AP14', 'RW03', 'CP08A', 'SS31', 'RW11A', 'RW07B', 'SC18A', '03P2', 'MP01', '06E', 'JC03B', '02K', 'SS13A', 'JC16', '09M', '04M', 'SC05A', '04S', '12K', 'JC13B', '08A', 'HP01', 'SC23B', 'RW06', '10C', 'SC212', 'ML04A', '03G', 'CP012', 'SS15A', 'SS18A', '12S', '04K', 'CH02', 'SS06', 'JC10', '09K', 'SC08G', 'SS08A', '08G', '12M', '01I', '02L2', '03A', 'CP05B', 'AP021', '04X2', '02S', '10E', '06F', 'JC03A', 'RW07A', 'SC18B', 'RW19', 'JC15', 'SS03', '01R', 'SS13B', '05B', 'SC05B', 'SS08D', '08B', 'JC09', 'SC08B', 'SC23A', '12H', 'JC13A', 'RW05', 'SC211', '11R', '07J', '03D', 'CP011', 'ML04B', '11H', '06B', '04J', '06L2', 'JC11', 'CH03', 'SC08F', 'CP04', '04T', 'A01A', '12L', '01H', '05F', 'SC30A', '07N', 'RW01', '10D', '06G', '11M', 'SC02', 'JC14', '01S', '05C', '05A2', 'SC08C', 'JC08', '08C', '12I', '02W', '10A', 'AP13', 'RW04', '03E', 'ML04C', 'SC17B', '09F', '04F', 'C032', 'C01B', '11E3', '06N', 'AP06', 'SS11B', 'EP01', '03L', '07B', 'ML06B', '05J', 'AP04B', '01D', 'ML024', 'JC01', '08J', 'SS17', 'AP09B', '04C', 'AP12A', '09C', 'JC18', 'AP03', 'SC11A', 'SS26', 'ML05C', '02E', 'SS07A', '03I', '10M', 'RW08', 'EP04', 'RW20', '03P1A', 'SS12', 'ML021', 'SC17C', 'SS09A', '09G', 'AP01A', '04G', '11E2', '02A', 'ML011', 'SS11C', 'RW10', '03S', 'SS22', '06Q', '10I', 'SC16', 'SS19A', '07C', '03M', '10H2', '01E', 'JC04B', '05K', '12A', 'SS16', '08K', '08P', '04B', 'ML072', 'AP01D', 'SC27', 'JC19', '09B', 'SC09B', '02F1', '08N1', 'ML05B', 'SS02B', '02D', 'SS29A', 'AP07B', '06J', '10R', 'SC19B', '03H', '07F', 'RW09', 'SC13', 'CP083', '12D', 'RW21', 'JC05', 'C02B', 'SS09B', '09D', 'AP01B', '04D', 'SC29A', '11E1', '02B', 'ML012', 'RW13', 'EP03', '10J', '06R', 'SC15', '03N', 'SS19B', '01F', 'JC04A', '10H1', '08H', '04A', 'ML071', '09A', 'SC09A', 'AP12C', '02F2', '08N2', 'RW16', '11C', 'SS02A', '02G', 'AP07A', '06I', 'ML05A', 'C01E', '07E', 'SS07C', 'SC19A', '12E1', '88888', '99999', 'SC10', '08M', 'JC06', '12G', '01C', 'ML023', 'C02A', '09E', 'SC17A', 'AP01C', 'C031', '02C', 'C01A', 'SS20', 'RW12', '11G', 'SS11A', 'AP05', 'EP02', 'SC14', '10K', 'SC07A', '07A', 'CP01B', 'AP04A', 'ML06A', 'JC02', 'SS14', 'AP09A', 'AP12B', 'SS25', '11B', 'SS11D', 'RW17', 'SC11B', '03T', '10P', 'CP051', '07D', 'SS07B', 'AP02B', '08F1', 'CP081', 'JC07', '08L', 'PA01', '12F', 'SC01B', 'ML022', '01B', 'CP07A'], 'Macon': ['5', '4', '2', '3', '99999', '88888'], 'Madison': ['percent', 'HUL', 'PAO', 'HAR', 'COL', 'L', 'PIT', 'FOR', 'COM', 'POC', 'LA'], 'Taylor': ['6', '88888', '5'], 'Evans': ['99999'], 'Clinch': ['99999', 'F', 'AB', 'AG', 'D', 'percent'], 'Charlton': ['4H', '3B', '5F', '3S', '4A', '5W', '5R'], 'Echols': ['88888'], 'Grady': ['P', 'W', 'L', 'percent', 'SH', 'H', 'M', 'S', 'percent', 'WL', 'C05', 'C04'], 'Dawson': ['02', '03'], 'Hart': ['8', '5', '4', '7', '3', '6'], 'Baldwin': ['88888', '99999', '322', '321W', 'CTY6', '321E', 'CTY3', 'CTY2', 'MONT', 'CTY4', '318', 'CTY1', 'CTY5', 'MERI', '319'], 'Lumpkin': ['DA'], 'Lanier': ['88888', '4', '2', '3'], 'Haralson': ['13', '12', '08', '11', '09', '10', '05', '04', '07', '06', '03'], 'Rockdale': ['SH', 'SM', 'percent', 'T', 'BT', 'ST', 'MA', 'HC', 'SP', 'MI', 'percent', 'percent', 'percent', 'FS', 'HI', 'FI', 'SA'], 'Elbert': ['191', '190', '193', '196', '315', '192', '197', '201', '202', '199'], 'Decatur': ['513', '1805', '694', '1361', '99999', '88888', '514', '1342', '1325', '1613'], 'Clarke': ['5D', '3B', '5A', '8A', '6A', '6D', '6B', '5C', '8C', '6C', '3A', '5B', '8B', '88888', '99999', '2A', '7C', '4B', '7B', '1D', '7A', '1B', '2B', '4A', '1C'], 'Richmond': ['810', '809', '112', '808', '801B', '210', '109', '310', '115', '608', '309', '708', '209', '108', '509', '114', '308', '709', '208', '111', '405', '301', '803', '104', '201', '304', '605', '806', '804H', '204', '705', '404', '601', '802', '105', '504', '701', '305', '401', '604', '807', '501', '303', '801', '106', '203', '507', '702', '306', '402', '103', '804', '607', '502', '99999', '88888', '707', '406', '302', '603', '107', '202', '506', '703', '307', '102', '805', '503', '207', '706'], 'Cobb': ['A01', 'VG03', 'SM01', 'FP01', 'MK01', 'F02', 'LM02', 'MA03', 'FO02', 'G02', 'KE5A', 'H03', 'FR01', 'SO01', 'T02', 'MR7A', 'RW01', 'K01', 'R01', 'L02', 'HY01', 'LA01', 'SN2A', 'LW01', 'MR4A', 'VG02', 'SN1A', 'F03', 'SI01', 'MT03', 'LM03', 'GM01', 'MA02', 'R02', 'SW02', 'H02', 'RS01', 'MR2B', 'ML01', 'MS02', 'HL01', 'SF01', 'VG01', 'MR4B', 'SM03', 'LI01', 'MA01', 'K01', 'R01', 'SW01', 'VG04', 'SN7A', 'WL01', 'SO03', 'RM01', 'FY01', 'MR2A', 'MB01', 'MA04', 'FO05', 'MS01', 'HR01', 'MC01', 'HT01', '01', 'MR4C', 'ME01', 'FO01', 'W01', 'LM01', 'MT01', 'SN4A', 'MD01', 'MR1A', 'G01', 'SA01', 'SO02', 'PS3A', 'WG02', 'T01', 'RW02', 'FO04', 'MT04', 'VA01', 'LM04', 'KE3A', 'L01', 'GT01', 'SN5A', 'AC1A', 'PP01', 'AD01', 'EL01', 'DU01', 'MR6B', 'PR01', 'EA02', 'KE2A', 'DV01', 'EL04', 'PM02', 'PS2A', 'R02', 'TM01', 'NS01', 'NC01', 'PE01', 'PS1A', 'KE1A', 'K01', 'MR5B', 'PT01', 'DC01', 'KP01', 'SN6A', 'AU1A', 'PF01', 'EL05', 'MR3A', 'NP01', 'R03', 'DO01', 'AC1C', 'KL01', 'MR5A', 'R05', 'TR01', 'EL03', 'KP02', 'DL01', 'AC1B', 'KE4A', 'PO01', 'R04', 'EL02', 'MR6A', 'EA01', 'NJ01', 'KP03', 'SN3A', 'PM01', 'R01', 'EP01', 'DI01'], 'Morgan': ['99999', '04', '05', '06', '03', '07', '02'], 'Glascock': ['MILL', 'IBS', 'MITC', 'EDGH'], 'Treutlen': ['ANNEX', '99999', 'SOPE'], 'Walton': ['99999', '425', '414', '420', '424', '415', '421', '427', '416', '422', '426', '417', '559', '423', '502', '503', '454', '250', '1675', '419', '418'], 'Muscogee': ['105', '119', '104', '118', '107', '102', '99999', '88888', '106', '103', '122', '116', '127', '113', '117', '126', '112', '108', '120', '114', '125', '111', '109', '121', '115', '124', '110'], 'Wheeler': ['2', '88888'], 'Fayette': ['35', '29', '30', '18', '04', '34', '28', '31', '19', '05', '03', '32', '06', '36', '02', '33', '07', '12', '26', '17', '23', '13', '27', '16', '22', '10', '24', '15', '21', '09', '11', '25', '14', '20', '08'], 'Early': ['B', 'JAKIN', 'CO', 'F', 'CS', 'percent', 'D', 'H', 'percent', 'U', 'CUBA'], 'Floyd': ['060', '065', '055', '085', '080', '050', '130', '030', '135', '035', '105', '115', '015', '110', '076', '010', '020', '025', '125', '045', '090', '040', '140', '075'], 'Chattahoochee': ['88888', '99999'], 'Towns': ['833', '99999', '1581', '990'], 'Bryan': ['2', '7', '10', '3', '6', '88888', '5', '4', '8', '9'], 'Lincoln': ['2', '4-A', '3-A', '1-B', '88888', '3-B', '4-B'], 'Dade': ['974', '1885', '1214', '99999', '1889', '1222', '960'], 'Franklin': ['3', '6', '2', '7', '4', '5'], 'Walker': ['1893', '0944', '0917', '1809', '1812', '88888', '1501', '1851', '0953', '1161', '1818'], 'Terrell': ['05', '04', '88888', '02', '06', '03'], 'Carroll': ['716', '1122', '641', '714BN', '1540', '713', '714A2', '1240', '714A6', '640', '1371', '714A3', '714BW', '714A5', '1111', '1542', '715', '714A4', '1496', '642', '714A1', '1163', '1152', '1483', '682', '501', '649', '88888', '99999', '650', '1533'], 'Murray': ['1039', '874', '1895', '824', '1291', '872'], 'Talbot': ['03', '06', '02', '04', '05', '08'], 'Tift': ['05', '04', '99999', '07', '02', '06', '03', '12', '08', '11', '09', '10'], 'Peach': ['F1', '1', 'F3', 'F2', 'B1', '99999', 'B2', '1'], 'Pike': ['8', '7', '2', '6', '88888', '3', '5', '4'], 'Sumter': ['C3-27', '88888', 'C2-27', '17', 'W-27', 'O-26', '-27', 'C1-27', '29', 'N-26', '28'], 'Calhoun': ['2', '3', '5', '4'], 'Douglas': ['740', '1260', '739', '738', '1259', '731', '1271', '734', '1274', '730', '1270', '736S', '735', '1275', '729', '785', '736N', '1273', '733', '1276', '784', '1272', '732', '737', '88888', '99999'], 'Pulaski': ['NNEX', '99999'], 'Atkinson': ['99999', '88888', '0004', '0002', '0003'], 'DeKalb': ['JB', 'RJ', 'CL', 'GB', 'MV', 'PB', 'percent', 'percent', 'MH', 'F', 'SF', 'CR', 'CI', 'percent', 'PG', 'MS', 'percent', 'C', 'CW', 'SC', 'FK', 'percent', 'RK', 'GC', 'CM', 'PC', 'MW', 'percent', 'percent', 'MI', 'G', 'SG', 'WI', 'CS', 'OA', 'RN', 'CH', 'GF', 'MR', 'PF', 'TH', 'percent', 'ML', 'IB', 'CV', 'WL', 'SB', 'percent', 'FJ', 'RH', 'F', 'MT', 'HH', 'MJ', 'FL', 'percent', 'SD', 'WJ', 'OB', 'CP', 'CK', 'RM', 'C', 'MQ', 'PE', 'percent', 'MO', 'IA', 'CU', 'G', 'SA', 'JA', 'CO', 'GA', 'RI', 'G', 'MU', 'PA', 'HI', 'MK', 'percent', 'C', 'FM', 'WK', 'SE', 'CQ', 'GD', 'CJ', 'RL', 'VB', 'percent', 'percent', 'MP', 'MN', 'R', 'CT', 'F', 'WN', 'TC', 'percent', 'RE', 'CC', '99999', 'NC', 'percent', 'SI', 'WG', 'FA', 'I', 'MG', 'PH', 'TF', 'NF', 'SR', 'CF', 'WB', 'SL', 'J', 'percent', 'MB', 'RD', 'CB', 'NB', 'SV', 'WF', 'SH', 'H', 'PR', 'MF', 'TG', 'PI', 'percent', 'HA', 'SS', 'RA', 'CG', 'SM', 'WC', 'FE', 'OK', 'percent', 'MC', 'HG', 'YA', 'G', 'I', 'TA', 'CA', 'RG', 'SU', 'C', 'M', 'FC', 'SK', 'ME', 'HB', 'SP', 'ND', 'CD', 'OV', 'H', 'SN', 'CZ', 'HF', 'H', 'H', 'F', 'MZ', 'PN', 'RF', 'ST', 'R', 'percent', 'FB', 'percent', 'SJ', 'WD', 'V', 'MD', 'C', 'HC', 'SQ', 'CE', 'RC', 'I', 'FG', 'WA', 'SO', 'G', 'MA'], 'Crisp': ['ORDE', 'LISTO', 'ARABI', 'JAMES', 'ONEY'], 'Troup': ['04', '99999', '88888', '05', '06', '03', '07', '02', '12', '16', '13', '15', '09', '10', '08', '11'], 'Crawford': ['5', '4', '2', '3', '1B'], 'Long': ['2', '7', '3', '6', '5', '4', '88888', '99999'], 'Gilmer': ['09', '10', '08', '11', '12', '13', '06', '03', '07', '02', '04', '05'], 'Bleckley': ['99999', '88888'], 'Gwinnett': ['080', '050', '036', '078', '102', '150', '064', '002', '136', '055', '085', '107', '149', '033', '061', '155', '099', '133', '007', '049', '081', '051', '079', '037', '103', '151', '065', '003', '137', '054', '084', '148', '106', '032', '060', '154', '098', '132', '048', '006', '128', '082', '052', '034', '100', '152', '066', '028', '134', '057', '019', '087', '105', '031', '063', '119', '131', '005', '129', '083', '053', '035', '101', '153', '029', '067', '135', '99999', '018', '056', '88888', '086', '104', '030', '062', '118', '156', '130', '004', '143', '077', '039', '011', '125', '093', '139', '043', '025', '111', '072', '146', '108', '120', '014', '046', '008', '096', '114', '020', '142', '038', '076', '010', '124', '092', '138', '042', '024', '110', '073', '109', '147', '121', '015', '009', '047', '097', '115', '021', '141', '075', '013', '127', '091', '041', '027', '069', '113', '070', '144', '122', '088', '016', '058', '044', '094', '116', '022', '140', '074', '012', '126', '090', '040', '068', '026', '112', '071', '145', '123', '089', '059', '017', '045', '095', '117', '023'], 'Clayton': ['MO5', 'RD10', 'JB05', 'FP5', 'J2', 'RD09', 'MO4', 'RD11', 'JB18', 'JB04', 'FP4', 'MO1', 'J3', 'JB01', 'RD08', 'FP1', 'MO7', 'RD12', 'J5', 'JB07', 'MO2', 'JB02', 'FP2', 'MO6', 'J4', 'JB06', 'FP6', 'MO3', 'J1', 'JB03', 'FP3', 'JB16', 'RD03', 'K3', 'JB13', 'RD06', 'JB17', 'RD02', 'K2', 'JB12', 'PH2', 'RD07', 'EW1', 'JB14', 'MO8', 'RD01', 'K1', 'JB08', '1', 'JB11', 'PH1', 'RD04', 'K4', 'JB15', 'MO9', '99999', 'JB09', 'JB10', 'RD05'], 'Brantley': ['3', '2'], 'Quitman': ['percent'], 'Hancock': ['2B', '4A', '1B', '4C', '2A', '4B', '3A', '3C', '99999', '3B'], 'Jones': ['8', '9', '10', '11', 'DODGE', '2', '3', '6', '5', '4'], 'Pierce': ['88888', '99999', '3A', '3B', '0002', '4D', '4A', '4B', '4C'], 'Laurens': ['07', '06', '19', '05', '99999', '04', '14', '08', '11', '15', '21', '09', '10', '16', '22', '13', '12'], 'Berrien': ['99999', '88888', '1157', '518', '1642', '1144'], 'Lamar': ['1712C', '88888', '1714', '1712B', '1712A', '1713'], 'Emanuel': ['1208', '0058', '88888', '1429', '1560', '0052', '1748', '1333', '0057', '0053', '1502'], 'Telfair': ['MC', 'HE', 'U', 'MI', 'SC', 'JA'], 'Banks': ['0005', '0004', '0002', '0007', '0003', '0006', '0013', '0012', '0011', '0008', '0010', '0009'], 'Mitchell': ['PE', 'N', 'percent', 'percent', 'SC', 'S', 'BA', 'PC', 'BV', 'S', 'F'], 'Stewart': ['06', '99999', '88888', '04', '05'], 'Houston': ['AFS', 'PC', 'RECR', 'EFS', 'WPK', 'FMMS', 'ROZR', 'MCMS', 'CENT', 'ANNX', 'BMS', 'CGTC', 'MS', '99999', 'ES', 'MILL', 'VHS', 'CTC'], 'Whitfield': ['MC', '2A', 'percent', '88888', 'GL', 'UT', 'AN', 'BLCK', '4A', 'CA', 'percent', 'G', '5A', '6A', 'PG', 'percent', 'S', 'NI', 'VA', 'R', 'CO', 'percent', 'S', '3A'], 'Spalding': ['14', '08', '20', '11', '15', '09', '21', '10', '16', '13', '17', '12', '07', '02', '06', '03', '19', '05', '18', '04', '99999'], 'Miller': [], 'Habersham': ['05', '99999', '88888', '04', '07', '02', '06', '03'], 'Rabun': ['percent'], 'Bulloch': ['5', '4', '2', '7', '3', '6', '16', '13', '12', '14', '11', '8', '15', '10', '9'], 'Fannin': ['TOCC', 'HOTH', 'HEMP', 'SKEN', 'SUGC', 'OON', 'LIN', 'COLW', 'R', '99999', 'MINE', 'MORG', 'MOBI'], 'Tattnall': ['3', '7', '88888', '4', '5', '9', '10', '8'], 'Turner': ['3', '2'], 'Twiggs': ['HV', '-T', 'percent', 'JV-W'], 'Randolph': ['947', '718B', '334', '954', '998', '566', '934', '718A', '99999'], 'Monroe': ['13', '12', '11', '08', '14', '10', '09', '05', '04', '02', '07', '03', '06']}
#print dictt
import requests
import json
from collections import defaultdict
import time

# 1) GET TEAMID FROM SEARCHING ORG LIST DONE
# 2) USE TEAMID TO SEARCH FOR RECENT MATCHES, -> GET MATCHID FOR STAGE 2
# 3) COLLECT MATCHID DATA FOR CALCULATIONS
# 4) CALCULATE ALL TEAM MATCH DATA
# 5) OUTPUT INTO PANDA DF FOR USE IN SPREADHSHEET


base_Link = "http://127.0.0.1:3001"

orgList = ["DFM","FS","GE","GEN", "KRX","NS","PRX","RRQ","T1","TS","VL","ZETA","BBL","EF","FNC","FUT","GX","KC","M8","NAVI","PCF","TH","TL","VIT","100T","C9","EG","ENVY","FUR","G2","KRÜ","LEV","LOUD","MIBR","NRG","SEN"]
# COMPLETE PLAYERLIST WITH EMEA AND PACIFIC TEAMS
playerList = ["keiko", "basic", "spike", "zekken", "Paincakes", "Rossy", "vora", "erde", "johnqt", "Zellsis", "Less", "trent", "Meiy", "primmie", "UdoTan", "t3xture", "Mako", "Dambi", "something", "Jemkin", "stax", "Zeus", "Foxy9", "Absol", "Lar0k", "echo", "kaajak", "yetujey", "westside", "dos9", "Minny", "Ruxic", "seven", "benjyfishy", "kamo", "Derke"]
tempStore = 0

# change id to real teamid list
finalOutput = defaultdict(dict)
with open ('orgIDsNoName', 'w', encoding='utf8') as file:
        for i in orgList:
                statsResponse = requests.get(f"{base_Link}/v2/search?q={i}")
                if statsResponse.status_code == 200:
                        statsData = statsResponse.json()
                        print(statsData)
                        
                        orgID = statsData['data']['segments']['results']['teams'][0]['id']
                        #orgName = statsData['data']['segments']['results']['teams'][0]['name']
                                
                        finalOutput[tempStore] = orgID
                        tempStore += 1
        file.write(json.dumps(finalOutput))